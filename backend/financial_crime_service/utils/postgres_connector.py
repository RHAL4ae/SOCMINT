import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

class PostgresConnector:
    """
    Connector for PostgreSQL database operations related to financial crime detection.
    Handles alerts and clusters data storage and retrieval.
    """
    def __init__(self):
        self.conn_params = {
            'dbname': os.getenv('POSTGRES_DB', 'socmint'),
            'user': os.getenv('POSTGRES_USER', 'postgres'),
            'password': os.getenv('POSTGRES_PASSWORD', 'postgres'),
            'host': os.getenv('POSTGRES_HOST', 'localhost'),
            'port': os.getenv('POSTGRES_PORT', '5432')
        }
        self._init_tables()
    
    def _get_connection(self):
        """Create a new database connection"""
        return psycopg2.connect(**self.conn_params)
    
    def _init_tables(self):
        """Initialize database tables if they don't exist"""
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                # Create financial_alerts table
                cur.execute("""
                CREATE TABLE IF NOT EXISTS financial_alerts (
                    id SERIAL PRIMARY KEY,
                    tenant_id VARCHAR(50) NOT NULL,
                    entity VARCHAR(100) NOT NULL,
                    score FLOAT NOT NULL,
                    reason TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """)
                
                # Create clusters table
                cur.execute("""
                CREATE TABLE IF NOT EXISTS clusters (
                    id SERIAL PRIMARY KEY,
                    cluster_id INTEGER NOT NULL,
                    member_id VARCHAR(100) NOT NULL,
                    risk_level VARCHAR(20) NOT NULL,
                    UNIQUE(cluster_id, member_id)
                );
                """)
                
                conn.commit()
    
    def insert_alert(self, tenant_id, alert_data):
        """Insert a new financial alert into the database"""
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                INSERT INTO financial_alerts (tenant_id, entity, score, reason, timestamp)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
                """, (
                    tenant_id,
                    alert_data['entity'],
                    alert_data['score'],
                    alert_data['reason'],
                    datetime.fromisoformat(alert_data['timestamp']) if isinstance(alert_data['timestamp'], str) else alert_data['timestamp']
                ))
                
                alert_id = cur.fetchone()[0]
                conn.commit()
                
                # Add the ID to the alert data
                alert_data['id'] = alert_id
                return alert_data
    
    def insert_cluster(self, cluster_data):
        """Insert a new cluster member into the database"""
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                INSERT INTO clusters (cluster_id, member_id, risk_level)
                VALUES (%s, %s, %s)
                ON CONFLICT (cluster_id, member_id) DO UPDATE
                SET risk_level = EXCLUDED.risk_level
                RETURNING id;
                """, (
                    cluster_data['cluster_id'],
                    cluster_data['member_id'],
                    cluster_data['risk_level']
                ))
                
                cluster_id = cur.fetchone()[0]
                conn.commit()
                
                # Add the ID to the cluster data
                cluster_data['id'] = cluster_id
                return cluster_data
    
    def get_alerts(self, tenant_id=None, limit=100):
        """Get recent financial alerts, optionally filtered by tenant_id"""
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                if tenant_id:
                    cur.execute("""
                    SELECT * FROM financial_alerts
                    WHERE tenant_id = %s
                    ORDER BY timestamp DESC
                    LIMIT %s;
                    """, (tenant_id, limit))
                else:
                    cur.execute("""
                    SELECT * FROM financial_alerts
                    ORDER BY timestamp DESC
                    LIMIT %s;
                    """, (limit,))
                
                return cur.fetchall()
    
    def get_clusters(self, risk_level=None, limit=100):
        """Get cluster information, optionally filtered by risk_level"""
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                if risk_level:
                    cur.execute("""
                    SELECT * FROM clusters
                    WHERE risk_level = %s
                    ORDER BY cluster_id
                    LIMIT %s;
                    """, (risk_level, limit))
                else:
                    cur.execute("""
                    SELECT * FROM clusters
                    ORDER BY cluster_id
                    LIMIT %s;
                    """, (limit,))
                
                return cur.fetchall()