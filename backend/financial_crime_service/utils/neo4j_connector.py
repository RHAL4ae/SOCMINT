import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Neo4jConnector:
    """
    Connector for Neo4j graph database operations related to financial crime detection.
    Handles storing and querying graph data for entity relationships analysis.
    """
    def __init__(self):
        uri = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
        user = os.getenv('NEO4J_USER', 'neo4j')
        password = os.getenv('NEO4J_PASSWORD', 'neo4j')
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        """Close the Neo4j driver connection"""
        self.driver.close()
    
    def push_graph(self, graph_data):
        """
        Push nodes and relationships to Neo4j graph database.
        
        Args:
            graph_data (dict): Dictionary containing 'nodes' and 'relationships' lists
            
        Returns:
            dict: Summary of operations performed
        """
        nodes_created = 0
        relationships_created = 0
        
        with self.driver.session() as session:
            # Create or merge nodes
            for node in graph_data.get('nodes', []):
                result = session.write_transaction(
                    self._create_or_merge_node,
                    node['id'],
                    node['type'],
                    node.get('properties', {})
                )
                nodes_created += result
            
            # Create relationships
            for rel in graph_data.get('relationships', []):
                result = session.write_transaction(
                    self._create_relationship,
                    rel['source'],
                    rel['target'],
                    rel['type'],
                    rel.get('properties', {})
                )
                relationships_created += result
        
        return {
            'nodes_created': nodes_created,
            'relationships_created': relationships_created
        }
    
    @staticmethod
    def _create_or_merge_node(tx, node_id, node_type, properties):
        # Convert properties to a string of Cypher parameters
        props = ', '.join([f"{k}: ${k}" for k in properties.keys()])
        
        # Create Cypher query
        query = f"""
        MERGE (n:{node_type} {{id: $node_id}})
        SET n += {{{props}}}
        RETURN n
        """
        
        # Add node_id to properties for the query
        properties['node_id'] = node_id
        
        result = tx.run(query, **properties)
        return result.consume().counters.nodes_created
    
    @staticmethod
    def _create_relationship(tx, source_id, target_id, rel_type, properties):
        # Convert properties to a string of Cypher parameters
        props = ', '.join([f"{k}: ${k}" for k in properties.keys()])
        
        # Create Cypher query
        query = f"""
        MATCH (source {{id: $source_id}})
        MATCH (target {{id: $target_id}})
        MERGE (source)-[r:{rel_type} {{{props}}}]->(target)
        RETURN r
        """
        
        # Add source_id and target_id to properties for the query
        properties['source_id'] = source_id
        properties['target_id'] = target_id
        
        result = tx.run(query, **properties)
        return result.consume().counters.relationships_created
    
    def get_high_centrality_nodes(self, limit=10):
        """
        Get nodes with high centrality scores using Neo4j's PageRank algorithm.
        
        Args:
            limit (int): Maximum number of nodes to return
            
        Returns:
            list: List of high centrality nodes with their scores
        """
        with self.driver.session() as session:
            return session.read_transaction(self._get_high_centrality_nodes, limit)
    
    @staticmethod
    def _get_high_centrality_nodes(tx, limit):
        # This query assumes you've run the PageRank algorithm in Neo4j
        # In a production environment, you would use Neo4j Graph Data Science library
        query = """
        MATCH (n)
        WHERE EXISTS(n.centrality_score)
        RETURN n.id AS id, labels(n)[0] AS type, n.centrality_score AS score
        ORDER BY n.centrality_score DESC
        LIMIT $limit
        """
        
        result = tx.run(query, limit=limit)
        return [record.data() for record in result]
    
    def get_suspicious_relationships(self, limit=100):
        """
        Get relationships marked as suspicious.
        
        Args:
            limit (int): Maximum number of relationships to return
            
        Returns:
            list: List of suspicious relationships
        """
        with self.driver.session() as session:
            return session.read_transaction(self._get_suspicious_relationships, limit)
    
    @staticmethod
    def _get_suspicious_relationships(tx, limit):
        query = """
        MATCH (source)-[r:SUSPICIOUS_LINKED]->(target)
        RETURN source.id AS source_id, target.id AS target_id, 
               r.reason AS reason, r.score AS score, r.timestamp AS timestamp
        ORDER BY r.score DESC
        LIMIT $limit
        """
        
        result = tx.run(query, limit=limit)
        return [record.data() for record in result]