import asyncio
from typing import Dict, Any, Optional
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class BaseHandler(ABC):
    def __init__(self):
        self.collection_interval = 300  # Default 5 minutes
        self._ensure_config()

    @abstractmethod
    async def collect_data(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Collect data from the platform
        :param config: Platform-specific configuration
        :return: Collected data
        """
        pass

    def _ensure_config(self):
        """Ensure required configuration is present"""
        if not hasattr(self, 'config'):
            raise ValueError("Configuration must be set before collecting data")

    @abstractmethod
    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate platform-specific configuration
        :param config: Configuration to validate
        :return: True if valid, False otherwise
        """
        pass

    async def _make_request(self, url: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Make an HTTP request to the platform
        :param url: URL to request
        :param headers: Optional headers
        :return: Response data
        """
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Request failed with status {response.status}")
                        return {}
        except Exception as e:
            logger.error(f"Error making request: {str(e)}")
            return {}

    def _process_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process platform response
        :param response: Raw response data
        :return: Processed data
        """
        return {
            'platform': self.__class__.__name__.replace('Handler', ''),
            'content': response.get('content', {}),
            'metadata': response.get('metadata', {})
        }
