from fastapi import FastAPI

from .models import Transaction
from .models import Block
from .models import Blockchain

from .schemas import TransactionModel

app = FastAPI(title='Simple blockchain example', version='1')

blockchain = None


@app.on_event('startup')
def starup():
    global blockchain
    blockchain = Blockchain()


@app.get('/blockchain')
async def get_chain():
    return blockchain.get_chain()
