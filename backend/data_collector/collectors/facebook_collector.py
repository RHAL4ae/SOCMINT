import os
import requests
from typing import Dict, Any, List, Optional
from datetime import datetime
from dotenv import load_dotenv

# Import utility functions
from utils.helpers import publish_social_data

class FacebookCollector:
    """Facebook API data collector"""
    
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Facebook API credentials
        self.app_id = os.getenv("FACEBOOK_APP_ID")
        self.app_secret = os.getenv("FACEBOOK_APP_SECRET")
        self.access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")
        
        # Facebook Graph API base URL
        self.api_base_url = "https://graph.facebook.com/v18.0"
        
        # Check if credentials are available
        self.is_configured = all([self.app_id, self.app_secret, self.access_token])
    
    def check_connection(self) -> bool:
        """Check if Facebook API connection is available"""
        if not self.is_configured:
            return False
        
        try:
            # Try to make a simple API call to check connection
            response = requests.get(
                f"{self.api_base_url}/me",
                params={"access_token": self.access_token}
            )
            return response.status_code == 200
        except Exception:
            return False
    
    def get_access_token(self) -> Optional[str]:
        """Get a valid access token using app credentials"""
        if not self.is_configured:
            return None
        
        # If we already have an access token, use it
        if self.access_token:
            return self.access_token
        
        try:
            # Get an app access token
            response = requests.get(
                f"{self.api_base_url}/oauth/access_token",
                params={
                    "client_id": self.app_id,
                    "client_secret": self.app_secret,
                    "grant_type": "client_credentials"
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                self.access_token = data.get("access_token")
                return self.access_token
            return None
        except Exception:
            return None
    
    async def collect(self, query_params: Dict[str, Any]) -> bool:
        """Collect data from Facebook based on query parameters"""
        if not self.is_configured:
            print("Facebook collector not configured properly")
            return False
        
        # Get access token
        access_token = self.get_access_token()
        if not access_token:
            print("Failed to get Facebook access token")
            return False
        
        # Extract parameters
        page_id = query_params.get("page_id")
        post_id = query_params.get("post_id")
        limit = query_params.get("limit", 25)
        
        try:
            collected_data = []
            
            # Collect page posts
            if page_id and not post_id:
                url = f"{self.api_base_url}/{page_id}/posts"
                params = {
                    "access_token": access_token,
                    "limit": limit,
                    "fields": "id,message,created_time,from"
                }
                response = requests.get(url, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    posts = data.get("data", [])
                    
                    for post in posts:
                        # Transform to common format
                        post_data = {
                            "id": post.get("id"),
                            "text": post.get("message", ""),
                            "timestamp": post.get("created_time"),
                            "author": post.get("from", {}),
                            "type": "post"
                        }
                        collected_data.append(post_data)
                        
                        # Publish to Kafka
                        publish_social_data(post_data, "facebook")
            
            # Collect post comments
            if post_id:
                url = f"{self.api_base_url}/{post_id}/comments"
                params = {
                    "access_token": access_token,
                    "limit": limit,
                    "fields": "id,message,created_time,from"
                }
                response = requests.get(url, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    comments = data.get("data", [])
                    
                    for comment in comments:
                        # Transform to common format
                        comment_data = {
                            "id": comment.get("id"),
                            "text": comment.get("message", ""),
                            "timestamp": comment.get("created_time"),
                            "author": comment.get("from", {}),
                            "type": "comment",
                            "post_id": post_id
                        }
                        collected_data.append(comment_data)
                        
                        # Publish to Kafka
                        publish_social_data(comment_data, "facebook")
            
            return len(collected_data) > 0
        
        except Exception as e:
            print(f"Error collecting data from Facebook: {e}")
            return False