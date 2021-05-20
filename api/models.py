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
