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

    def validate_configs(self) -> None:
        """
        Validate all platform configurations.
        Raises ValueError if any critical configuration is missing.
        """
        missing_configs = {}
        for platform, config_items in self.platform_configs.items():
            # Consider all defined keys as potentially critical. Adjust if some are truly optional.
            # For now, any empty value for a defined key is treated as missing.
            missing_keys = [k for k, v in config_items.items() if not v and v is not False] # Ensure boolean False is not treated as missing
            if missing_keys:
                missing_configs[platform] = missing_keys
        
        if missing_configs:
            error_message = "Critical configurations missing, service cannot start:\n"
            for platform, keys in missing_configs.items():
                error_message += f"  Platform '{platform}': {', '.join(keys)}\n"
            logger.error(error_message)
            raise ValueError(error_message)
        logger.info("All platform configurations validated successfully.")
