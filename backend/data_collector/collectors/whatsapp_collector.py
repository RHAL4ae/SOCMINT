import os
import requests
from typing import Dict, Any, List, Optional
from datetime import datetime
from dotenv import load_dotenv

# Import utility functions
from utils.helpers import publish_social_data

class WhatsAppCollector:
    """WhatsApp API data collector
    
    Note: This is a simplified implementation. WhatsApp Business API access
    requires approval from WhatsApp and has strict usage policies.
    """
    
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # WhatsApp API credentials
        self.api_key = os.getenv("WHATSAPP_API_KEY")
        self.phone_number_id = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
        self.business_account_id = os.getenv("WHATSAPP_BUSINESS_ACCOUNT_ID")
        
        # WhatsApp API base URL (using Facebook Graph API for WhatsApp Business)
        self.api_base_url = "https://graph.facebook.com/v18.0"
        
        # Check if credentials are available
        self.is_configured = all([self.api_key, self.phone_number_id, self.business_account_id])
    
    def check_connection(self) -> bool:
        """Check if WhatsApp API connection is available"""
        if not self.is_configured:
            return False
        
        try:
            # Try to make a simple API call to check connection
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            response = requests.get(
                f"{self.api_base_url}/{self.business_account_id}",
                headers=headers
            )
            return response.status_code == 200
        except Exception:
            return False
    
    async def collect(self, query_params: Dict[str, Any]) -> bool:
        """Collect data from WhatsApp based on query parameters"""
        if not self.is_configured:
            print("WhatsApp collector not configured properly")
            return False
        
        # Extract parameters
        phone_number = query_params.get("phone_number")
        message_id = query_params.get("message_id")
        limit = query_params.get("limit", 25)
        
        collected_data = []
        
        try:
            # Note: WhatsApp Business API doesn't allow retrieving message history
            # without explicit user opt-in and has strict usage policies.
            # This is a simplified implementation for demonstration purposes.
            
            # In a real implementation, you would typically:
            # 1. Set up a webhook to receive incoming messages
            # 2. Store messages in your own database
            # 3. Retrieve messages from your database
            
            # For this example, we'll simulate retrieving messages
            if phone_number:
                print(f"Retrieving messages for {phone_number} (simulated)")
                
                # Simulate retrieved messages
                simulated_messages = [
                    {
                        "id": f"wamid.{i}",
                        "from": phone_number,
                        "timestamp": datetime.now().isoformat(),
                        "text": {
                            "body": f"Simulated message {i}"
                        },
                        "type": "text"
                    } for i in range(1, min(limit + 1, 6))
                ]
                
                for message in simulated_messages:
                    # Transform to common format
                    message_data = {
                        "id": message.get("id"),
                        "text": message.get("text", {}).get("body", ""),
                        "timestamp": message.get("timestamp"),
                        "author": {
                            "phone_number": message.get("from")
                        },
                        "type": "message"
                    }
                    collected_data.append(message_data)
                    
                    # Publish to Kafka
                    publish_social_data(message_data, "whatsapp")
            
            # Get specific message by ID
            if message_id:
                print(f"Retrieving message {message_id} (simulated)")
                
                # Simulate retrieved message
                simulated_message = {
                    "id": message_id,
                    "from": "1234567890",
                    "timestamp": datetime.now().isoformat(),
                    "text": {
                        "body": "Simulated specific message"
                    },
                    "type": "text"
                }
                
                # Transform to common format
                message_data = {
                    "id": simulated_message.get("id"),
                    "text": simulated_message.get("text", {}).get("body", ""),
                    "timestamp": simulated_message.get("timestamp"),
                    "author": {
                        "phone_number": simulated_message.get("from")
                    },
                    "type": "message"
                }
                collected_data.append(message_data)
                
                # Publish to Kafka
                publish_social_data(message_data, "whatsapp")
            
            return len(collected_data) > 0
        
        except Exception as e:
            print(f"Error collecting data from WhatsApp: {e}")
            return False