from elasticsearch import Elasticsearch
from typing import List, Dict
import os

def fetch_logs(query: dict) -> List[Dict]:
    """
    Fetch logs from Elasticsearch index 'security_logs' using the provided query.
    """
    es = Elasticsearch(os.getenv("ELASTICSEARCH_URL", "http://localhost:9200"))
    resp = es.search(index="security_logs", body=query)
    logs = [hit["_source"] for hit in resp["hits"]["hits"]]
    return logs