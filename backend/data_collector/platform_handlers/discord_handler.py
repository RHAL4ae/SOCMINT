import asyncio
from typing import Dict, Any, Optional
import logging
from discord import Client, Intents
from discord.errors import LoginFailure

from .base_handler import BaseHandler

logger = logging.getLogger(__name__)

class DiscordHandler(BaseHandler):
    def __init__(self):
        super().__init__()
        self.collection_interval = 300  # 5 minutes for Discord
        self.client: Optional[Client] = None
        self._running = False

    async def collect_data(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Collect data from Discord
        :param config: Configuration containing bot token and channel IDs
        :return: Collected data
        """
        if not self.validate_config(config):
            return {}

        try:
            if not self.client:
                intents = Intents.default()
                intents.messages = True
                self.client = Client(intents=intents)

            # Start collecting in background
            if not self._running:
                self._running = True
                await self._start_collection(config)

            # Return recent data
            return self._process_response({
                'content': self._collected_data[-10:],  # Last 10 messages
                'metadata': {
                    'channel_id': config['channel_id'],
                    'timestamp': datetime.now().isoformat()
                }
            })

        except LoginFailure as e:
            logger.error(f"Discord login failed: {str(e)}")
            return {}

    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate Discord configuration
        :param config: Configuration to validate
        :return: True if valid, False otherwise
        """
        required_fields = ['bot_token', 'channel_id']
        return all(field in config for field in required_fields)

    async def _start_collection(self, config: Dict[str, Any]):
        """Start background collection"""
        @self.client.event
        async def on_ready():
            logger.info(f"Logged in as {self.client.user.name}")
            self._collected_data = []

        @self.client.event
        async def on_message(message):
            if message.channel.id == config['channel_id']:
                self._collected_data.append({
                    'content': message.content,
                    'author': message.author.name,
                    'timestamp': message.created_at.isoformat(),
                    'attachments': [a.url for a in message.attachments]
                })

        try:
            await self.client.start(config['bot_token'])
        except Exception as e:
            logger.error(f"Error in Discord collection: {str(e)}")
            self._running = False

    def stop_collection(self):
        """Stop collection and cleanup"""
        if self.client:
            asyncio.run(self.client.close())
        self._running = False
