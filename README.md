# Microservice3-Order-Service
This Order microservice is responsible for managing all order-related functionalities. It handles the creation, retrieval, and management of orders placed by users. The Order Microservice is built using Django. It operates independently with its own database and exposes a set of RESTful API endpoints for integration with the composite microservice and other sub-microservices.

## Features
- Order Creation
- Order Retrieval
- Order Management

## Order Model
The order data is stored using the following Django model:

## API Endpoints

### Base Message
- URL: ```GET /```
- Description: Returns a welcome message or basic information about the microservice.
- Input argument: None

### Get All Order
- URL: ```GET /everything/```
- Description: Retrieves a list of all orders.
- Input argument: None
