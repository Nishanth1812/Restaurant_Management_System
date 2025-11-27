from django.test import TestCase
from .models import InventoryItem

class InventoryTests(TestCase):
    def test_low_stock(self):
        item = InventoryItem.objects.create(name="Tomatoes", quantity=5, low_stock_threshold=10)
        self.assertTrue(item.is_low_stock)
