import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_entities(data, n_clusters=5):
    """
    Group entities by behavior using KMeans clustering to identify potential fraud rings or money routes.
    
    Args:
        data (list): List of dictionaries containing financial transaction data
        n_clusters (int): Number of clusters to form
        
    Returns:
        list: List of dictionaries containing cluster information
    """
    # Convert to DataFrame for easier processing
    df = pd.DataFrame(data)
    
    # Select numerical features for clustering
    numerical_features = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if not numerical_features or len(df) < n_clusters:
        return []
    
    # Standardize features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[numerical_features])
    
    # Apply KMeans clustering
    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )
    
    # Fit and predict
    df['cluster'] = kmeans.fit_predict(scaled_features)
    
    # Calculate risk level for each cluster
    # This is a simplified approach - in a real system, you would use more sophisticated methods
    cluster_risk = {}
    for cluster_id in range(n_clusters):
        cluster_data = df[df['cluster'] == cluster_id]
        
        # Calculate risk based on transaction patterns
        # For example: high frequency + high amounts = high risk
        if 'amount' in df.columns and 'frequency' in df.columns:
            avg_amount = cluster_data['amount'].mean()
            avg_frequency = cluster_data['frequency'].mean()
            
            # Simple risk scoring
            risk_score = (avg_amount * avg_frequency) / (df['amount'].mean() * df['frequency'].mean())
            
            if risk_score > 1.5:
                risk_level = "high"
            elif risk_score > 1.0:
                risk_level = "medium"
            else:
                risk_level = "low"
        else:
            # Default risk level if we don't have amount/frequency
            risk_level = "medium"
            
        cluster_risk[cluster_id] = risk_level
    
    # Prepare results
    results = []
    for _, row in df.iterrows():
        cluster_id = int(row['cluster'])
        member_id = row.get('entity_id', str(row.name))  # Use entity_id if available, otherwise use index
        
        cluster_info = {
            "cluster_id": cluster_id,
            "member_id": member_id,
            "risk_level": cluster_risk.get(cluster_id, "medium")
        }
        
        results.append(cluster_info)
    
    return results