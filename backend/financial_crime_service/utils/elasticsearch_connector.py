import os
from elasticsearch import Elasticsearch
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ElasticsearchConnector:
    """
    Connector for Elasticsearch operations related to financial crime detection.
    Handles indexing and searching financial data for analysis.
    """
    def __init__(self):
        es_host = os.getenv('ELASTICSEARCH_HOST', 'localhost')
        es_port = os.getenv('ELASTICSEARCH_PORT', '9200')
        es_user = os.getenv('ELASTICSEARCH_USER', '')
        es_password = os.getenv('ELASTICSEARCH_PASSWORD', '')
        
        # Configure Elasticsearch client
        if es_user and es_password:
            self.es = Elasticsearch(
                [f'http://{es_host}:{es_port}'],
                http_auth=(es_user, es_password)
            )
        else:
            self.es = Elasticsearch([f'http://{es_host}:{es_port}'])
        
        # Initialize indices
        self._init_indices()
    
    def _init_indices(self):
        """Initialize Elasticsearch indices if they don't exist"""
        # Financial transactions index
        if not self.es.indices.exists(index='financial_transactions'):
            self.es.indices.create(
                index='financial_transactions',
                body={
                    'mappings': {
                        'properties': {
                            'tenant_id': {'type': 'keyword'},
                            'entity_id': {'type': 'keyword'},
                            'transaction_id': {'type': 'keyword'},
                            'amount': {'type': 'float'},
                            'currency': {'type': 'keyword'},
                            'timestamp': {'type': 'date'},
                            'source_account': {'type': 'keyword'},
                            'destination_account': {'type': 'keyword'},
                            'transaction_type': {'type': 'keyword'},
                            'risk_score': {'type': 'float'},
                            'is_suspicious': {'type': 'boolean'}
                        }
                    }
                }
            )
        
        # Financial entities index
        if not self.es.indices.exists(index='financial_entities'):
            self.es.indices.create(
                index='financial_entities',
                body={
                    'mappings': {
                        'properties': {
                            'tenant_id': {'type': 'keyword'},
                            'entity_id': {'type': 'keyword'},
                            'entity_type': {'type': 'keyword'},  # Person, Company, Account
                            'name': {'type': 'text'},
                            'account_number': {'type': 'keyword'},
                            'registration_date': {'type': 'date'},
                            'risk_score': {'type': 'float'},
                            'is_suspicious': {'type': 'boolean'},
                            'cluster_id': {'type': 'integer'}
                        }
                    }
                }
            )
    
    def index_transaction(self, transaction_data):
        """Index a financial transaction in Elasticsearch"""
        # Ensure transaction has a timestamp
        if 'timestamp' not in transaction_data:
            transaction_data['timestamp'] = datetime.now().isoformat()
        
        # Generate ID if not provided
        doc_id = transaction_data.get('transaction_id', None)
        
        result = self.es.index(
            index='financial_transactions',
            id=doc_id,
            body=transaction_data
        )
        
        return result
    
    def index_entity(self, entity_data):
        """Index a financial entity in Elasticsearch"""
        # Generate ID if not provided
        doc_id = entity_data.get('entity_id', None)
        
        result = self.es.index(
            index='financial_entities',
            id=doc_id,
            body=entity_data
        )
        
        return result
    
    def update_entity_risk(self, entity_id, risk_score, is_suspicious=False, cluster_id=None):
        """Update risk information for an entity"""
        update_body = {
            'doc': {
                'risk_score': risk_score,
                'is_suspicious': is_suspicious
            }
        }
        
        if cluster_id is not None:
            update_body['doc']['cluster_id'] = cluster_id
        
        result = self.es.update(
            index='financial_entities',
            id=entity_id,
            body=update_body
        )
        
        return result
    
    def search_suspicious_entities(self, tenant_id=None, min_risk_score=0.7, size=100):
        """Search for suspicious entities based on risk score"""
        query = {
            'bool': {
                'must': [
                    {'range': {'risk_score': {'gte': min_risk_score}}}
                ]
            }
        }
        
        if tenant_id:
            query['bool']['must'].append({'term': {'tenant_id': tenant_id}})
        
        result = self.es.search(
            index='financial_entities',
            body={
                'query': query,
                'size': size,
                'sort': [{'risk_score': {'order': 'desc'}}]
            }
        )
        
        return result['hits']['hits']
    
    def search_transactions_by_entity(self, entity_id, size=100):
        """Search for transactions related to a specific entity"""
        query = {
            'bool': {
                'should': [
                    {'term': {'source_account': entity_id}},
                    {'term': {'destination_account': entity_id}},
                    {'term': {'entity_id': entity_id}}
                ],
                'minimum_should_match': 1
            }
        }
        
        result = self.es.search(
            index='financial_transactions',
            body={
                'query': query,
                'size': size,
                'sort': [{'timestamp': {'order': 'desc'}}]
            }
        )
        
        return result['hits']['hits']
    
    def get_entity_by_id(self, entity_id):
        """Get entity details by ID"""
        try:
            result = self.es.get(
                index='financial_entities',
                id=entity_id
            )
            return result['_source']
        except:
            return None