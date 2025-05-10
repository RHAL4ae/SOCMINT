import asyncio
from typing import Dict, Any, Optional
import logging
import random
import time

from playwright.async_api import async_playwright

from .base_handler import BaseHandler

logger = logging.getLogger(__name__)

class TikTokHandler(BaseHandler):
    def __init__(self):
        super().__init__()
        self.collection_interval = 3600  # 1 hour for TikTok
        self._playwright = None
        self._browser = None
        self._page = None

    async def collect_data(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Collect data from TikTok
        :param config: Configuration containing target user/hashtag
        :return: Collected data
        """
        if not self.validate_config(config):
            return {}

        try:
            if not self._playwright:
                self._playwright = await async_playwright().start()
                self._browser = await self._playwright.chromium.launch(
                    headless=True,
                    args=['--no-sandbox', '--disable-setuid-sandbox']
                )
                self._page = await self._browser.new_page()

            # Set random user agent
            await self._set_random_user_agent()

            # Navigate to target
            target = config['target']
            url = f"https://www.tiktok.com/@{target}" if target.startswith('@') else f"https://www.tiktok.com/tag/{target}"
            await self._page.goto(url)

            # Wait for content to load
            await asyncio.sleep(5)

            # Scroll and collect data
            await self._scroll_and_collect()

            # Process collected data
            return self._process_response({
                'content': self._collected_data,
                'metadata': {
                    'target': target,
                    'timestamp': datetime.now().isoformat()
                }
            })

        except Exception as e:
            logger.error(f"Error collecting TikTok data: {str(e)}")
            return {}

    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate TikTok configuration
        :param config: Configuration to validate
        :return: True if valid, False otherwise
        """
        return 'target' in config

    async def _set_random_user_agent(self):
        """Set a random user agent"""
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
        ]
        await self._page.set_extra_http_headers({
            'User-Agent': random.choice(user_agents)
        })

    async def _scroll_and_collect(self):
        """Scroll through content and collect data"""
        self._collected_data = []
        
        # Scroll 5 times
        for _ in range(5):
            # Scroll down
            await self._page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await asyncio.sleep(2)
            
            # Collect visible posts
            posts = await self._page.query_selector_all('.tiktok-post')
            for post in posts:
                try:
                    video_url = await post.query_selector('video').get_attribute('src')
                    likes = await post.query_selector('.likes').inner_text()
                    comments = await post.query_selector('.comments').inner_text()
                    
                    self._collected_data.append({
                        'video_url': video_url,
                        'likes': likes,
                        'comments': comments,
                        'timestamp': datetime.now().isoformat()
                    })
                except:
                    continue
