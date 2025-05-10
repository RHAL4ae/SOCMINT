import unittest
import os
import json
import sys
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

# Create a test environment where we mock all external dependencies
# This allows tests to run without requiring actual installations of these packages

# Mock selenium module
class MockSelenium:
    class webdriver:
        class Chrome:
            def __init__(self, *args, **kwargs):
                pass
                
            def get(self, *args, **kwargs):
                pass
                
            def quit(self):
                pass
                
            def find_element(self, *args, **kwargs):
                return MagicMock()
                
            def find_elements(self, *args, **kwargs):
                return []
        
        class chrome:
            class options:
                class Options:
                    def __init__(self):
                        pass
                    
                    def add_argument(self, *args, **kwargs):
                        pass
                    
                    def add_experimental_option(self, *args, **kwargs):
                        pass
        
        class common:
            class by:
                class By:
                    ID = "id"
                    NAME = "name"
                    CLASS_NAME = "class name"
                    CSS_SELECTOR = "css selector"
                    XPATH = "xpath"
    
    class common:
        class exceptions:
            class TimeoutException(Exception):
                pass

sys.modules['selenium'] = MockSelenium
sys.modules['selenium.webdriver'] = MockSelenium.webdriver
sys.modules['selenium.webdriver.chrome'] = MockSelenium.webdriver.chrome
sys.modules['selenium.webdriver.chrome.options'] = MockSelenium.webdriver.chrome.options
sys.modules['selenium.webdriver.common'] = MockSelenium.webdriver.common
sys.modules['selenium.webdriver.common.by'] = MockSelenium.webdriver.common.by
sys.modules['selenium.common.exceptions'] = MockSelenium.common.exceptions

# Mock scrapy module
class MockScrapy:
    class Spider:
        pass
        
    class Request:
        pass
        
    class Item:
        pass

sys.modules['scrapy'] = MockScrapy

# Mock requests module if not already imported
if 'requests' not in sys.modules:
    class MockRequests:
        def get(*args, **kwargs):
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {}
            return mock_response
            
        def post(*args, **kwargs):
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {}
            return mock_response
    
    sys.modules['requests'] = MockRequests

# Mock kafka module to prevent import errors
class MockKafka:
    class KafkaProducer:
        def __init__(self, *args, **kwargs):
            pass
        
        def send(self, *args, **kwargs):
            pass
            
        def flush(self):
            pass
            
        def close(self):
            pass
    
    class errors:
        class KafkaError(Exception):
            pass

sys.modules['kafka'] = MockKafka
sys.modules['kafka.errors'] = MockKafka.errors

# Mock socks module for TOR connection
class MockSocks:
    class socksocket:
        def __init__(self):
            pass
            
        def set_proxy(self, *args, **kwargs):
            pass
            
        def connect(self, *args, **kwargs):
            pass
            
        def close(self):
            pass

sys.modules['socks'] = MockSocks

# Import the FastAPI app
from main import app

# Import collectors and scrapers for mocking
from collectors.facebook_collector import FacebookCollector
from collectors.twitter_collector import TwitterCollector
from collectors.reddit_collector import RedditCollector
from collectors.instagram_collector import InstagramCollector
from collectors.whatsapp_collector import WhatsAppCollector
from scraper.regular_scraper import RegularScraper
from scraper.darkweb_scraper import DarkWebScraper

# Import utility functions
from utils.helpers import check_kafka_connection, check_tor_connection

# Create test client
client = TestClient(app)

class TestDataCollectorAPI(unittest.TestCase):
    """Test cases for the Data Collector API endpoints"""
    
    def setUp(self):
        """Set up test environment"""
        # Mock environment variables
        os.environ["KAFKA_BROKER"] = "kafka:9092"
        os.environ["TOR_PROXY"] = "socks5h://localhost:9050"
    
    @patch('utils.helpers.check_kafka_connection')
    @patch('collectors.facebook_collector.FacebookCollector.check_connection')
    @patch('collectors.twitter_collector.TwitterCollector.check_connection')
    @patch('collectors.reddit_collector.RedditCollector.check_connection')
    @patch('collectors.instagram_collector.InstagramCollector.check_connection')
    @patch('scraper.regular_scraper.RegularScraper.check_status')
    @patch('scraper.darkweb_scraper.DarkWebScraper.check_status')
    def test_status_endpoint(self, mock_darkweb, mock_regular, mock_instagram, 
                            mock_reddit, mock_twitter, mock_facebook, mock_kafka):
        """Test the /status endpoint"""
        # Configure mocks
        mock_kafka.return_value = True
        mock_facebook.return_value = True
        mock_twitter.return_value = True
        mock_reddit.return_value = False
        mock_instagram.return_value = True
        mock_regular.return_value = {"selenium_available": True, "scrapy_available": True}
        mock_darkweb.return_value = True
        
        # Make request
        response = client.get("/status")
        
        # Check response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertTrue(data["kafka_connection"])
        self.assertTrue(data["collectors"]["facebook"])
        self.assertTrue(data["collectors"]["twitter"])
        self.assertFalse(data["collectors"]["reddit"])
        self.assertTrue(data["collectors"]["instagram"])
        self.assertTrue(data["scrapers"]["regular"])
        self.assertTrue(data["scrapers"]["darkweb"])
    
    @patch('collectors.facebook_collector.FacebookCollector.collect')
    def test_facebook_collection(self, mock_collect):
        """Test Facebook data collection endpoint"""
        # Configure mock
        mock_collect.return_value = True
        
        # Test data
        test_data = {"page_id": "meta", "limit": 10}
        
        # Make request
        response = client.post("/collect/facebook", json=test_data)
        
        # Check response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["message"], "Facebook data collection completed")
        
        # Verify mock was called with correct parameters
        mock_collect.assert_called_once()
        call_args = mock_collect.call_args[0][0]
        self.assertEqual(call_args["page_id"], "meta")
        self.assertEqual(call_args["limit"], 10)
    
    @patch('collectors.twitter_collector.TwitterCollector.collect')
    def test_twitter_collection(self, mock_collect):
        """Test Twitter data collection endpoint"""
        # Configure mock
        mock_collect.return_value = True
        
        # Test data
        test_data = {"query": "#osint", "max_results": 25}
        
        # Make request
        response = client.post("/collect/twitter", json=test_data)
        
        # Check response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["message"], "Twitter data collection completed")
    
    @patch('collectors.reddit_collector.RedditCollector.collect')
    def test_reddit_collection(self, mock_collect):
        """Test Reddit data collection endpoint"""
        # Configure mock
        mock_collect.return_value = True
        
        # Test data
        test_data = {"subreddit": "osint", "limit": 15, "sort": "new"}
        
        # Make request
        response = client.post("/collect/reddit", json=test_data)
        
        # Check response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["message"], "Reddit data collection completed")
        
        # Verify mock was called with correct parameters
        mock_collect.assert_called_once()
        call_args = mock_collect.call_args[0][0]
        self.assertEqual(call_args["subreddit"], "osint")
        self.assertEqual(call_args["limit"], 15)
        self.assertEqual(call_args["sort"], "new")
    
    @patch('collectors.instagram_collector.InstagramCollector.collect')
    def test_instagram_collection(self, mock_collect):
        """Test Instagram data collection endpoint"""
        # Configure mock
        mock_collect.return_value = True
        
        # Test data
        test_data = {"user_id": "instagram_user", "limit": 10}
        
        # Make request
        response = client.post("/collect/instagram", json=test_data)
        
        # Check response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["message"], "Instagram data collection completed")
        
        # Verify mock was called with correct parameters
        mock_collect.assert_called_once()
        call_args = mock_collect.call_args[0][0]
        self.assertEqual(call_args["user_id"], "instagram_user")
        self.assertEqual(call_args["limit"], 10)
    
    @patch('collectors.whatsapp_collector.WhatsAppCollector.collect')
    def test_whatsapp_collection(self, mock_collect):
        """Test WhatsApp data collection endpoint using generic endpoint"""
        # Configure mock
        mock_collect.return_value = True
        
        # Test data
        test_data = {"phone_number": "1234567890", "limit": 5}
        
        # Make request - using the generic endpoint since there's no specific WhatsApp endpoint
        response = client.post("/collect/whatsapp", json=test_data)
        
        # Check response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["message"], "Whatsapp data collection completed")
        
        # Verify mock was called with correct parameters
        mock_collect.assert_called_once()
        call_args = mock_collect.call_args[0][0]
        self.assertEqual(call_args["phone_number"], "1234567890")
        self.assertEqual(call_args["limit"], 5)
    
    @patch('scraper.regular_scraper.RegularScraper.scrape')
    def test_web_scraping(self, mock_scrape):
        """Test web scraping endpoint"""
        # Configure mock
        mock_scrape.return_value = True
        
        # Test data
        test_data = {
            "url": "https://example.com",
            "method": "selenium",
            "selectors": {"headlines": "h1, h2, h3", "paragraphs": "p"}
        }
        
        # Make request
        response = client.post("/scrape", json=test_data)
        
        # Check response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["message"], "Web scraping completed")
    
    @patch('scraper.darkweb_scraper.DarkWebScraper.check_status')
    @patch('scraper.darkweb_scraper.DarkWebScraper.scrape')
    def test_darkweb_scraping(self, mock_scrape, mock_check):
        """Test dark web scraping endpoint"""
        # Configure mocks
        mock_check.return_value = True
        mock_scrape.return_value = True
        
        # Test data
        test_data = {
            "url": "http://example.onion",
            "method": "requests",
            "timeout": 120
        }
        
        # Make request
        response = client.post("/scrape/darkweb", json=test_data)
        
        # Check response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["message"], "Dark web scraping completed")
    
    @patch('scraper.darkweb_scraper.DarkWebScraper.check_status')
    def test_darkweb_scraping_no_tor(self, mock_check):
        """Test dark web scraping endpoint when TOR is not available"""
        # Configure mock
        mock_check.return_value = False
        
        # Test data
        test_data = {
            "url": "http://example.onion",
            "method": "requests"
        }
        
        # Make request
        response = client.post("/scrape/darkweb", json=test_data)
        
        # Check response
        self.assertEqual(response.status_code, 503)
        data = response.json()
        self.assertEqual(data["detail"], "TOR connection not available")

class TestFacebookCollector(unittest.TestCase):
    """Test cases for the Facebook collector"""
    
    def setUp(self):
        """Set up test environment"""
        # Mock environment variables
        os.environ["FACEBOOK_APP_ID"] = "test_app_id"
        os.environ["FACEBOOK_APP_SECRET"] = "test_app_secret"
        os.environ["FACEBOOK_ACCESS_TOKEN"] = "test_access_token"
        
        # Initialize collector
        self.collector = FacebookCollector()
    
    @patch('requests.get')
    def test_check_connection(self, mock_get):
        """Test Facebook connection check"""
        # Configure mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Check connection
        result = self.collector.check_connection()
        
        # Verify result
        self.assertTrue(result)
        mock_get.assert_called_once()
    
    @patch('requests.get')
    @patch('utils.helpers.publish_social_data')
    def test_collect(self, mock_publish, mock_get):
        """Test Facebook data collection"""
        # Configure mocks
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [
                {
                    "id": "123456789",
                    "message": "Test post",
                    "created_time": "2023-01-01T12:00:00+0000",
                    "from": {"id": "987654321", "name": "Test User"}
                }
            ]
        }
        mock_get.return_value = mock_response
        mock_publish.return_value = True
        
        # Test data
        query_params = {"page_id": "meta", "limit": 1}
        
        # Collect data
        import asyncio
        result = asyncio.run(self.collector.collect(query_params))
        
        # Verify result
        self.assertTrue(result)
        mock_get.assert_called_once()
        mock_publish.assert_called_once()

class TestInstagramCollector(unittest.TestCase):
    """Test cases for the Instagram collector"""
    
    def setUp(self):
        """Set up test environment"""
        # Mock environment variables
        os.environ["INSTAGRAM_ACCESS_TOKEN"] = "test_access_token"
        
        # Initialize collector
        self.collector = InstagramCollector()
    
    @patch('requests.get')
    def test_check_connection(self, mock_get):
        """Test Instagram connection check"""
        # Configure mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Check connection
        result = self.collector.check_connection()
        
        # Verify result
        self.assertTrue(result)
        mock_get.assert_called_once()
    
    @patch('requests.get')
    @patch('utils.helpers.publish_social_data')
    def test_collect_by_user_id(self, mock_publish, mock_get):
        """Test Instagram data collection by user ID"""
        # Configure mocks
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [
                {
                    "id": "123456789",
                    "caption": "Test post",
                    "timestamp": "2023-01-01T12:00:00+0000",
                    "media_type": "IMAGE",
                    "media_url": "https://example.com/image.jpg"
                }
            ]
        }
        mock_get.return_value = mock_response
        mock_publish.return_value = True
        
        # Test data
        query_params = {"user_id": "instagram_user", "limit": 1}
        
        # Collect data
        import asyncio
        result = asyncio.run(self.collector.collect(query_params))
        
        # Verify result
        self.assertTrue(result)
        mock_get.assert_called_once()
        mock_publish.assert_called_once()
    
    def test_collect_not_configured(self):
        """Test Instagram collection when not configured"""
        # Temporarily clear environment variables
        original_token = os.environ.pop("INSTAGRAM_ACCESS_TOKEN", None)
        
        try:
            # Reinitialize collector without configuration
            self.collector = InstagramCollector()
            
            # Test data
            query_params = {"user_id": "instagram_user"}
            
            # Collect data
            import asyncio
            result = asyncio.run(self.collector.collect(query_params))
            
            # Verify result
            self.assertFalse(result)
        finally:
            # Restore environment variable
            if original_token:
                os.environ["INSTAGRAM_ACCESS_TOKEN"] = original_token

class TestRedditCollector(unittest.TestCase):
    """Test cases for the Reddit collector"""
    
    def setUp(self):
        """Set up test environment"""
        # Mock environment variables
        os.environ["REDDIT_CLIENT_ID"] = "test_client_id"
        os.environ["REDDIT_CLIENT_SECRET"] = "test_client_secret"
        os.environ["REDDIT_USERNAME"] = "test_username"
        os.environ["REDDIT_PASSWORD"] = "test_password"
        
        # Initialize collector
        self.collector = RedditCollector()
    
    @patch('requests.post')
    @patch('requests.get')
    def test_check_connection(self, mock_get, mock_post):
        """Test Reddit connection check"""
        # Configure mocks for token request
        mock_token_response = MagicMock()
        mock_token_response.status_code = 200
        mock_token_response.json.return_value = {"access_token": "test_token", "expires_in": 3600}
        mock_post.return_value = mock_token_response
        
        # Configure mocks for API request
        mock_api_response = MagicMock()
        mock_api_response.status_code = 200
        mock_get.return_value = mock_api_response
        
        # Check connection
        result = self.collector.check_connection()
        
        # Verify result
        self.assertTrue(result)
        mock_post.assert_called_once()
        mock_get.assert_called_once()
    
    @patch('requests.post')
    @patch('requests.get')
    @patch('utils.helpers.publish_social_data')
    def test_collect_by_subreddit(self, mock_publish, mock_get, mock_post):
        """Test Reddit data collection by subreddit"""
        # Configure mocks for token request
        mock_token_response = MagicMock()
        mock_token_response.status_code = 200
        mock_token_response.json.return_value = {"access_token": "test_token", "expires_in": 3600}
        mock_post.return_value = mock_token_response
        
        # Configure mocks for API request
        mock_api_response = MagicMock()
        mock_api_response.status_code = 200
        mock_api_response.json.return_value = {
            "data": {
                "children": [
                    {
                        "data": {
                            "id": "abc123",
                            "title": "Test post",
                            "selftext": "Test content",
                            "created_utc": 1672567200,  # 2023-01-01 12:00:00 UTC
                            "author": "test_user",
                            "subreddit": "test_subreddit"
                        }
                    }
                ]
            }
        }
        mock_get.return_value = mock_api_response
        mock_publish.return_value = True
        
        # Test data
        query_params = {"subreddit": "osint", "limit": 1}
        
        # Collect data
        import asyncio
        result = asyncio.run(self.collector.collect(query_params))
        
        # Verify result
        self.assertTrue(result)
        self.assertEqual(mock_post.call_count, 1)
        self.assertEqual(mock_get.call_count, 1)
        mock_publish.assert_called_once()
    
    def test_collect_not_configured(self):
        """Test Reddit collection when not configured"""
        # Temporarily clear environment variables
        original_client_id = os.environ.pop("REDDIT_CLIENT_ID", None)
        
        try:
            # Reinitialize collector without configuration
            self.collector = RedditCollector()
            
            # Test data
            query_params = {"subreddit": "osint"}
            
            # Collect data
            import asyncio
            result = asyncio.run(self.collector.collect(query_params))
            
            # Verify result
            self.assertFalse(result)
        finally:
            # Restore environment variable
            if original_client_id:
                os.environ["REDDIT_CLIENT_ID"] = original_client_id

class TestWhatsAppCollector(unittest.TestCase):
    """Test cases for the WhatsApp collector"""
    
    def setUp(self):
        """Set up test environment"""
        # Mock environment variables
        os.environ["WHATSAPP_API_KEY"] = "test_api_key"
        os.environ["WHATSAPP_PHONE_NUMBER_ID"] = "test_phone_number_id"
        os.environ["WHATSAPP_BUSINESS_ACCOUNT_ID"] = "test_business_account_id"
        
        # Initialize collector
        self.collector = WhatsAppCollector()
    
    @patch('requests.get')
    def test_check_connection(self, mock_get):
        """Test WhatsApp connection check"""
        # Configure mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Check connection
        result = self.collector.check_connection()
        
        # Verify result
        self.assertTrue(result)
        mock_get.assert_called_once()
    
    @patch('utils.helpers.publish_social_data')
    def test_collect_by_phone_number(self, mock_publish):
        """Test WhatsApp data collection by phone number"""
        # Configure mock
        mock_publish.return_value = True
        
        # Test data
        query_params = {"phone_number": "1234567890", "limit": 3}
        
        # Collect data
        import asyncio
        result = asyncio.run(self.collector.collect(query_params))
        
        # Verify result
        self.assertTrue(result)
        # Should be called 3 times (once for each simulated message)
        self.assertEqual(mock_publish.call_count, 3)
    
    @patch('utils.helpers.publish_social_data')
    def test_collect_by_message_id(self, mock_publish):
        """Test WhatsApp data collection by message ID"""
        # Configure mock
        mock_publish.return_value = True
        
        # Test data
        query_params = {"message_id": "wamid.123456789"}
        
        # Collect data
        import asyncio
        result = asyncio.run(self.collector.collect(query_params))
        
        # Verify result
        self.assertTrue(result)
        mock_publish.assert_called_once()
    
    def test_collect_not_configured(self):
        """Test WhatsApp collection when not configured"""
        # Temporarily clear environment variables
        original_api_key = os.environ.pop("WHATSAPP_API_KEY", None)
        
        try:
            # Reinitialize collector without configuration
            self.collector = WhatsAppCollector()
            
            # Test data
            query_params = {"phone_number": "1234567890"}
            
            # Collect data
            import asyncio
            result = asyncio.run(self.collector.collect(query_params))
            
            # Verify result
            self.assertFalse(result)
        finally:
            # Restore environment variable
            if original_api_key:
                os.environ["WHATSAPP_API_KEY"] = original_api_key

class TestHelpers(unittest.TestCase):
    """Test cases for helper functions"""
    
    @patch('kafka.KafkaProducer')
    def test_check_kafka_connection(self, mock_producer):
        """Test Kafka connection check"""
        # Configure mock
        mock_producer.return_value = MagicMock()
        
        # Check connection
        result = check_kafka_connection()
        
        # Verify result
        self.assertTrue(result)
        mock_producer.assert_called_once()
    
    @patch('socks.socksocket')
    def test_check_tor_connection(self, mock_socket):
        """Test TOR connection check"""
        # Configure mock
        mock_instance = MagicMock()
        mock_socket.return_value = mock_instance
        
        # Check connection
        result = check_tor_connection()
        
        # Verify result
        self.assertTrue(result)
        mock_socket.assert_called_once()
        mock_instance.set_proxy.assert_called_once()
        mock_instance.connect.assert_called_once()
        mock_instance.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()