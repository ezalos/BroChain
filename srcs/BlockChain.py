from Block import *

class BlockChain():
    def __init__(self, transactions_per_block = 10, chain = []):
        self.chain = chain
        self.transactions_per_block = transactions_per_block
        self.pending_transactions = []

    def AddBlock(self, block):
        pass
