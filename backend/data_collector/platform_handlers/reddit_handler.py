import asyncio
from typing import Dict, Any, Optional
import logging
from praw import Reddit
from praw.exceptions import RedditAPIException

from .base_handler import BaseHandler

logger = logging.getLogger(__name__)

class RedditHandler(BaseHandler):
    def __init__(self):
        super().__init__()
        self.collection_interval = 900  # 15 minutes for Reddit
        self.reddit: Optional[Reddit] = None

    async def collect_data(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Collect data from Reddit
        :param config: Configuration containing API credentials and subreddit
        :return: Collected data
        """
        if not self.validate_config(config):
            return {}

        try:
            if not self.reddit:
                self.reddit = Reddit(
                    client_id=config['client_id'],
                    client_secret=config['client_secret'],
                    user_agent=config['user_agent']
                )

            subreddit = config['subreddit']
            posts = await self._get_posts(subreddit)
            
            return self._process_response({
                'content': posts,
                'metadata': {
                    'subreddit': subreddit,
                    'timestamp': datetime.now().isoformat()
                }
            })

        except RedditAPIException as e:
            logger.error(f"Reddit API error: {str(e)}")
            return {}

    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate Reddit configuration
        :param config: Configuration to validate
        :return: True if valid, False otherwise
        """
        required_fields = ['client_id', 'client_secret', 'user_agent', 'subreddit']
        return all(field in config for field in required_fields)

    async def _get_posts(self, subreddit: str) -> List[Dict[str, Any]]:
        """
        Get posts from a subreddit
        :param subreddit: Subreddit name
        :return: List of posts
        """
        try:
            posts = []
            sub = await self.reddit.subreddit(subreddit)
            
            # Get top posts
            async for submission in sub.top('day', limit=10):
                posts.append({
                    'title': submission.title,
                    'url': submission.url,
                    'author': submission.author.name if submission.author else None,
                    'score': submission.score,
                    'num_comments': submission.num_comments,
                    'created_utc': submission.created_utc,
                    'selftext': submission.selftext
                })
            
            return posts
            
        except Exception as e:
            logger.error(f"Error getting Reddit posts: {str(e)}")
            return []
