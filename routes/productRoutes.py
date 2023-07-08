from fastapi import APIRouter 
from database import collection_products # Importing the collection from the database of products
from models.product import Product # Importing the Product model
from schemas.productSchema import individual_product_serial, list_product_serial # Importing the serializers
from bson import ObjectId # Importing ObjectId to convert string id to ObjectId

router = APIRouter()

#Get all products
@router.get("/products/")
async def get_all_products():
    products = collection_products.find() # Querying the database
    return list_product_serial(products) # Returning the serialized data



#Get a single product
@router.get("/product/{id}")
async def get_single_product(id: str):
    try:
        product = collection_products.find_one({"_id": ObjectId(id)}) # Querying the database by converting the string id to ObjectId
        return individual_product_serial(product) # Returning the serialized data
    except Exception as e:
        return {
            "status": 404,
            "message": "Product not found"
        }



#Add a new product
@router.post("/product/")
async def add_product(product: Product):
    collection_products.insert_one(dict(product)) # Inserting the product into the database
    return {
        "status": 200,
        "message": "Product addded successfully"
    }



#Update a product
@router.put("/product/{id}")
async def update_product(id: str, product: Product): 
    try:
        collection_products.update_one({"_id": ObjectId(id)}, {"$set": dict(product)}) # Updating the product in the database
        return {
            "status": 200,
            "message": "Product updated successfully"
        }
    except Exception as e:  
        return {
            "status": 404,
            "message": "Product not found"
        }



#Delete a product
@router.delete("/product/{id}")
async def delete_product(id: str):
    try:
        collection_products.delete_one({"_id": ObjectId(id)}) # Deleting the product from the database
        return {
            "status": 200,
            "message": "Product deleted successfully"
        }
    except Exception as e:
        return {
            "status": 404,
            "message": "Product not found"
        }

