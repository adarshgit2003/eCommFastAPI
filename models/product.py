from pydantic import BaseModel

# Product model
class Product(BaseModel):
    name: str
    price: float
    description: str
    quantity: int