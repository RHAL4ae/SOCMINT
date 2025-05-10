import pandas as pd
import numpy as np
from datetime import datetime

def analyze_graph(data, relationships=None):
    """
    Analyze relationships between entities to identify suspicious networks.
    Prepares data for Neo4j graph database and calculates centrality metrics.
    
    Args:
        data (list): List of dictionaries containing entity data
        relationships (list): List of dictionaries defining relationships between entities
        
    Returns:
        dict: Dictionary containing nodes and relationships for Neo4j
    """
    if not relationships:
        relationships = []
    
    # Convert to DataFrame for easier processing
    entities_df = pd.DataFrame(data)
    relationships_df = pd.DataFrame(relationships) if relationships else pd.DataFrame()
    
    # Prepare nodes for Neo4j
    nodes = []
    for _, row in entities_df.iterrows():
        # Determine node type based on available information
        if 'type' in row:
            node_type = row['type']
        elif 'account_number' in row:
            node_type = 'Account'
        elif 'company_name' in row:
            node_type = 'Company'
        elif 'transaction_id' in row:
            node_type = 'Transaction'
        else:
            node_type = 'Person'  # Default type
        
        # Create node with properties
        node = {
            'id': row.get('entity_id', str(row.name)),
            'type': node_type,
            'properties': row.to_dict()
        }
        
        nodes.append(node)
    
    # Prepare relationships for Neo4j
    graph_relationships = []
    
    # Use provided relationships if available
    if not relationships_df.empty:
        for _, row in relationships_df.iterrows():
            rel = {
                'source': row['source_id'],
                'target': row['target_id'],
                'type': row.get('relationship_type', 'CONNECTED_TO'),
                'properties': row.to_dict()
            }
            graph_relationships.append(rel)
    else:
        # If no relationships provided, try to infer some basic ones
        # This is a simplified approach - in a real system, you would use more sophisticated methods
        if 'owner_id' in entities_df.columns:
            for _, row in entities_df.iterrows():
                if pd.notna(row.get('owner_id')):
                    rel = {
                        'source': row.get('owner_id'),
                        'target': row.get('entity_id', str(row.name)),
                        'type': 'OWNS',
                        'properties': {
                            'since': row.get('created_date', datetime.now().isoformat())
                        }
                    }
                    graph_relationships.append(rel)
    
    # Calculate PageRank-like centrality (simplified version)
    # In a real implementation, you would use Neo4j's graph algorithms
    centrality = calculate_simple_centrality(nodes, graph_relationships)
    
    # Add centrality score to nodes
    for node in nodes:
        node['properties']['centrality_score'] = centrality.get(node['id'], 0.0)
        
        # Flag suspicious nodes based on centrality
        if centrality.get(node['id'], 0.0) > 0.7:
            rel = {
                'source': node['id'],
                'target': node['id'],  # Self-relationship for flagging
                'type': 'SUSPICIOUS_LINKED',
                'properties': {
                    'reason': 'High centrality in network',
                    'score': centrality.get(node['id'], 0.0),
                    'timestamp': datetime.now().isoformat()
                }
            }
            graph_relationships.append(rel)
    
    return {
        'nodes': nodes,
        'relationships': graph_relationships
    }

def calculate_simple_centrality(nodes, relationships, damping=0.85, iterations=20):
    """
    Calculate a simplified version of PageRank centrality.
    
    Args:
        nodes (list): List of node dictionaries
        relationships (list): List of relationship dictionaries
        damping (float): Damping factor for PageRank
        iterations (int): Number of iterations
        
    Returns:
        dict: Dictionary mapping node IDs to centrality scores
    """
    # Initialize scores
    node_ids = [node['id'] for node in nodes]
    scores = {node_id: 1.0 / len(node_ids) for node_id in node_ids}
    
    # Build adjacency map
    outgoing = {node_id: [] for node_id in node_ids}
    incoming = {node_id: [] for node_id in node_ids}
    
    for rel in relationships:
        source = rel['source']
        target = rel['target']
        
        if source in outgoing and target in incoming:
            outgoing[source].append(target)
            incoming[target].append(source)
    
    # PageRank iterations
    for _ in range(iterations):
        new_scores = {}
        
        for node_id in node_ids:
            # Base score from random jumps
            new_score = (1 - damping) / len(node_ids)
            
            # Score from incoming links
            for in_neighbor in incoming[node_id]:
                if outgoing[in_neighbor]:
                    new_score += damping * scores[in_neighbor] / len(outgoing[in_neighbor])
            
            new_scores[node_id] = new_score
        
        # Update scores
        scores = new_scores
    
    return scores