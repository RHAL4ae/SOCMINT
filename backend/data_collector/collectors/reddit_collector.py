import os
import requests
from typing import Dict, Any, List, Optional
from datetime import datetime
from dotenv import load_dotenv

# Import utility functions
from utils.helpers import publish_social_data

class RedditCollector:
    """Reddit API data collector"""
    
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Reddit API credentials
        self.client_id = os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        self.username = os.getenv("REDDIT_USERNAME")
        self.password = os.getenv("REDDIT_PASSWORD")
        self.user_agent = os.getenv("REDDIT_USER_AGENT", "OSINT Data Collector v1.0")
        
        # Reddit API base URL
        self.api_base_url = "https://oauth.reddit.com"
        self.auth_url = "https://www.reddit.com/api/v1/access_token"
        
        # Access token
        self.access_token = None
        self.token_expiry = None
        
        # Check if credentials are available
        self.is_configured = all([self.client_id, self.client_secret, self.username, self.password])
    
    def check_connection(self) -> bool:
        """Check if Reddit API connection is available"""
        if not self.is_configured:
            return False
        
        try:
            # Get access token
            token = self.get_access_token()
            if not token:
                return False
            
            # Try to make a simple API call to check connection
            headers = {"Authorization": f"Bearer {token}", "User-Agent": self.user_agent}
            response = requests.get(
                f"{self.api_base_url}/api/v1/me",
                headers=headers
            )
            return response.status_code == 200
        except Exception:
            return False
    
    def get_access_token(self) -> Optional[str]:
        """Get a valid access token using app credentials"""
        if not self.is_configured:
            return None
        
        # Check if we have a valid token
        if self.access_token and self.token_expiry and datetime.now() < self.token_expiry:
            return self.access_token
        
        try:
            # Get a new access token
            auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
            data = {
                "grant_type": "password",
                "username": self.username,
                "password": self.password
            }
            headers = {"User-Agent": self.user_agent}
            
            response = requests.post(
                self.auth_url,
                auth=auth,
                data=data,
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                self.access_token = data.get("access_token")
                expires_in = data.get("expires_in", 3600)  # Default 1 hour
                self.token_expiry = datetime.now().replace(second=0, microsecond=0)
                self.token_expiry = self.token_expiry.replace(second=self.token_expiry.second + expires_in)
                return self.access_token
            return None
        except Exception as e:
            print(f"Error getting Reddit access token: {e}")
            return None
    
    async def collect(self, query_params: Dict[str, Any]) -> bool:
        """Collect data from Reddit based on query parameters"""
        if not self.is_configured:
            print("Reddit collector not configured properly")
            return False
        
        # Get access token
        access_token = self.get_access_token()
        if not access_token:
            print("Failed to get Reddit access token")
            return False
        
        # Extract parameters
        subreddit = query_params.get("subreddit")
        post_id = query_params.get("post_id")
        search_query = query_params.get("search_query")
        limit = query_params.get("limit", 25)
        sort = query_params.get("sort", "new")
        
        headers = {"Authorization": f"Bearer {access_token}", "User-Agent": self.user_agent}
        collected_data = []
        
        try:
            # Get subreddit posts
            if subreddit and not post_id:
                url = f"{self.api_base_url}/r/{subreddit}/{sort}"
                params = {"limit": limit}
                
                response = requests.get(url, headers=headers, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    posts = data.get("data", {}).get("children", [])
                    
                    for post in posts:
                        post_data = post.get("data", {})
                        
                        # Transform to common format
                        normalized_post = {
                            "id": post_data.get("id"),
                            "text": post_data.get("selftext", post_data.get("title", "")),
                            "title": post_data.get("title", ""),
                            "timestamp": datetime.fromtimestamp(post_data.get("created_utc", 0)).isoformat(),
                            "author": {
                                "id": post_data.get("author_fullname", ""),
                                "name": post_data.get("author", "")
                            },
                            "url": post_data.get("url", ""),
                            "subreddit": post_data.get("subreddit", ""),
                            "score": post_data.get("score", 0),
                            "type": "post"
                        }
                        collected_data.append(normalized_post)
                        
                        # Publish to Kafka
                        publish_social_data(normalized_post, "reddit")
            
            # Get post comments
            if post_id:
                url = f"{self.api_base_url}/comments/{post_id}"
                params = {"limit": limit, "sort": sort}
                
                response = requests.get(url, headers=headers, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    if len(data) >= 2:  # First item is the post, second is comments
                        comments = data[1].get("data", {}).get("children", [])
                        
                        for comment in comments:
                            comment_data = comment.get("data", {})
                            
                            # Skip deleted or removed comments
                            if comment_data.get("body") in ["[deleted]", "[removed]"]:
                                continue
                            
                            # Transform to common format
                            normalized_comment = {
                                "id": comment_data.get("id"),
                                "text": comment_data.get("body", ""),
                                "timestamp": datetime.fromtimestamp(comment_data.get("created_utc", 0)).isoformat(),
                                "author": {
                                    "id": comment_data.get("author_fullname", ""),
                                    "name": comment_data.get("author", "")
                                },
                                "score": comment_data.get("score", 0),
                                "post_id": post_id,
                                "type": "comment"
                            }
                            collected_data.append(normalized_comment)
                            
                            # Publish to Kafka
                            publish_social_data(normalized_comment, "reddit")
            
            # Search for posts
            if search_query:
                url = f"{self.api_base_url}/search"
                params = {
                    "q": search_query,
                    "limit": limit,
                    "sort": sort,
                    "type": "link"  # Search for posts
                }
                
                response = requests.get(url, headers=headers, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    posts = data.get("data", {}).get("children", [])
                    
                    for post in posts:
                        post_data = post.get("data", {})
                        
                        # Transform to common format
                        normalized_post = {
                            "id": post_data.get("id"),
                            "text": post_data.get("selftext", post_data.get("title", "")),
                            "title": post_data.get("title", ""),
                            "timestamp": datetime.fromtimestamp(post_data.get("created_utc", 0)).isoformat(),
                            "author": {
                                "id": post_data.get("author_fullname", ""),
                                "name": post_data.get("author", "")
                            },
                            "url": post_data.get("url", ""),
                            "subreddit": post_data.get("subreddit", ""),
                            "score": post_data.get("score", 0),
                            "type": "search_result",
                            "search_query": search_query
                        }
                        collected_data.append(normalized_post)
                        
                        # Publish to Kafka
                        publish_social_data(normalized_post, "reddit")
            
            return len(collected_data) > 0
        
        except Exception as e:
            print(f"Error collecting data from Reddit: {e}")
            return False