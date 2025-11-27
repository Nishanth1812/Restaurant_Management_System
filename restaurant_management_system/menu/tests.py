from django.test import TestCase
from .models import Category, Item

class MenuTests(TestCase):
    def test_create_item(self):
        cat = Category.objects.create(name="Drinks")
        item = Item.objects.create(category=cat, name="Coke", price=2.50)
        self.assertEqual(item.name, "Coke")
