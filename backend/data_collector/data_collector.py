import asyncio
from typing import Dict, Any, Optional
from datetime import datetime
import logging
from queue import Queue
import threading

from .platform_handlers import PlatformHandler
from .rate_limiter import RateLimiter
from .data_processor import DataProcessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataCollector:
    def __init__(self):
        self.platform_handlers: Dict[str, PlatformHandler] = {}
        self.rate_limiter = RateLimiter()
        self.data_processor = DataProcessor()
        self.task_queue = Queue()
        self.running = False

    def register_platform(self, platform_name: str, handler: PlatformHandler):
        """Register a new platform handler"""
        self.platform_handlers[platform_name] = handler

    async def start_collection(self, platform_name: str, config: Dict[str, Any]):
        """Start data collection for a specific platform"""
        if platform_name not in self.platform_handlers:
            raise ValueError(f"Platform {platform_name} not registered")

        handler = self.platform_handlers[platform_name]
        
        while self.running:
            try:
                # Apply rate limiting
                await self.rate_limiter.wait(platform_name)
                
                # Collect data
                data = await handler.collect_data(config)
                
                if data:
                    # Process and store data
                    processed_data = self.data_processor.process(data)
                    self.data_processor.store(processed_data)
                    
                await asyncio.sleep(handler.collection_interval)
                
            except Exception as e:
                logger.error(f"Error collecting data from {platform_name}: {str(e)}")
                await asyncio.sleep(60)  # Wait before retrying

    def start(self):
        """Start the data collection system"""
        self.running = True
        logger.info("Starting data collection system")

    def stop(self):
        """Stop the data collection system"""
        self.running = False
        logger.info("Stopping data collection system")

    def add_task(self, task: Dict[str, Any]):
        """Add a new collection task to the queue"""
        self.task_queue.put(task)

    def process_tasks(self):
        """Process tasks from the queue"""
        while self.running:
            try:
                task = self.task_queue.get()
                platform_name = task.get('platform')
                config = task.get('config')
                
                if platform_name and config:
                    asyncio.run(self.start_collection(platform_name, config))
                
            except Exception as e:
                logger.error(f"Error processing task: {str(e)}")
                continue
