import os
import time
from typing import Dict, Any, List, Optional
from datetime import datetime
from dotenv import load_dotenv
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import Selector

# Import utility functions
from utils.helpers import publish_scraped_data

class CustomSpider(Spider):
    """Custom Scrapy spider for web scraping"""
    name = 'osint_spider'
    
    def __init__(self, url=None, selectors=None, *args, **kwargs):
        super(CustomSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url] if url else []
        self.selectors = selectors or {}
        self.results = []
    
    def parse(self, response):
        """Parse the response and extract data based on selectors"""
        data = {}
        
        # Extract title
        data['title'] = response.css('title::text').get()
        
        # Extract content based on provided selectors
        for key, selector in self.selectors.items():
            if selector.startswith('//'):
                # XPath selector
                data[key] = response.xpath(selector).getall()
            else:
                # CSS selector
                data[key] = response.css(selector).getall()
        
        # Extract all text content if no specific selectors
        if not self.selectors:
            data['content'] = '\n'.join(response.css('body ::text').getall())
        
        # Add URL and timestamp
        data['url'] = response.url
        data['scraped_at'] = datetime.now().isoformat()
        
        self.results.append(data)
        yield data

class RegularScraper:
    """Regular web scraper using Selenium or Scrapy"""
    
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize status
        self.status = {
            "selenium_available": self._check_selenium(),
            "scrapy_available": True  # Scrapy is a Python library, so it should be available
        }
    
    def _check_selenium(self) -> bool:
        """Check if Selenium with Chrome is available"""
        try:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            driver = webdriver.Chrome(options=options)
            driver.quit()
            return True
        except Exception:
            return False
    
    def check_status(self) -> Dict[str, bool]:
        """Check the status of the scraper components"""
        return self.status
    
    async def scrape(self, scrape_params: Dict[str, Any]) -> bool:
        """Scrape data from a website based on parameters"""
        url = scrape_params.get("url")
        if not url:
            print("URL is required for scraping")
            return False
        
        method = scrape_params.get("method", "selenium").lower()
        selectors = scrape_params.get("selectors", {})
        wait_for = scrape_params.get("wait_for", None)  # CSS selector to wait for
        timeout = scrape_params.get("timeout", 30)  # seconds
        
        try:
            if method == "selenium" and self.status["selenium_available"]:
                return await self._scrape_with_selenium(url, selectors, wait_for, timeout)
            elif method == "scrapy" and self.status["scrapy_available"]:
                return await self._scrape_with_scrapy(url, selectors)
            elif method == "requests":
                return await self._scrape_with_requests(url)
            else:
                print(f"Scraping method {method} not available")
                return False
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return False
    
    async def _scrape_with_selenium(self, url: str, selectors: Dict[str, str], wait_for: Optional[str], timeout: int) -> bool:
        """Scrape a website using Selenium"""
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Chrome(options=options)
        try:
            driver.get(url)
            
            # Wait for specific element if requested
            if wait_for:
                WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, wait_for))
                )
            else:
                # Default wait for page to load
                time.sleep(5)
            
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
            return publish_scraped_data(data, url, False)
        
        finally:
            driver.quit()
    
    async def _scrape_with_scrapy(self, url: str, selectors: Dict[str, str]) -> bool:
        """Scrape a website using Scrapy"""
        spider = CustomSpider(url=url, selectors=selectors)
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'LOG_LEVEL': 'ERROR'
        })
        
        process.crawl(spider)
        process.start()  # This will block until the crawling is finished
        
        # Check if we got any results
        if spider.results:
            # Publish to Kafka
            for result in spider.results:
                publish_scraped_data(result, url, False)
            return True
        return False
    
    async def _scrape_with_requests(self, url: str) -> bool:
        """Simple scraping using requests library"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
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
            return publish_scraped_data(data, url, False)
        
        return False