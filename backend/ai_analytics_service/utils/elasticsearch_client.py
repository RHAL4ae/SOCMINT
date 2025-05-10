# Elasticsearch client utility for ai_analytics_service
from elasticsearch import Elasticsearch
import os

class ElasticsearchClient:
    def __init__(self, hosts=None, username=None, password=None):
        self.hosts = hosts or os.getenv("ELASTICSEARCH_HOSTS", "localhost:9200").split(",")
        self.username = username or os.getenv("ELASTICSEARCH_USERNAME", None)
        self.password = password or os.getenv("ELASTICSEARCH_PASSWORD", None)
        self.client = Elasticsearch(
            self.hosts,
            basic_auth=(self.username, self.password) if self.username and self.password else None,
            verify_certs=False
        )

    def index_processed_data(self, index: str, doc: dict):
        return self.client.index(index=index, document=doc)