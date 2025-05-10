import json
from typing import Dict, Any, List
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self):
        self.storage_path = "data/collected_data"
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        """Ensure the storage directory exists"""
        import os
        os.makedirs(self.storage_path, exist_ok=True)

    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process raw data before storage
        :param data: Raw data from platform
        :return: Processed data
        """
        processed_data = {
            'timestamp': datetime.now().isoformat(),
            'platform': data.get('platform'),
            'content': self._clean_content(data.get('content', {})),
            'metadata': self._extract_metadata(data.get('metadata', {}))
        }
        return processed_data

    def _clean_content(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Clean and normalize content data"""
        cleaned = {}
        for key, value in content.items():
            if isinstance(value, str):
                cleaned[key] = self._sanitize_string(value)
            else:
                cleaned[key] = value
        return cleaned

    def _sanitize_string(self, text: str) -> str:
        """Sanitize text content"""
        return text.encode('ascii', 'ignore').decode('ascii')

    def _extract_metadata(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Extract important metadata"""
        return {
            'user_id': metadata.get('user_id'),
            'post_id': metadata.get('post_id'),
            'timestamp': metadata.get('timestamp'),
            'engagement': {
                'likes': metadata.get('likes', 0),
                'comments': metadata.get('comments', 0),
                'shares': metadata.get('shares', 0)
            }
        }

    def store(self, data: Dict[str, Any]):
        """
        Store processed data
        :param data: Processed data to store
        """
        try:
            platform = data.get('platform', 'unknown')
            timestamp = data.get('timestamp', datetime.now().isoformat())
            
            # Create platform-specific directory
            platform_dir = f"{self.storage_path}/{platform}"
            import os
            os.makedirs(platform_dir, exist_ok=True)
            
            # Create date-based subdirectory
            date_str = datetime.fromisoformat(timestamp).strftime('%Y-%m-%d')
            date_dir = f"{platform_dir}/{date_str}"
            os.makedirs(date_dir, exist_ok=True)
            
            # Generate unique filename
            filename = f"{date_dir}/{timestamp.replace(':', '-')}.json"
            
            # Write data
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Stored data for platform {platform} at {filename}")
            
        except Exception as e:
            logger.error(f"Error storing data: {str(e)}")
