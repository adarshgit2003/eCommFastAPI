from pydantic import BaseModel

# Address model
class Address(BaseModel):
    city: str
    state: str
    country: str
    pincode: int
