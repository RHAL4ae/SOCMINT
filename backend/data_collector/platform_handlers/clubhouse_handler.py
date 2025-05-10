import asyncio
from typing import Dict, Any, Optional
import logging
import json
import aiohttp

from .base_handler import BaseHandler

logger = logging.getLogger(__name__)

class ClubhouseHandler(BaseHandler):
    def __init__(self):
        super().__init__()
        self.collection_interval = 1800  # 30 minutes for Clubhouse
        self.api_url = "https://www.clubhouseapi.com/api"
        self.headers = {
            'CH-API-VERSION': '5',
            'CH-API-CLIENT': '1.0.16',
            'CH-API-PLATFORM': 'android',
            'CH-API-DEVICE': 'Pixel 3a'
        }

    async def collect_data(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Collect data from Clubhouse
        :param config: Configuration containing API token and channels
        :return: Collected data
        """
        if not self.validate_config(config):
            return {}

        try:
            async with aiohttp.ClientSession() as session:
                # Get active rooms
                rooms = await self._get_active_rooms(session)
                
                # Get room details
                room_details = await self._get_room_details(session, rooms)
                
                return self._process_response({
                    'content': room_details,
                    'metadata': {
                        'timestamp': datetime.now().isoformat()
                    }
                })

        except Exception as e:
            logger.error(f"Error collecting Clubhouse data: {str(e)}")
            return {}

    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate Clubhouse configuration
        :param config: Configuration to validate
        :return: True if valid, False otherwise
        """
        required_fields = ['api_token', 'channels']
        return all(field in config for field in required_fields)

    async def _get_active_rooms(self, session: aiohttp.ClientSession) -> List[Dict[str, Any]]:
        """
        Get list of active rooms
        :param session: aiohttp session
        :return: List of active rooms
        """
        try:
            url = f"{self.api_url}/get_active_rooms"
            async with session.get(url, headers=self.headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('rooms', [])
                return []
        except Exception as e:
            logger.error(f"Error getting active rooms: {str(e)}")
            return []

    async def _get_room_details(self, session: aiohttp.ClientSession, rooms: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Get detailed information about rooms
        :param session: aiohttp session
        :param rooms: List of rooms
        :return: List of room details
        """
        room_details = []
        for room in rooms:
            try:
                url = f"{self.api_url}/get_room_info"
                params = {
                    'room_id': room['room_id'],
                    'user_id': room['user_id']
                }
                
                async with session.get(url, headers=self.headers, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        room_details.append({
                            'title': data.get('title'),
                            'speakers': data.get('speakers', []),
                            'listeners': data.get('listeners', []),
                            'started_at': data.get('started_at'),
                            'ended_at': data.get('ended_at')
                        })
            except Exception as e:
                logger.error(f"Error getting room details: {str(e)}")
                continue
        
        return room_details
