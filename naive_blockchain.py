# Naive blockchain
# Source: https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531

import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof = 100)

    def new_block(self, proof, previous_hash = None):
        block = {
            # increment index after each block's addition:
            'index': len(self.chain) + 1,
            'timestamp': time(),
            # pending transactions: 
            'transactions': self.pending_transactions,
            # proof here is a valid nonce:
            'proof': proof,
            # Either the previous block's hash is passed, or calculated ad hoc by hashing the last block on the existing chain:
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # Since all pending transactions have been moved to the block:
        self.pending_transactions = []

        # Add this block to the chain
        self.chain.append(block)

        return block

    @property
    def last_block(self):
        
        # Return last block in chain:
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        self.pending_transactions.append(transaction)

        # Return the next index after the last block:
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys = True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Aqib", "5 BTC")
t2 = blockchain.new_transaction("Aqib", "Satoshi", "1 BTC")
t3 = blockchain.new_transaction("Satoshi", "Hal Finney", "5 BTC")
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Aqib", "Alice", "1 BTC")
t5 = blockchain.new_transaction("Alice", "Bob", "0.5 BTC")
t6 = blockchain.new_transaction("Bob", "Alice", "0.5 BTC")
blockchain.new_block(6789)

print("Blockchain: ")
for each in blockchain.chain:
    print(each)

