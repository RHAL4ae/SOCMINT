import os
import time
from typing import Dict, Any, List, Optional
from datetime import datetime
from dotenv import load_dotenv
import requests
import socks
import socket
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

# Import utility functions
from utils.helpers import publish_scraped_data, check_tor_connection

class DarkWebScraper:
    """Dark web scraper using TOR SOCKS5 proxy"""
    
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # TOR proxy configuration
        self.tor_proxy = os.getenv("TOR_PROXY", "socks5h://localhost:9050")
        self.proxy_parts = self.tor_proxy.split('://')
        
        # Parse proxy type and address
        if len(self.proxy_parts) == 2:
            self.proxy_type = self.proxy_parts[0]
            self.proxy_addr = self.proxy_parts[1]
            
            # Split host and port
            host_port = self.proxy_addr.split(':')
            if len(host_port) == 2:
                self.proxy_host = host_port[0]
                self.proxy_port = int(host_port[1])
            else:
                self.proxy_host = self.proxy_addr
                self.proxy_port = 9050  # Default TOR port
        else:
            self.proxy_type = "socks5h"
            self.proxy_host = "localhost"
            self.proxy_port = 9050
    
    def check_status(self) -> bool:
        """Check if TOR connection is available"""
        return check_tor_connection()
    
    def _configure_selenium_for_tor(self) -> webdriver.Chrome:
        """Configure Selenium to use TOR proxy"""
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Configure proxy
        options.add_argument(f'--proxy-server={self.tor_proxy}')
        
        return webdriver.Chrome(options=options)
    
    def _configure_requests_for_tor(self) -> requests.Session:
        """Configure requests session to use TOR proxy"""
        session = requests.Session()
        
        # Set up SOCKS proxy
        if self.proxy_type == 'socks5h':
            proxy_type = socks.SOCKS5
        elif self.proxy_type == 'socks4':
            proxy_type = socks.SOCKS4
        else:
            raise ValueError(f"Unsupported proxy type: {self.proxy_type}")
        
        # Apply proxy to session
        session.proxies = {
            'http': self.tor_proxy,
            'https': self.tor_proxy
        }
        
        # Set default timeout
        session.timeout = 60
        
        return session
    
    async def scrape(self, scrape_params: Dict[str, Any]) -> bool:
        """Scrape data from a dark web site based on parameters"""
        # Check TOR connection first
        if not self.check_status():
            print("TOR connection not available")
            return False
        
        url = scrape_params.get("url")
        if not url:
            print("URL is required for scraping")
            return False
        
        method = scrape_params.get("method", "requests").lower()
        selectors = scrape_params.get("selectors", {})
        timeout = scrape_params.get("timeout", 60)  # seconds
        
        try:
            if method == "selenium":
                return await self._scrape_with_selenium(url, selectors, timeout)
            else:  # Default to requests
                return await self._scrape_with_requests(url, timeout)
        except Exception as e:
            print(f"Error scraping dark web site {url}: {e}")
            return False
    
    async def _scrape_with_selenium(self, url: str, selectors: Dict[str, str], timeout: int) -> bool:
        """Scrape a dark web site using Selenium with TOR proxy"""
        driver = self._configure_selenium_for_tor()
        try:
            driver.set_page_load_timeout(timeout)
            driver.get(url)
            
            # Default wait for page to load
            time.sleep(10)  # Dark web sites can be slow
            
            # Extract data based on selectors
            data = {}
            data['title'] = driver.title
            data['url'] = url
            
            # Extract content based on provided selectors
            for key, selector in selectors.items():
                try:
                    if selector.startswith('//'):
                        # XPath selector
                        elements = driver.find_elements(By.XPATH, selector)
                        data[key] = [elem.text for elem in elements]
                    else:
                        # CSS selector
                        elements = driver.find_elements(By.CSS_SELECTOR, selector)
                        data[key] = [elem.text for elem in elements]
                except Exception as e:
                    print(f"Error extracting {key} with selector {selector}: {e}")
                    data[key] = []
            
            # If no selectors provided, get all text content
            if not selectors:
                data['content'] = driver.find_element(By.TAG_NAME, 'body').text
            
            # Get page source
            data['html'] = driver.page_source
            
            # Publish to Kafka
            return publish_scraped_data(data, url, True)
        
        finally:
            driver.quit()
    
    async def _scrape_with_requests(self, url: str, timeout: int) -> bool:
        """Scrape a dark web site using requests with TOR proxy"""
        session = self._configure_requests_for_tor()
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        try:
            response = session.get(url, headers=headers, timeout=timeout)
            
            if response.status_code == 200:
                # Extract basic information
                data = {
                    'url': url,
                    'content': response.text,
                    'status_code': response.status_code,
                    'headers': dict(response.headers)
                }
                
                # Try to extract title
                try:
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(response.text, 'html.parser')
                    data['title'] = soup.title.string if soup.title else ''
                except ImportError:
                    # BeautifulSoup not available
                    import re
                    title_match = re.search('<title>(.*?)</title>', response.text, re.IGNORECASE)
                    data['title'] = title_match.group(1) if title_match else ''
                
                # Publish to Kafka
                return publish_scraped_data(data, url, True)
            
            return False
        
        except Exception as e:
            print(f"Error making request to {url}: {e}")
            return False