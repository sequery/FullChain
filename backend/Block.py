import hashlib
import json
from time import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Computes the hash of the block's contents.
        """
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()