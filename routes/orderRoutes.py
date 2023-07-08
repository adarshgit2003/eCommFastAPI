from fastapi import APIRouter, Query, HTTPException 
from database import collection_orders # Importing the collection from the database of orders
from models.order import Order # Importing the Order model
from schemas.orderSchema import individual_order_serial, list_order_serial # Importing the serializers
from bson import ObjectId # Importing ObjectId to convert string id to ObjectId
from datetime import datetime, timedelta # Importing datetime to get the current time

router = APIRouter()


#Get all orders
@router.get("/orders/")
async def get_all_orders(page: int = Query(1, gt=0), limit: int = Query(10, gt=0)):
    skip = (page - 1) * limit # Calculating the number of documents to be skipped
    countOrders = collection_orders.count_documents({}) # Counting the total number of documents

    if skip >= countOrders: 
        raise HTTPException(status_code=404, detail="No more orders") # If the number of documents to be skipped is greater than the total number of documents, raise an exception
    
    current = collection_orders.find().skip(skip).limit(limit) # Querying the database
    return list_order_serial(current) # Returning the serialized data



#Get a single order
@router.get("/order/{id}")
async def get_single_order(id: str):
    try:
        order = collection_orders.find_one({"_id": ObjectId(id)}) # Querying the database by converting the string id to ObjectId
        return individual_order_serial(order) # Returning the serialized data
    except Exception as e:
        return {
            "status": 404,
            "message": "Order not found"
        }



#Post a new order
@router.post("/order/")
async def add_order(order: Order):
    try:
        order = order.dict() # Converting the order object to a dictionary

        utc_now = datetime.utcnow() # Getting the current time in UTC
        ist_now = utc_now + timedelta(hours=5, minutes=30) # Converting the current time to IST

        order["timestamp"] = ist_now # Adding the timestamp to the order

        collection_orders.insert_one(dict(order)) # Inserting the order into the database

        return {
            "status": 200,
            "message": "Order added successfully"
        }
    except Exception as e:
        return {
            "status": 400,
            "message": "Order not added"
        }
    



