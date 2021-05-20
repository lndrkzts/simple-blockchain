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
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
