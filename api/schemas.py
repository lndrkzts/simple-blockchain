from pydantic import BaseModel
from pydantic import root_validator


class TransactionModel(BaseModel):
    sender: str
    receiver: str
    amount: float
    
    @root_validator
    def check_fill_fields(cls, values):
        sender = values.get('sender').replace(" ", "")
        receiver = values.get('receiver').replace(" ", "")
        amount = values.get('amount')

        if not sender:
            raise ValueError('sender is empty')
        
        if not receiver:
            raise ValueError('receiver is empty')
        
        if not amount:
            raise ValueError('amount is 0')

        return values