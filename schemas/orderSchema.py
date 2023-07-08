# Purpose: Schemas for order model

from schemas.productSchema import list_productForOrder_serial
from schemas.addressSchema import address_serial

def individual_order_serial(order) -> dict:
    return {
        "id": str(order["_id"]), # Converting the ObjectId to string
        "products": list_productForOrder_serial(order["products"]), # Serializing the products
        "amount": order["amount"],
        "timestamp": order["timestamp"],
        "address": address_serial(order["address"]) # Serializing the address
    }

def list_order_serial(orders) -> list:
    return [individual_order_serial(order) for order in orders] # Serializing each order