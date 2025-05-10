from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from analytics.anomaly_detection import detect_anomalies
from analytics.clustering import cluster_entities
from analytics.graph_risk_analysis import analyze_graph
from utils.postgres_connector import PostgresConnector
from utils.neo4j_connector import Neo4jConnector
from utils.blockchain_connector import BlockchainConnector
import os

app = FastAPI()

# Models
class RunAnalysisRequest(BaseModel):
    tenant_id: str
    data: list
    relationships: Optional[list] = None

class AlertResponse(BaseModel):
    id: int
    tenant_id: str
    entity: str
    score: float
    reason: str
    timestamp: str
    blockchain_tx: str

class ClusterResponse(BaseModel):
    cluster_id: int
    member_id: str
    risk_level: str

# Connectors
pg = PostgresConnector()
neo4j = Neo4jConnector()
blockchain = BlockchainConnector()

@app.post("/run-analysis")
def run_analysis(request: RunAnalysisRequest):
    # 1. Anomaly Detection
    anomalies = detect_anomalies(request.data)
    alerts_with_blockchain = []
    for anomaly in anomalies:
        # Generate forensic report (here, just the alert itself)
        forensic_hash = blockchain.hash_report(anomaly)
        tx_hash = blockchain.send_hash_to_chain(forensic_hash)
        anomaly['blockchain_tx'] = tx_hash
        pg.insert_alert(request.tenant_id, anomaly)
        alerts_with_blockchain.append(anomaly)
    # 2. Clustering
    clusters = cluster_entities(request.data)
    for cluster in clusters:
        pg.insert_cluster(cluster)
    # 3. Graph Analysis
    graph_result = analyze_graph(request.data, request.relationships)
    neo4j.push_graph(graph_result)
    return {"alerts": alerts_with_blockchain, "clusters": clusters, "graph": graph_result}

@app.get("/alerts", response_model=List[AlertResponse])
def get_alerts(tenant_id: Optional[str] = None):
    return pg.get_alerts(tenant_id)

@app.get("/clusters", response_model=List[ClusterResponse])
def get_clusters():
    return pg.get_clusters()