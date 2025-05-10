from typing import Dict, Any, Optional
import logging
from telegram import Bot
from telegram.error import TelegramError

from .base_handler import BaseHandler

logger = logging.getLogger(__name__)

class TelegramHandler(BaseHandler):
    def __init__(self):
        super().__init__()
        self.collection_interval = 60  # 1 minute for Telegram
        self.bot: Optional[Bot] = None

    async def collect_data(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Collect data from Telegram
        :param config: Configuration containing bot token and chat IDs
        :return: Collected data
        """
        if not self.validate_config(config):
            return {}

        try:
            if not self.bot:
                self.bot = Bot(token=config['bot_token'])

            chat_id = config['chat_id']
            messages = await self._get_messages(chat_id)
            
            return self._process_response({
                'content': messages,
                'metadata': {
                    'chat_id': chat_id,
                    'timestamp': datetime.now().isoformat()
                }
            })

        except TelegramError as e:
            logger.error(f"Telegram error: {str(e)}")
            return {}

    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate Telegram configuration
        :param config: Configuration to validate
        :return: True if valid, False otherwise
        """
        required_fields = ['bot_token', 'chat_id']
        return all(field in config for field in required_fields)

    async def _get_messages(self, chat_id: str) -> List[Dict[str, Any]]:
        """
        Get messages from a chat
        :param chat_id: Chat ID to get messages from
        :return: List of messages
        """
        try:
            messages = []
            offset = None
            
            while True:
                updates = await self.bot.get_updates(
                    offset=offset,
                    timeout=30,
                    allowed_updates=['message']
                )
                
                if not updates:
                    break
                
                for update in updates:
                    if update.message and update.message.chat_id == chat_id:
                        messages.append({
                            'text': update.message.text,
                            'user_id': update.message.from_user.id,
                            'timestamp': update.message.date.isoformat()
                        })
                
                offset = updates[-1].update_id + 1 if updates else None
                
                if not offset:
                    break
            
            return messages
            
        except Exception as e:
            logger.error(f"Error getting messages: {str(e)}")
            return []
