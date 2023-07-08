# Purpose : Schemas for product model in two cases: 
# 1. when product is listed,
# 2. when product is listed for order

from database import collection_products
from bson import ObjectId


def individual_product_serial(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "description": product["description"],
        "quantity": product["quantity"]
    }


# 1. When product is listed
def list_product_serial(products) -> list:
    return [individual_product_serial(product) for product in products] # Serializing each product


# 2. When product is listed for order
def list_productForOrder_serial(products) -> list:
    p = []

    for product in products:
        pr = collection_products.find_one({"_id": ObjectId(product["id"])}) # Finding the product in the database by converting the string id to ObjectId
        pr["quantity"] = product["quantity"] # Change the quantity of the product to the quantity ordered
        p.append(pr) # Appending the product to the list

    return [individual_product_serial(product) for product in p] # Serializing each product