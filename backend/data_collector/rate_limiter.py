import asyncio
from typing import Dict, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class RateLimiter:
    def __init__(self):
        self.limits: Dict[str, Dict[str, Any]] = {}
        self.lock = asyncio.Lock()

    def set_limit(self, platform: str, limit: int, interval: int):
        """
        Set rate limit for a platform
        :param platform: Platform name
        :param limit: Number of requests allowed
        :param interval: Time interval in seconds
        """
        with self.lock:
            self.limits[platform] = {
                'limit': limit,
                'interval': interval,
                'count': 0,
                'reset_time': datetime.now()
            }

    async def wait(self, platform: str):
        """
        Wait if necessary to respect rate limits
        :param platform: Platform name
        """
        async with self.lock:
            if platform not in self.limits:
                return

            limit_data = self.limits[platform]
            
            # Check if we need to reset the counter
            if datetime.now() > limit_data['reset_time']:
                limit_data['count'] = 0
                limit_data['reset_time'] = datetime.now() + timedelta(seconds=limit_data['interval'])

            # If we've reached the limit, wait
            if limit_data['count'] >= limit_data['limit']:
                wait_time = (limit_data['reset_time'] - datetime.now()).total_seconds()
                logger.info(f"Waiting {wait_time:.2f} seconds for {platform} rate limit")
                await asyncio.sleep(wait_time)
                limit_data['count'] = 0

            limit_data['count'] += 1
