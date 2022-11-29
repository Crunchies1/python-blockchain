from hashlib import sha256
import json

class Block:
    '''
    index (int): Index of the current block
    transactions (Transaction[]) = List of transactions
    timestamp (date) = Time this block was created
    previous_hash (string) = The hash of the block before this. 0 if first block.
    nonce (string) = nonce
    '''
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        block_json = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_json.encode()).hexdigest()
