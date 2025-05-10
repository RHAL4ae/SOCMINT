from kafka import KafkaProducer
import json
import os
from dotenv import load_dotenv

load_dotenv()

class SocialMediaKafkaProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=os.getenv('KAFKA_BOOTSTRAP_SERVER', 'kafka:9092'),
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda v: v.encode('utf-8')
        )
        
    def send_post(self, post_data: dict):
        """
        Send social media post data to Kafka topic
        """
        self.producer.send(
            topic='social_media_posts',
            key=post_data['post_id'],
            value=post_data
        )
        
    def send_media(self, media_data: dict):
        """
        Send media data to Kafka topic
        """
        self.producer.send(
            topic='social_media_media',
            key=media_data['media_id'],
            value=media_data
        )
        
    def send_analytics(self, analytics_data: dict):
        """
        Send analytics data to Kafka topic
        """
        self.producer.send(
            topic='social_media_analytics',
            key=analytics_data['analysis_id'],
            value=analytics_data
        )
        
    def close(self):
        """
        Close the Kafka producer connection
        """
        self.producer.close()

# Example usage
if __name__ == "__main__":
    producer = SocialMediaKafkaProducer()
    try:
        post_data = {
            'post_id': '123',
            'platform': 'twitter',
            'content': 'Sample post',
            'timestamp': '2025-05-10T12:00:00Z'
        }
        producer.send_post(post_data)
    finally:
        producer.close()
