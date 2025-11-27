from django.test import TestCase
from .models import Table, Order

class OrderTests(TestCase):
    def test_create_order(self):
        table = Table.objects.create(number=1, capacity=4)
        order = Order.objects.create(table=table)
        self.assertEqual(order.status, 'PENDING')
