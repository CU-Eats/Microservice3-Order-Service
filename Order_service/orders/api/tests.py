from django.test import TestCase
from orders.services import OrderService
from orders.models import Order
from rest_framework.test import APIClient
from datetime import date

RESTAURANT_API = '/api/orders/restaurant_orders/'
USER_ORDERS_API = '/api/orders/user_orders/'
CREATE_API = '/api/orders/'

class OrderServiceTest(TestCase):

    def setUp(self):
        order1 = Order.objects.create(
            order_id=1,
            product_name='product1',
            user_id = 1,
            user_name='user1',
            restaurant_name='restaurant1',
            quantity=1,
        )
        self.client = APIClient()

    def test_restaurant_orders(self):
        response = self.client.get(RESTAURANT_API)
        self.assertEqual(response.status_code, 400)

        response = self.client.get(RESTAURANT_API, {'restaurant_name': 'restaurant1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['user_id'], 1)

        response = self.client.get(
            RESTAURANT_API,
            {
                'restaurant_name': 'restaurant1',
                'created_at': str(date.today())
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['user_id'], 1)

        response = self.client.get(
            RESTAURANT_API,
            {
                'restaurant_name': 'restaurant1',
                'created_at': '2024-10-27'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_user_orders(self):
        response = self.client.get(USER_ORDERS_API)
        self.assertEqual(response.status_code, 400)

        response = self.client.get(USER_ORDERS_API, {'user_id': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['restaurant_name'], 'restaurant1')

        response = self.client.get(
            USER_ORDERS_API,
            {
                'user_id': '1',
                'created_at': str(date.today())
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['restaurant_name'], 'restaurant1')

        response = self.client.get(
            USER_ORDERS_API,
            {
                'user_id': '1',
                'created_at': '2024-10-27'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_create(self):
        response = self.client.post(
            CREATE_API,
            {
                'order_id': 1,
                'product_name': 'product1',
                'user_id': 1,
                'user_name': 'user1',
                'restaurant_name': 'restaurant1',
                'quantity': 1,
            }
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['user_name'], 'user1')
        self.assertEqual(response.data['restaurant_name'], 'restaurant1')
