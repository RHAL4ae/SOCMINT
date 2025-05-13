import os
from dotenv import load_dotenv
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

class SocialMediaManagerConfig:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL") # Example: postgresql://user:pass@host:port/db
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = os.getenv("ALGORITHM", "HS256")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
        self.FRONTEND_URL = os.getenv("FRONTEND_URL", "*")
        # Add other service-specific configurations here
        # e.g., API keys for social media platforms if managed directly by this service

        self.critical_configs = {
            'DATABASE_URL': self.DATABASE_URL,
            'SECRET_KEY': self.SECRET_KEY,
            # Add other critical variables here
        }

    def validate_configs(self) -> None:
        """
        Validate critical configurations.
        Raises ValueError if any critical configuration is missing.
        """
        missing = [key for key, value in self.critical_configs.items() if not value]
        if missing:
            error_message = f"Critical configurations missing for Social Media Manager: {', '.join(missing)}. Service cannot start."
            logger.error(error_message)
            raise ValueError(error_message)
        logger.info("Social Media Manager configurations validated successfully.")

# Global config instance
config = SocialMediaManagerConfig()
config.validate_configs() # Validate on import