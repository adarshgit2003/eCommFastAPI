# E-Commerce API using FastAPI
This GitHub repository aims to provide a comprehensive ecommerce solution using Python, FastAPI, and MongoDB Atlas. It combines the power of Python's versatility, FastAPI's modern web framework, and MongoDB Atlas's cloud-based database service to create a robust and scalable ecommerce application.
## Key Features
### 1. MongoDB Atlas Integration: 
The repository demonstrates the integration of MongoDB Atlas as the database backend. MongoDB Atlas provides a fully managed cloud-based database service, ensuring high availability, scalability, and security for your ecommerce application.
### 2. Database Schema
The repository includes a well-designed database schema using MongoDB's document-based model. It defines collections for products and orders, allowing for flexible and efficient data storage.
### 3. FastAPI Endpoints
FastAPI's routing capabilities are utilized to define endpoints for essential ecommerce operations. These operations include product listing, product details, order placement, and more. The use of route decorators like @app.get and @app.post simplifies the process of defining HTTP methods and URL paths for these endpoints.
### 4. Request and Response Models
FastAPI's request and response models are used to define the expected structure of data passed in requests and returned in responses. 
### 5. Asynchronous Programming
FastAPI's support for asynchronous programming using Python's async and await keywords enhances the performance of the ecommerce application. Asynchronous operations can be utilized for tasks like processing orders, interacting with the MongoDB database.

The main goal of this GitHub repository is to provide a solid foundation for building scalable and efficient ecommerce applications using Python, FastAPI, and MongoDB Atlas.

## Prerequisites
1. Python (Version 3.7+)
2. FastAPI
3. Pymongo (Official Python driver that connects to and interacts with MongoDB databases).

## Installation
#### 1. Clone the repository:
	git clone https://github.com/adarshgit2003/eCommFastAPI.git
#### 2. Set up the virtual environment in the folder
	python -m venv venv
 	venv\Scripts\activate
#### 3. Install the dependencies : Use the pip package manager for installing this project
	pip install fastapi
 	pip install uvicorn
#### 4. Set up the mongo db atlas

## Execution
#### 1. To start the API server, run the following command:
	uvicorn main:app --reload
#### 2. The API will be available at http://localhost:8000
#### 3. Access the Builtin API documentation of FastAPI at http://localhost:8000/docs in your web browser.

## API Endpoints
### 1. Navigate to Home
* Endpoint: "/"
* Method: GET
* Description: Navigate to Home
* Response: Things written in the home page.

### 2. Get all products
* Endpoint: "/products/"
* Method: GET
* Description: This endpoint retrieves a list of all products available in the system. It returns the information about the each product. The information contains product_id, name, price, description and quantity
* Response: JSON Response containing the list of products.
* #### For example:
		[
	 	{
		    "id": "64a92b3b251d9d219aa976d5",
		    "name": "Laptop",
		    "price": 50499,
		    "description": "A very good Lenovo Laptop",
		    "quantity": 5
		  },
		  {
		    "id": "64a951b6eeb07f5daacf76a2",
		    "name": "Samsung Mobile",
		    "price": 14599,
		    "description": "A new-version of Samsung",
		    "quantity": 20
		  },
	 	]

### 3. Get a single product with product_id
* Endpoint: "/product/{id}/"
* Method: GET
* Description: This endpoint retrieves the details of a specific product identified by its unique ID.
* Response: JSON Response containing the information about single product.
### 4. Update a single product with product_id
* Endpoint: "/product/{id}"
* Method: PUT
* Description: This endpoint is used to update an existing product identified by its ID. The client provides the updated information for the product, such as a new name, price, description and quantity.
* Require: You need the product id to update the product.
* Response: Returns a success message for the updated product details
### 5. Delete a single product with product_id
* Endpoint: "/product/{id}"
* Method: DELETE
* Description: This endpoint is responsible for deleting a specific product identified by its ID. When invoked, it removes the corresponding product from the system.
* Require: The id of the product which has to be deleted
* Response Returns a success message for the confirmation of deletion.
### 6. Add a new product
* Endpoint: "/product/"
* Method: POST
* Description: This endpoint allows the creation of a new product. It typically requires the client to provide the necessary information, such as the product name, price, description, and quantity.
* Require: Attributes of the product
* #### For example:
		{
		  "name": "Fan",
		  "price": 500,
		  "description": "Get a new fan in this summer",
		  "quantity": 40
		}
* Response: Returns a success message for the addition of new product.

### 7. Get all orders
* Endpoint: "/orders/"
* Method: GET
* Description: This endpoint retrieves a list of all orders available in the system.
* #### The information includes:
		* Order_id of the order.
		* List of product details which are ordered with quantity of each product.
  		* Total amount
  		* TimeStamp: At what time the order is placed
  		* Address: Address of the user
* #### Require:
  	* Page: It is page number(Optional). By default it is 1.
  	* Limit: Maximum order shown in each page(Optional). By default it is 10.
  	  
* Response: JSON response containing the list of orders.
* #### For example:
		[
		  {
		    "id": "64a95e7de20c637dd2e5ff2c",
		    "products": [
		      {
		        "id": "64a92b3b251d9d219aa976d5",
		        "name": "Laptop",
		        "price": 50499,
		        "description": "A very good Lenovo Laptop",
		        "quantity": 1
		      },
		      {
		        "id": "64a951b6eeb07f5daacf76a2",
		        "name": "Samsung Mobile",
		        "price": 14599,
		        "description": "A new-version of Samsung",
		        "quantity": 1
		      }
		    ],
		    "amount": 65098,
		    "timestamp": "2023-07-08T18:32:53.216000",
		    "address": {
		      "city": "Mairwa",
		      "state": "Bihar",
		      "country": "India",
		      "pincode": 841239
		    }
		  },
		  {
		    "id": "64aa5e8c9a8ba68482c963ab",
		    "products": [
		      {
		        "id": "64a95380eeb07f5daacf76aa",
		        "name": "Peter England Shirts",
		        "price": 1499,
		        "description": "Be Cool by wearing peter",
		        "quantity": 2
		      },
		      {
		        "id": "64a95247eeb07f5daacf76a5",
		        "name": "Boat Headphones",
		        "price": 1400,
		        "description": "Clear Sound",
		        "quantity": 1
		      },
		      {
		        "id": "64a952b2eeb07f5daacf76a7",
		        "name": "Rolex Watch",
		        "price": 100000,
		        "description": "Time is Money",
		        "quantity": 3
		      }
		    ],
		    "amount": 302337,
		    "timestamp": "2023-07-09T12:45:24.586000",
		    "address": {
		      "city": "Gorakhpur",
		      "state": "Uttar Pradesh",
		      "country": "India",
		      "pincode": 273010
		    }
		  }
		]

### 8. Get a single order by id
* Endpoint: "/order/{id}/"
* Method: GET
* Description: This endpoint retrieves the details of a specific order identified by its unique ID.
* Require: Id of the order
* Response: JSON response of the specific order.
### 9. Add a new order
* Endpoint: "/order/"
* Method: PUT
* Description: This endpoint adds a new order in the database.
* Require: Attributes of the order. It contains product_id and quantity of each product which is ordered, total amount and address of the user. It is a JSON array
* #### For example:
		{
		  "products": [
		    {
		      "id": "64a95380eeb07f5daacf76aa",
		      "quantity": 2
		    },
		    {
		      "id": "64a95247eeb07f5daacf76a5",
		      "quantity": 1
		    },
		    {
		      "id": "64a952b2eeb07f5daacf76a7",
		      "quantity": 3
		    }
		  ],
		  "amount": 302337,
		  "address": {
		    "city": "Gorakhpur",
		    "state": "Uttar Pradesh",
		    "country": "India",
		    "pincode": 273010
		  }
		}
* Response: Successful message for the addition of new order in the database.
