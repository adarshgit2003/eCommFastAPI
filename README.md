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
 	env\Scripts\activate
#### 3. Install the dependencies : Use the pip package manager for installing this project
	pip install fastapi

