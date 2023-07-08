from pydantic import BaseModel
from models.address import Address # Importing Address model
from typing import List 

# Model for product when order is placed
class productForOrder(BaseModel):
    id: str
    quantity: int

# Order model
class Order(BaseModel):
    products: List[productForOrder]
    amount: float
    address: Address
