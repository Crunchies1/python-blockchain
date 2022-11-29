from block import Block
import time

class Blockchain:
    '''
    unconfirmed_transactions (Transaction[]): Transactions to be verified
    chain (Block[]) = Blocks in the blockchain
    create_genesis_block() : Function to create first block
    '''
    def __init__(self, difficulty = 2):
        self.unconfirmed_transactions = []
        self.chain = []
        self.difficulty = difficulty
        self.init_blockchain()

    def init_blockchain(self):
        block = Block(0, [], time.time(), "0")
        block.compute_hash()
        self.chain.append(block)

    @property
    def last_block(self):
        return self.chain[-1]

    # Find a hash that starts with a certain number of zeroes
    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    # Adding a block to the end of the block chain.
    def add_block(self, block, proof):
        previous_hash = self.last_block.compute_hash()
        # We need to check that we have a valid hash and that the block submitted
        # has the hash of the previous block.
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True
 
    # Check that the hash starts with a certain number of zeroes.
    def is_valid_proof(self, block, block_hash):
            return (block_hash.startswith('0' * self.difficulty) and
                    block_hash == block.compute_hash())

    def add_new_transaction(self, transaction):
                self.unconfirmed_transactions.append(transaction)

    # Mining function.
    def mine(self):
        # Wait until there are unconfirmed transactions
        if not self.unconfirmed_transactions:
            return False
 
        last_block = self.last_block
 
        # Create a new block to confirm all unconfirmed transactions
        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.compute_hash())
 
        # Get a valid hash
        proof = self.proof_of_work(new_block)
        # Try to add the block to the blockchain
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index