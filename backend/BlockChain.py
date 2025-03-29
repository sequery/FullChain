class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Generates the first block (genesis block) and appends it to the chain.
        """
        genesis_block = Block(index=0, data="Genesis Block", previous_hash="0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the chain with the given data.
        """
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            data=data,
            previous_hash=last_block.hash
        )
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        """
        Validates the blockchain by checking hash connections and recomputing hashes.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Check current block's hash
            if current.hash != current.compute_hash():
                print(f"Block {i} has invalid hash.")
                return False

            # Check hash linkage
            if current.previous_hash != previous.hash:
                print(f"Block {i} has invalid previous hash.")
                return False

        return True
