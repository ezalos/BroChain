from Account import Account
from Transaction import Transaction
from datetime import datetime

class Block():
    def __init__(self, transactions, last_block_hash, nonce, timestamp = datetime.now()):
        self.transactions = transactions
        self.last_block_hash = last_block_hash
        self.nonce = nonce
        self.timestamp = timestamp