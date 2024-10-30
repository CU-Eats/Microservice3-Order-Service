from django.test import TestCase
from orders.services import OrderService
from orders.models import Order
from datetime import date

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

    def test_parse_time(self):
        test_date_string = '2024-10-28'
        test_date = date(2024, 10, 28)

        self.assertEqual(OrderService.parse_time(test_date_string), test_date)
