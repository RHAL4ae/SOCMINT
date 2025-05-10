import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

load_dotenv()

class OAuthHandler:
    def __init__(self):
        self.clients = {}
        self.load_credentials()

    def load_credentials(self):
        """Load OAuth credentials from environment variables"""
        platforms = ["twitter", "facebook", "linkedin"]
        for platform in platforms:
            client_id = os.getenv(f"{platform.upper()}_CLIENT_ID")
            client_secret = os.getenv(f"{platform.upper()}_CLIENT_SECRET")
            if client_id and client_secret:
                self.clients[platform] = {
                    "client_id": client_id,
                    "client_secret": client_secret
                }

    def get_oauth_session(self, platform: str):
        """Get OAuth session for a platform"""
        if platform not in self.clients:
            raise ValueError(f"Unsupported platform: {platform}")
        
        client = BackendApplicationClient(client_id=self.clients[platform]["client_id"])
        oauth = OAuth2Session(client=client)
        return oauth

    def refresh_token(self, platform: str, refresh_token: str):
        """Refresh OAuth token for a platform"""
        if platform not in self.clients:
            raise ValueError(f"Unsupported platform: {platform}")
        
        oauth = self.get_oauth_session(platform)
        token = oauth.refresh_token(
            token_url=f"https://api.{platform}.com/oauth2/token",
            refresh_token=refresh_token,
            client_id=self.clients[platform]["client_id"],
            client_secret=self.clients[platform]["client_secret"]
        )
        return token["access_token"]
