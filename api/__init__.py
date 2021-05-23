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


@app.get('/block/{block_id}')
async def get_block(block_id: int):
    return blockchain.get_block(block_id)


@app.post('/transaction')
async def create_transaction(transaction: TransactionModel):
    new_transaction = Transaction(sender=transaction.sender,
                                  reciver=transaction.receiver,
                                  amount=transaction.amount)
    new_transaction.set_timestamp()
    blockchain.add_transaction(new_transaction)

    return new_transaction


@app.get('/blockchain/mine')
async def mine():
    block_index = blockchain.mine_block()
    if not block_index:
        return 'Need transactions to mine block'
    return f'Block #{block_index} successfully mined'
