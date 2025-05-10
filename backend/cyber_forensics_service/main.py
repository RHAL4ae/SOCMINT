from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from forensics.timeline_reconstruction import build_timeline
from forensics.evidence_correlation import correlate_evidence
from forensics.blockchain_logger import log_to_blockchain, verify_on_blockchain
from utils.elasticsearch_fetcher import fetch_logs
from utils.postgres_writer import PostgresWriter
from utils.blockchain_client import BlockchainClient
import os

app = FastAPI()

class GenerateReportRequest(BaseModel):
    tenant_id: str
    title: str
    osint: list
    financial_data: list
    logs_query: dict

class ReportResponse(BaseModel):
    id: int
    tenant_id: str
    title: str
    timeline: list
    blockchain_tx: str
    created_at: str

class VerifyResponse(BaseModel):
    report_id: int
    verified: bool
    blockchain_reference: str
    timestamp: str

pg = PostgresWriter()
bc = BlockchainClient()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate-report", response_model=ReportResponse)
def generate_report(request: GenerateReportRequest):
    logs = fetch_logs(request.logs_query)
    timeline = build_timeline(logs)
    report = correlate_evidence(request.osint, request.financial_data, timeline)
    report_id = pg.insert_report(request.tenant_id, request.title, timeline)
    hash_val, tx_id, timestamp = log_to_blockchain(report, bc)
    pg.insert_evidence_log(report_id, hash_val, tx_id, timestamp)
    return {
        "id": report_id,
        "tenant_id": request.tenant_id,
        "title": request.title,
        "timeline": timeline,
        "blockchain_tx": tx_id,
        "created_at": timestamp
    }

@app.get("/report/{id}", response_model=ReportResponse)
def get_report(id: int):
    report = pg.get_report(id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@app.get("/verify/{id}", response_model=VerifyResponse)
def verify_report(id: int):
    log = pg.get_evidence_log(id)
    if not log:
        raise HTTPException(status_code=404, detail="Evidence log not found")
    verified = verify_on_blockchain(log["sha256_hash"], log["blockchain_reference"], bc)
    return {
        "report_id": id,
        "verified": verified,
        "blockchain_reference": log["blockchain_reference"],
        "timestamp": log["timestamp"]
    }