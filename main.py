from fastapi import FastAPI
from routes.productRoutes import router as productRouter # Importing the router from the productRoutes file
from routes.orderRoutes import router as orderRouter # Importing the router from the orderRoutes file

app = FastAPI()

app.include_router(productRouter) 
app.include_router(orderRouter)