import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from datetime import datetime

def detect_anomalies(data, contamination=0.05):
    """
    Detect anomalies in financial data using Isolation Forest algorithm.
    
    Args:
        data (list): List of dictionaries containing financial transaction data
        contamination (float): The proportion of outliers in the data set
        
    Returns:
        list: List of dictionaries containing anomaly information
    """
    # Convert to DataFrame for easier processing
    df = pd.DataFrame(data)
    
    # Select numerical features for anomaly detection
    # Assuming data has columns like 'amount', 'frequency', 'age_of_account', etc.
    numerical_features = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if not numerical_features:
        return []
    
    # Apply Isolation Forest
    model = IsolationForest(
        contamination=contamination,
        random_state=42,
        n_estimators=100
    )
    
    # Fit and predict
    df['anomaly_score'] = model.fit_predict(df[numerical_features])
    
    # Convert scores: -1 for anomalies, 1 for normal
    # Convert to a 0-1 scale where higher means more anomalous
    df['anomaly_score'] = df['anomaly_score'].apply(lambda x: 0 if x == 1 else 1)
    
    # Get feature importance
    if hasattr(model, 'feature_importances_'):
        feature_importance = dict(zip(numerical_features, model.feature_importances_))
    else:
        feature_importance = {}
    
    # Filter anomalies and prepare result
    anomalies = df[df['anomaly_score'] > 0].copy()
    
    # Prepare results
    results = []
    for _, row in anomalies.iterrows():
        # Determine the reason for flagging
        if feature_importance:
            # Find the feature that contributed most to the anomaly
            max_feature = max(feature_importance.items(), key=lambda x: x[1])[0]
            reason = f"Unusual {max_feature} value"
        else:
            reason = "Unusual pattern detected"
        
        # Create alert object
        alert = {
            "entity": row.get('entity_id', str(row.name)),  # Use entity_id if available, otherwise use index
            "score": float(row['anomaly_score']),
            "reason": reason,
            "timestamp": datetime.now().isoformat()
        }
        
        results.append(alert)
    
    return results