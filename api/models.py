import hashlib
import json
import time

from typing import List


class Transaction:
    def __init__(self, sender: str, reciver: str, amount: float):
        self.sender = sender
        self.reciver = reciver
        self.message = amount
        self.timestamp = 0

    def set_timestamp(self):
        if not self.timestamp:
            self.timestamp = time.time()


class Block:
    def __init__(self, index: int, transactions: List, previous_hash: str, timestamp: float):
        self.index = index
        self.nounce = 0
        self.hash = ''
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = timestamp

    def generate_hash(self):
        block_string = json.dumps(self.__dict__, default=lambda o: o.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    difficulty = 4

    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.create_genesis_block()

    @property
    def last_block(self):
        return self.chain[-1]

    def get_block(self, num: int):
        if len(self.chain) < num:
            return 'Invalid block'
        return self.chain[num].__dict__

    def get_chain(self):
        chain_data = []

        for block in self.chain:
            chain_data.append(block.__dict__)

        return chain_data

    def create_genesis_block(self):
        genesis_block = Block(index=0,
                              transactions=[],
                              previous_hash='0'*64,
                              timestamp=time.time())

        genesis_block.hash = genesis_block.generate_hash()
        self.chain.append(genesis_block)

    def add_transaction(self, transaction: Transaction):
        self.unconfirmed_transactions.append(transaction)

    def proof_of_work(self, block: Block):
        computed_hash = block.generate_hash()

        while not computed_hash.startswith('0'*Blockchain.difficulty):
            block.nounce += 1
            computed_hash = block.generate_hash()
            print(computed_hash)  # TODO Delete this

        return computed_hash

    def validate_proof(self, block: Block, block_hash: str):
        return block_hash.startswith('0'*Blockchain.difficulty) and block_hash == block.generate_hash()

    def add_block(self, block: Block, proof: str):
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.validate_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)

        return True

    def mine_block(self):
        if not self.unconfirmed_transactions:
            return False

        new_block = Block(index=self.last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=self.last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []

        return new_block.index
