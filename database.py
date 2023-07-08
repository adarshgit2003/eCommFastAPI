from pymongo import MongoClient # Using pymongo to connect to MongoDB Atlas

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://wwwaksmw:mxbUUqAPYFKfx5Tv@cluster0.23djivm.mongodb.net/?retryWrites=true&w=majority")

# Making a database named as eComm
db = client.eComm

collection_products = db.products # Making a collection named as products
collection_orders = db.orders # Making a collection named as orders