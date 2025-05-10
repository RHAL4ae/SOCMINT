import os
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Dict, Optional
from datetime import datetime

class PostgresWriter:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "forensics"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432")
        )
        self.conn.autocommit = True

    def insert_report(self, tenant_id: str, title: str, timeline: List[Dict]) -> int:
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO incident_reports (tenant_id, title, timeline_json, created_at)
                VALUES (%s, %s, %s, %s) RETURNING id
                """,
                (tenant_id, title, timeline, datetime.utcnow())
            )
            return cur.fetchone()[0]

    def insert_evidence_log(self, report_id: int, sha256_hash: str, blockchain_reference: str, timestamp: str):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO evidence_log (report_id, sha256_hash, blockchain_reference, timestamp)
                VALUES (%s, %s, %s, %s)
                """,
                (report_id, sha256_hash, blockchain_reference, timestamp)
            )

    def get_report(self, report_id: int) -> Optional[Dict]:
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM incident_reports WHERE id = %s", (report_id,))
            return cur.fetchone()

    def get_evidence_log(self, report_id: int) -> Optional[Dict]:
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM evidence_log WHERE report_id = %s", (report_id,))
            return cur.fetchone()