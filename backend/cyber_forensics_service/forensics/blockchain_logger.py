import hashlib
from typing import Dict, Tuple
from datetime import datetime

def log_to_blockchain(report: Dict, blockchain_client) -> Tuple[str, str, str]:
    """
    Hash and timestamp the forensic report, log to blockchain, return (hash, txID, timestamp).
    """
    report_bytes = str(report).encode('utf-8')
    sha256_hash = hashlib.sha256(report_bytes).hexdigest()
    tx_id, timestamp = blockchain_client.log_hash(sha256_hash)
    return sha256_hash, tx_id, timestamp

def verify_on_blockchain(sha256_hash: str, blockchain_reference: str, blockchain_client) -> bool:
    """
    Verify the hash exists on blockchain with the given reference.
    """
    return blockchain_client.verify_hash(sha256_hash, blockchain_reference)