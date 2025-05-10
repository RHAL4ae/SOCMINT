import os
import requests
from typing import Dict, Any, List, Optional
from datetime import datetime
from dotenv import load_dotenv

# Import utility functions
from utils.helpers import publish_social_data

class InstagramCollector:
    """Instagram API data collector"""
    
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Instagram API credentials (using Facebook Graph API for Instagram)
        self.access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN")
        
        # Instagram Graph API base URL
        self.api_base_url = "https://graph.instagram.com"
        self.api_version = "v18.0"
        
        # Check if credentials are available
        self.is_configured = self.access_token is not None
    
    def check_connection(self) -> bool:
        """Check if Instagram API connection is available"""
        if not self.is_configured:
            return False
        
        try:
            # Try to make a simple API call to check connection
            response = requests.get(
                f"{self.api_base_url}/me",
                params={"access_token": self.access_token, "fields": "id,username"}
            )
            return response.status_code == 200
        except Exception:
            return False
    
    async def collect(self, query_params: Dict[str, Any]) -> bool:
        """Collect data from Instagram based on query parameters"""
        if not self.is_configured:
            print("Instagram collector not configured properly")
            return False
        
        # Extract parameters
        user_id = query_params.get("user_id")
        media_id = query_params.get("media_id")
        hashtag = query_params.get("hashtag")
        limit = query_params.get("limit", 25)
        
        collected_data = []
        
        try:
            # Get user media
            if user_id and not media_id:
                url = f"{self.api_base_url}/{user_id}/media"
                params = {
                    "access_token": self.access_token,
                    "fields": "id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username",
                    "limit": limit
                }
                
                response = requests.get(url, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    media_items = data.get("data", [])
                    
                    for media in media_items:
                        # Transform to common format
                        media_data = {
                            "id": media.get("id"),
                            "text": media.get("caption", ""),
                            "timestamp": media.get("timestamp"),
                            "author": {
                                "username": media.get("username")
                            },
                            "media_type": media.get("media_type"),
                            "media_url": media.get("media_url"),
                            "permalink": media.get("permalink"),
                            "type": "post"
                        }
                        collected_data.append(media_data)
                        
                        # Publish to Kafka
                        publish_social_data(media_data, "instagram")
            
            # Get media comments
            if media_id:
                url = f"{self.api_base_url}/{media_id}/comments"
                params = {
                    "access_token": self.access_token,
                    "fields": "id,text,timestamp,username",
                    "limit": limit
                }
                
                response = requests.get(url, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    comments = data.get("data", [])
                    
                    for comment in comments:
                        # Transform to common format
                        comment_data = {
                            "id": comment.get("id"),
                            "text": comment.get("text", ""),
                            "timestamp": comment.get("timestamp"),
                            "author": {
                                "username": comment.get("username")
                            },
                            "media_id": media_id,
                            "type": "comment"
                        }
                        collected_data.append(comment_data)
                        
                        # Publish to Kafka
                        publish_social_data(comment_data, "instagram")
            
            # Get hashtag media
            if hashtag:
                # Note: Hashtag search requires additional permissions and a business account
                # This is a simplified implementation
                print(f"Hashtag search for {hashtag} requires additional permissions")
                # In a real implementation, you would use the Instagram Graph API hashtag endpoints
                # This would require a business account and additional permissions
                
                # Example of how it would work with proper permissions:
                # 1. Get hashtag ID
                # hashtag_url = f"https://graph.facebook.com/{self.api_version}/ig_hashtag_search"
                # hashtag_params = {
                #     "user_id": user_id,
                #     "q": hashtag,
                #     "access_token": self.access_token
                # }
                # hashtag_response = requests.get(hashtag_url, params=hashtag_params)
                # hashtag_id = hashtag_response.json().get("data", [])[0].get("id")
                #
                # 2. Get recent media with hashtag
                # media_url = f"https://graph.facebook.com/{self.api_version}/{hashtag_id}/recent_media"
                # media_params = {
                #     "user_id": user_id,
                #     "access_token": self.access_token,
                #     "fields": "id,caption,media_type,media_url,permalink,timestamp,username",
                #     "limit": limit
                # }
                # media_response = requests.get(media_url, params=media_params)
                # ... process media items as above
            
            return len(collected_data) > 0
        
        except Exception as e:
            print(f"Error collecting data from Instagram: {e}")
            return False