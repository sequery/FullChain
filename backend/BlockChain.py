from block import Block

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(index=0, data="Genesis Block", previous_hash="0")
        genesis_block.hash = self.mine_block(genesis_block)
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            data=data,
            previous_hash=last_block.hash
        )
        new_block.hash = self.mine_block(new_block)
        self.chain.append(new_block)
        return new_block

    def mine_block(self, block):
        """
        Simple Proof-of-Work algorithm:
        Finds a hash with `difficulty` number of leading zeros.
        """
        prefix = '0' * self.difficulty
        while not block.compute_hash().startswith(prefix):
            block.nonce += 1
        return block.compute_hash()

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                print(f"Invalid hash at block {i}")
                return False

            if current.previous_hash != previous.hash:
                print(f"Invalid previous hash at block {i}")
                return False

            if not current.hash.startswith('0' * self.difficulty):
                print(f"Block {i} has invalid proof of work")
                return False

        return True
