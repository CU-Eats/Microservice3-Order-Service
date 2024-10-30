# Microservice3-Order-Service
This Order microservice is responsible for managing all order-related functionalities. It handles the creation, retrieval, and management of orders placed by users. The Order Microservice is built using Django. It operates independently with its own database and exposes a set of RESTful API endpoints for integration with the composite microservice and other sub-microservices.

## Features
- Order Creation
- Order Retrieval
- Order Management

## Order Model
The order data is stored using the following Django model:
```
from django.db import models

class Order(models.Model):
    order_id = models.IntegerField(null=False)
    product_name = models.CharField(max_length=256, null=False)
    user_name = models.CharField(max_length=256, null=False)
    user_id = models.IntegerField(null=False)
    restaurant_name = models.CharField(max_length=256, null=False)
    quantity = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        index_together = (
            ('user_name', 'product_name'),
            ('restaurant_name', 'created_at'),
        )

    def __str__(self):
        return '{} ordered {} from {} at {}'.format(
            self.user_id,
            self.product_name,
            self.restaurant_name,
            self.created_at
        )
```

## API Endpoints

### Base URL
- All endpoints are prefixed with ```/api/orders/```.

### Create Order
- URL: ```POST /api/orders/```
- Description: Creates a new order.
- Input argument:
  | Parameter         | Type     | Description                                 |
  | ----------------- | -------- | ------------------------------------------- |
  | `order_id`        | Integer  | Unique identifier for the order             |
  | `product_name`    | String   | Name of the product being ordered           |
  | `user_name`       | String   | Name of the user placing the order          |
  | `user_id`         | Integer  | Unique identifier of the user               |
  | `restaurant_name` | String   | Name of the restaurant                      |
  | `quantity`        | Integer  | Quantity of the product ordered             |


### List Ordres
- URL: ```GET /api/orders/```
- Description: Retrieves a list of orders based on query parameters.
- Input argument: None

### Retrieve User Order
- URL: ```GET /api/orders/user_orders/```
- Description: Retrieves orders placed by a specific user.
- Input argument: 
  | Parameter         | Type     | Description                                 |
  | ----------------- | -------- | ------------------------------------------- |
  | `user_id`         | Integer  | Unique identifier of the user               |

### Retrieve Restaurant Orders
- URL: ```GET /api/orders/restaurant_orders/```
- Description: Retrieves orders placed by a specific restaurant.
- Input argument:
  | Parameter         | Type     | Description                                 |
  | ----------------- | -------- | ------------------------------------------- |
  | `restaurant_name` | String   | Name of the restaurant                      |
