import os
from dotenv import load_dotenv
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

class AIAnalyticsConfig:
    def __init__(self):
        self.ELASTICSEARCH_HOSTS = os.getenv("ELASTICSEARCH_HOSTS", "http://elasticsearch:9200")
        self.ELASTICSEARCH_USERNAME = os.getenv("ELASTICSEARCH_USERNAME")
        self.ELASTICSEARCH_PASSWORD = os.getenv("ELASTICSEARCH_PASSWORD")
        self.NEO4J_URI = os.getenv("NEO4J_URI", "bolt://neo4j:7687") # Updated default to use service name
        self.NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
        self.NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
        self.KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092") # Updated default
        self.KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "ai_analytics_group")
        self.SENTIMENT_MODEL = os.getenv("SENTIMENT_MODEL", "asafaya/bert-base-arabic-sentiment")
        self.NER_MODEL = os.getenv("NER_MODEL", "aubmindlab/bert-base-arabertv02-ner")
        self.TOPIC_MODEL = os.getenv("TOPIC_MODEL", "facebook/bart-large-mnli")
        self.KAFKA_RAW_SOCIAL_TOPIC = os.getenv("KAFKA_RAW_SOCIAL_TOPIC", "raw_social_data")
        self.KAFKA_RAW_SCRAPED_TOPIC = os.getenv("KAFKA_RAW_SCRAPED_TOPIC", "raw_scraped_data")
        self.PROCESSED_DATA_INDEX = os.getenv("PROCESSED_DATA_INDEX", "processed_data")

        self.critical_configs = {
            'ELASTICSEARCH_HOSTS': self.ELASTICSEARCH_HOSTS,
            'NEO4J_URI': self.NEO4J_URI,
            'KAFKA_BOOTSTRAP_SERVERS': self.KAFKA_BOOTSTRAP_SERVERS,
            # Add other truly critical variables here if they must be present for startup
            # For example, if ELASTICSEARCH_PASSWORD is required when USERNAME is set:
            # 'ELASTICSEARCH_PASSWORD': self.ELASTICSEARCH_PASSWORD if self.ELASTICSEARCH_USERNAME else True 
        }

    def validate_configs(self) -> None:
        """
        Validate critical configurations.
        Raises ValueError if any critical configuration is missing.
        """
        missing = []
        for key, value in self.critical_configs.items():
            if not value:
                # Special handling for password if username is present
                if key == 'ELASTICSEARCH_PASSWORD' and self.ELASTICSEARCH_USERNAME and not self.ELASTICSEARCH_PASSWORD:
                    missing.append(key)
                elif key != 'ELASTICSEARCH_PASSWORD': # Avoid double-adding or if it's optional without username
                    missing.append(key)
                
        if missing:
            error_message = f"Critical configurations missing for AI Analytics Service: {', '.join(missing)}. Service cannot start."
            logger.error(error_message)
            raise ValueError(error_message)
        logger.info("AI Analytics Service configurations validated successfully.")

# Global config instance
config = AIAnalyticsConfig()
config.validate_configs() # Validate on import