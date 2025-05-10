import os
import json
import time
from datetime import datetime
from typing import Dict, Any, List, Optional
from kafka import KafkaProducer
from kafka.errors import KafkaError
import requests
import socks
import socket
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Kafka configuration
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
SOCIAL_TOPIC = "raw_social_data"
SCRAPED_TOPIC = "raw_scraped_data"

# TOR configuration
TOR_PROXY = os.getenv("TOR_PROXY", "socks5h://localhost:9050")

# Initialize Kafka producer with retry logic
def get_kafka_producer():
    """Get a Kafka producer with retry logic"""
    max_retries = 5
    retry_interval = 2  # seconds
    
    for attempt in range(max_retries):
        try:
            producer = KafkaProducer(
                bootstrap_servers=[KAFKA_BROKER],
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                acks='all',
                retries=3,
                retry_backoff_ms=500
            )
            return producer
        except KafkaError as e:
            if attempt < max_retries - 1:
                time.sleep(retry_interval)
                retry_interval *= 2  # Exponential backoff
            else:
                raise e

# Check Kafka connection
def check_kafka_connection() -> bool:
    """Check if Kafka connection is available"""
    try:
        producer = get_kafka_producer()
        producer.close()
        return True
    except Exception:
        return False

# Check TOR connection
def check_tor_connection() -> bool:
    """Check if TOR connection is available"""
    try:
        # Parse TOR proxy string
        proxy_parts = TOR_PROXY.split('://')
        proxy_type = proxy_parts[0]
        proxy_addr = proxy_parts[1]
        
        # Set up socket with SOCKS proxy
        if proxy_type == 'socks5h':
            socks_type = socks.SOCKS5
        elif proxy_type == 'socks4':
            socks_type = socks.SOCKS4
        else:
            return False
        
        # Split host and port
        host, port_str = proxy_addr.split(':')
        port = int(port_str)
        
        # Create a socket through the SOCKS proxy
        s = socks.socksocket()
        s.set_proxy(socks_type, host, port)
        
        # Try to connect to a .onion site (DuckDuckGo's onion)
        s.connect(("3g2upl4pq6kufc4m.onion", 80))
        s.close()
        return True
    except Exception:
        return False

# Publish to Kafka
def publish_to_kafka(data: Dict[str, Any], topic: str) -> bool:
    """Publish data to Kafka topic with retry logic"""
    try:
        producer = get_kafka_producer()
        future = producer.send(topic, value=data)
        # Block until the message is sent (or timeout)
        record_metadata = future.get(timeout=10)
        producer.close()
        return True
    except Exception as e:
        print(f"Error publishing to Kafka: {e}")
        return False

# Normalize social media data
def normalize_social_data(data: Dict[str, Any], source: str) -> Dict[str, Any]:
    """Normalize social media data to a common format"""
    normalized = {
        "text": data.get("text", data.get("content", data.get("message", ""))),
        "author": data.get("author", data.get("user", data.get("from", {}))),
        "timestamp": data.get("timestamp", data.get("created_at", data.get("date", datetime.now().isoformat()))),
        "source": source,
        "original_data": data,
        "collected_at": datetime.now().isoformat()
    }
    return normalized

# Normalize scraped data
def normalize_scraped_data(data: Dict[str, Any], url: str, is_darkweb: bool = False) -> Dict[str, Any]:
    """Normalize scraped data to a common format"""
    normalized = {
        "url": url,
        "title": data.get("title", ""),
        "content": data.get("content", ""),
        "is_darkweb": is_darkweb,
        "original_data": data,
        "scraped_at": datetime.now().isoformat()
    }
    return normalized

# Publish social media data
def publish_social_data(data: Dict[str, Any], source: str) -> bool:
    """Normalize and publish social media data to Kafka"""
    normalized_data = normalize_social_data(data, source)
    return publish_to_kafka(normalized_data, SOCIAL_TOPIC)

# Publish scraped data
def publish_scraped_data(data: Dict[str, Any], url: str, is_darkweb: bool = False) -> bool:
    """Normalize and publish scraped data to Kafka"""
    normalized_data = normalize_scraped_data(data, url, is_darkweb)
    return publish_to_kafka(normalized_data, SCRAPED_TOPIC)