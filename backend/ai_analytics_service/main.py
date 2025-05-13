# FastAPI entrypoint for ai_analytics_service microservice
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from ai_analytics_service.models.sentiment_analysis import analyze_sentiment
from ai_analytics_service.models.ner import extract_entities
from ai_analytics_service.models.topic_classification import classify_topic
from ai_analytics_service.utils.kafka_consumer import KafkaTextConsumer
from ai_analytics_service.utils.elasticsearch_client import ElasticsearchClient
from ai_analytics_service.utils.neo4j_client import Neo4jClient
from .config import config # Import the global config instance
import datetime
import asyncio
import threading
import os
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("ai_analytics_service")

# Initialize FastAPI app
app = FastAPI(
    title="AI Analytics Microservice",
    description="Analyzes textual data using NLP and AI models to generate actionable insights",
    version="1.0.0"
)

# Pydantic models for API requests and responses
class TestRequest(BaseModel):
    text: str
    source: str = "unknown"
    language: Optional[str] = None

class Entity(BaseModel):
    type: str
    value: str

class SentimentResult(BaseModel):
    label: str
    confidence: float

class TestResponse(BaseModel):
    source: str
    text: str
    sentiment: SentimentResult
    entities: List[Entity]
    topic: str
    timestamp: str

class KafkaProcessingStatus(BaseModel):
    status: str
    topics: List[str]
    messages_processed: int

# Global variables for Kafka processing
kafka_processor = None
processing_status = {
    "status": "stopped",
    "topics": [],
    "messages_processed": 0
}

# Elasticsearch and Neo4j clients
es_client = ElasticsearchClient(
    hosts=config.ELASTICSEARCH_HOSTS.split(","),
    username=config.ELASTICSEARCH_USERNAME,
    password=config.ELASTICSEARCH_PASSWORD
)

neo4j_client = Neo4jClient(
    uri=config.NEO4J_URI,
    user=config.NEO4J_USER,
    password=config.NEO4J_PASSWORD
)

# Function to process a single message
def process_message(message: dict) -> dict:
    """Process a single message from Kafka
    
    Args:
        message: The message from Kafka
        
    Returns:
        Processed message with NLP analysis results
    """
    try:
        # Extract text and source from message
        text = message.get("text", "")
        source = message.get("source", "unknown")
        
        if not text:
            logger.warning(f"Received message without text from {source}")
            return None
            
        # Perform NLP analysis
        sentiment = analyze_sentiment(text)
        entities = extract_entities(text)
        topic = classify_topic(text)
        
        # Create processed message
        processed = {
            "source": source,
            "text": text,
            "sentiment": sentiment,
            "entities": entities,
            "topic": topic,
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "original_data": message  # Keep original data for reference
        }
        
        return processed
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        return None

# Function to start Kafka consumer in a separate thread
def start_kafka_consumer():
    """Start consuming messages from Kafka topics"""
    global kafka_processor, processing_status
    
    # Kafka topics to consume from
    topics = [config.KAFKA_RAW_SOCIAL_TOPIC, config.KAFKA_RAW_SCRAPED_TOPIC]
    
    try:
        # Initialize Kafka consumer
        kafka_consumer = KafkaTextConsumer(
            topics=topics,
            bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
            group_id=config.KAFKA_GROUP_ID
        )
        
        # Update processing status
        processing_status["status"] = "running"
        processing_status["topics"] = topics
        processing_status["messages_processed"] = 0
        
        logger.info(f"Started Kafka consumer for topics: {topics}")
        
        # Process messages
        for message in kafka_consumer.consume():
            try:
                # Process the message
                processed_message = process_message(message)
                
                if processed_message:
                    # Index to Elasticsearch
                    es_client.index_processed_data(config.PROCESSED_DATA_INDEX, processed_message)
                    
                    # Create entity graph in Neo4j
                    if processed_message["entities"]:
                        neo4j_client.create_entity_graph(processed_message["entities"])
                    
                    # Update processing status
                    processing_status["messages_processed"] += 1
                    
                    if processing_status["messages_processed"] % 100 == 0:
                        logger.info(f"Processed {processing_status['messages_processed']} messages")
            except Exception as e:
                logger.error(f"Error processing Kafka message: {e}")
    except Exception as e:
        logger.error(f"Error in Kafka consumer: {e}")
        processing_status["status"] = "error"
    finally:
        processing_status["status"] = "stopped"

# API endpoints
@app.get("/health")
def health():
    """Health check endpoint"""
    global processing_status
    return {
        "status": "ok",
        "kafka_processing": processing_status["status"],
        "messages_processed": processing_status["messages_processed"]
    }

@app.get("/models")
def list_models():
    """List available NLP models"""
    return {
        "sentiment": config.SENTIMENT_MODEL,
        "ner": config.NER_MODEL,
        "topic_classification": config.TOPIC_MODEL
    }

@app.post("/test", response_model=TestResponse)
def test_text(request: TestRequest):
    """Test endpoint to analyze a single text input"""
    try:
        sentiment = analyze_sentiment(request.text)
        entities = extract_entities(request.text)
        topic = classify_topic(request.text)
        timestamp = datetime.datetime.utcnow().isoformat() + "Z"
        
        response = {
            "source": request.source,
            "text": request.text,
            "sentiment": sentiment,
            "entities": entities,
            "topic": topic,
            "timestamp": timestamp
        }
        
        return response
    except Exception as e:
        logger.error(f"Error in test endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/start-processing")
def start_processing(background_tasks: BackgroundTasks):
    """Start processing messages from Kafka"""
    global kafka_processor, processing_status
    
    if processing_status["status"] == "running":
        return {"message": "Kafka processing is already running"}
    
    # Start Kafka consumer in a background thread
    kafka_thread = threading.Thread(target=start_kafka_consumer)
    kafka_thread.daemon = True
    kafka_thread.start()
    
    return {"message": "Started Kafka processing"}

@app.post("/stop-processing")
def stop_processing():
    """Stop processing messages from Kafka"""
    global processing_status
    
    if processing_status["status"] != "running":
        return {"message": "Kafka processing is not running"}
    
    # Set status to stopping to signal the consumer to stop
    processing_status["status"] = "stopping"
    
    return {"message": "Stopping Kafka processing"}

@app.get("/processing-status", response_model=KafkaProcessingStatus)
def get_processing_status():
    """Get the current status of Kafka processing"""
    global processing_status
    
    return {
        "status": processing_status["status"],
        "topics": processing_status["topics"],
        "messages_processed": processing_status["messages_processed"]
    }