import os
from web3 import Web3
from typing import Tuple
from datetime import datetime

class BlockchainClient:
    def __init__(self):
        self.provider = os.getenv("BLOCKCHAIN_PROVIDER", "http://localhost:8545")
        self.private_key = os.getenv("PRIVATE_KEY")
        self.chain_id = int(os.getenv("CHAIN_ID", "1"))
        self.web3 = Web3(Web3.HTTPProvider(self.provider))
        self.account = self.web3.eth.account.from_key(self.private_key) if self.private_key else None

    def log_hash(self, sha256_hash: str) -> Tuple[str, str]:
        # For demo: send a simple transaction with hash in data field
        nonce = self.web3.eth.get_transaction_count(self.account.address)
        tx = {
            'nonce': nonce,
            'to': self.account.address,
            'value': 0,
            'gas': 21000,
            'gasPrice': self.web3.to_wei('1', 'gwei'),
            'data': self.web3.to_hex(text=sha256_hash),
            'chainId': self.chain_id
        }
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_id = self.web3.to_hex(tx_hash)
        timestamp = datetime.utcnow().isoformat() + 'Z'
        return tx_id, timestamp

    def verify_hash(self, sha256_hash: str, blockchain_reference: str) -> bool:
        # For demo: check if hash is in the data field of the tx
        tx = self.web3.eth.get_transaction(blockchain_reference)
        return sha256_hash in self.web3.to_text(tx.input)