import unittest
from transaction import Transaction
import time
from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):

    def test_initialization(self):
        test_blockchain = Blockchain()
        self.assertEqual(len(test_blockchain.chain), 1)

    def test_mining(self):
        test_blockchain = Blockchain()
        test_transaction = Transaction("Clif", time.time(), "Out,300,Adam")
        test_blockchain.add_new_transaction(test_transaction)
        test_blockchain.mine()
        self.assertEqual(len(test_blockchain.chain), 2)

if __name__ == '__main__':
    unittest.main()