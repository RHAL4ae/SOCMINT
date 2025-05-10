# Kafka consumer utility for ai_analytics_service
from kafka import KafkaConsumer
import json
from typing import Iterator

class KafkaTextConsumer:
    def __init__(self, topics, bootstrap_servers='localhost:9092', group_id='ai_analytics_group'):
        self.consumer = KafkaConsumer(
            *topics,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True
        )

    def consume(self) -> Iterator[dict]:
        for message in self.consumer:
            yield message.value