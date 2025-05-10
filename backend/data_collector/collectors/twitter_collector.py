import os
import requests
from typing import Dict, Any, List, Optional
from datetime import datetime
from dotenv import load_dotenv
import base64

# Import utility functions
from utils.helpers import publish_social_data

class TwitterCollector:
    """Twitter API data collector"""
    
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Twitter API credentials
        self.api_key = os.getenv("TWITTER_API_KEY")
        self.api_secret = os.getenv("TWITTER_API_SECRET")
        self.bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
        
        # Twitter API base URLs
        self.api_base_url = "https://api.twitter.com/2"
        self.auth_url = "https://api.twitter.com/oauth2/token"
        
        # Check if credentials are available
        self.is_configured = all([self.api_key, self.api_secret]) or self.bearer_token is not None
    
    def check_connection(self) -> bool:
        """Check if Twitter API connection is available"""
        if not self.is_configured:
            return False
        
        try:
            # Get bearer token if not already available
            bearer_token = self.get_bearer_token()
            if not bearer_token:
                return False
            
            # Try to make a simple API call to check connection
            headers = {"Authorization": f"Bearer {bearer_token}"}
            response = requests.get(
                f"{self.api_base_url}/tweets/search/recent?query=test&max_results=1",
                headers=headers
            )
            return response.status_code == 200
        except Exception:
            return False
    
    def get_bearer_token(self) -> Optional[str]:
        """Get a valid bearer token using app credentials"""
        # If we already have a bearer token, use it
        if self.bearer_token:
            return self.bearer_token
        
        if not self.api_key or not self.api_secret:
            return None
        
        try:
            # Create the bearer token request
            credentials = f"{self.api_key}:{self.api_secret}"
            encoded_credentials = base64.b64encode(credentials.encode()).decode()
            
            headers = {
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
            }
            
            data = {"grant_type": "client_credentials"}
            
            response = requests.post(self.auth_url, headers=headers, data=data)
            
            if response.status_code == 200:
                data = response.json()
                self.bearer_token = data.get("access_token")
                return self.bearer_token
            return None
        except Exception:
            return None
    
    async def collect(self, query_params: Dict[str, Any]) -> bool:
        """Collect data from Twitter based on query parameters"""
        if not self.is_configured:
            print("Twitter collector not configured properly")
            return False
        
        # Get bearer token
        bearer_token = self.get_bearer_token()
        if not bearer_token:
            print("Failed to get Twitter bearer token")
            return False
        
        # Extract parameters
        query = query_params.get("query")
        username = query_params.get("username")
        tweet_id = query_params.get("tweet_id")
        max_results = query_params.get("max_results", 25)
        
        headers = {"Authorization": f"Bearer {bearer_token}"}
        collected_data = []
        
        try:
            # Search for tweets
            if query:
                url = f"{self.api_base_url}/tweets/search/recent"
                params = {
                    "query": query,
                    "max_results": max_results,
                    "tweet.fields": "created_at,author_id,text",
                    "user.fields": "name,username",
                    "expansions": "author_id"
                }
                
                response = requests.get(url, headers=headers, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    tweets = data.get("data", [])
                    users = {user["id"]: user for user in data.get("includes", {}).get("users", [])}
                    
                    for tweet in tweets:
                        author_id = tweet.get("author_id")
                        author = users.get(author_id, {})
                        
                        # Transform to common format
                        tweet_data = {
                            "id": tweet.get("id"),
                            "text": tweet.get("text", ""),
                            "timestamp": tweet.get("created_at"),
                            "author": {
                                "id": author_id,
                                "name": author.get("name"),
                                "username": author.get("username")
                            },
                            "type": "tweet"
                        }
                        collected_data.append(tweet_data)
                        
                        # Publish to Kafka
                        publish_social_data(tweet_data, "twitter")
            
            # Get user tweets
            if username and not tweet_id:
                # First get user ID from username
                user_url = f"{self.api_base_url}/users/by/username/{username}"
                user_response = requests.get(user_url, headers=headers)
                
                if user_response.status_code == 200:
                    user_data = user_response.json()
                    user_id = user_data.get("data", {}).get("id")
                    
                    if user_id:
                        # Get user tweets
                        tweets_url = f"{self.api_base_url}/users/{user_id}/tweets"
                        tweets_params = {
                            "max_results": max_results,
                            "tweet.fields": "created_at,text"
                        }
                        
                        tweets_response = requests.get(tweets_url, headers=headers, params=tweets_params)
                        
                        if tweets_response.status_code == 200:
                            tweets_data = tweets_response.json()
                            tweets = tweets_data.get("data", [])
                            
                            for tweet in tweets:
                                # Transform to common format
                                tweet_data = {
                                    "id": tweet.get("id"),
                                    "text": tweet.get("text", ""),
                                    "timestamp": tweet.get("created_at"),
                                    "author": {
                                        "id": user_id,
                                        "username": username
                                    },
                                    "type": "tweet"
                                }
                                collected_data.append(tweet_data)
                                
                                # Publish to Kafka
                                publish_social_data(tweet_data, "twitter")
            
            # Get tweet replies
            if tweet_id:
                url = f"{self.api_base_url}/tweets/search/recent"
                params = {
                    "query": f"conversation_id:{tweet_id}",
                    "max_results": max_results,
                    "tweet.fields": "created_at,author_id,text,in_reply_to_user_id",
                    "user.fields": "name,username",
                    "expansions": "author_id"
                }
                
                response = requests.get(url, headers=headers, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    replies = data.get("data", [])
                    users = {user["id"]: user for user in data.get("includes", {}).get("users", [])}
                    
                    for reply in replies:
                        author_id = reply.get("author_id")
                        author = users.get(author_id, {})
                        
                        # Transform to common format
                        reply_data = {
                            "id": reply.get("id"),
                            "text": reply.get("text", ""),
                            "timestamp": reply.get("created_at"),
                            "author": {
                                "id": author_id,
                                "name": author.get("name"),
                                "username": author.get("username")
                            },
                            "type": "reply",
                            "tweet_id": tweet_id
                        }
                        collected_data.append(reply_data)
                        
                        # Publish to Kafka
                        publish_social_data(reply_data, "twitter")
            
            return len(collected_data) > 0
        
        except Exception as e:
            print(f"Error collecting data from Twitter: {e}")
            return False