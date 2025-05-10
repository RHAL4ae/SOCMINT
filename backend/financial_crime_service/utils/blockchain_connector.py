import os
import json
import hashlib
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

class BlockchainConnector:
    """
    Handles blockchain interactions for forensic report immutability.
    """
    def __init__(self):
        provider = os.getenv('BLOCKCHAIN_PROVIDER')
        private_key = os.getenv('PRIVATE_KEY')
        chain_id = int(os.getenv('CHAIN_ID', '1'))
        self.web3 = Web3(Web3.HTTPProvider(provider))
        self.account = self.web3.eth.account.from_key(private_key)
        self.chain_id = chain_id

    def hash_report(self, report_data):
        """
        Hash the forensic report (dict or str) for blockchain storage.
        """
        if not isinstance(report_data, str):
            report_data = json.dumps(report_data, sort_keys=True)
        return hashlib.sha256(report_data.encode()).hexdigest()

    def send_hash_to_chain(self, report_hash):
        """
        Store the hash on-chain as a simple transaction (data field).
        Returns the transaction hash.
        """
        nonce = self.web3.eth.get_transaction_count(self.account.address)
        tx = {
            'nonce': nonce,
            'to': self.account.address,  # Send to self (or a burn address)
            'value': 0,
            'gas': 21000,
            'gasPrice': self.web3.eth.gas_price,
            'chainId': self.chain_id,
            'data': self.web3.to_bytes(hexstr=report_hash)
        }
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.web3.toHex(tx_hash)
