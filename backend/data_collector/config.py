import os
from typing import Dict, Any
from dotenv import load_dotenv
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class Config:
    def __init__(self):
        self.platform_configs = {
            'telegram': {
                'bot_token': os.getenv('TELEGRAM_BOT_TOKEN'),
                'chat_id': os.getenv('TELEGRAM_CHAT_ID')
            },
            'tiktok': {
                'target': os.getenv('TIKTOK_TARGET', '@default_target')
            },
            'discord': {
                'bot_token': os.getenv('DISCORD_BOT_TOKEN'),
                'channel_id': os.getenv('DISCORD_CHANNEL_ID')
            },
            'reddit': {
                'client_id': os.getenv('REDDIT_CLIENT_ID'),
                'client_secret': os.getenv('REDDIT_CLIENT_SECRET'),
                'user_agent': os.getenv('REDDIT_USER_AGENT', 'socmint_data_collector'),
                'subreddit': os.getenv('REDDIT_SUBREDDIT', 'default_subreddit')
            },
            'clubhouse': {
                'api_token': os.getenv('CLUBHOUSE_API_TOKEN'),
                'channels': os.getenv('CLUBHOUSE_CHANNELS', '').split(',')
            }
        }

    def get_config(self, platform: str) -> Dict[str, Any]:
        """
        Get configuration for a specific platform
        :param platform: Platform name
        :return: Platform configuration
        """
        return self.platform_configs.get(platform, {})

    def validate_configs(self) -> bool:
        """
        Validate all platform configurations
        :return: True if all configurations are valid
        """
        valid = True
        for platform, config in self.platform_configs.items():
            missing = [k for k, v in config.items() if not v]
            if missing:
                logger.warning(f"Missing configuration for {platform}: {missing}")
                valid = False
        return valid
