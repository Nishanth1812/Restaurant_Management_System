import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management_system.settings')
django.setup()

from menu.models import Item
from inventory.models import InventoryItem
from orders.serializers import OrderSerializer
from orders.models import Table

def verify():
    print("Verifying Inventory Deduction...")

    # 1. Get Items
    butter_chicken = Item.objects.get(name='Butter Chicken')
    chicken_stock = InventoryItem.objects.get(name='Chicken')
    
    initial_qty = chicken_stock.quantity
    print(f"Initial Chicken Stock: {initial_qty} {chicken_stock.unit}")

    # 2. Place Order (using Serializer to trigger logic)
    # Ensure we have a table
    table, _ = Table.objects.get_or_create(number=1, capacity=4)
    
    order_data = {
        'table': table.id,
        'items': [
            {'item': butter_chicken, 'quantity': 2}  # 2 Butter Chickens = 0.6kg Chicken
        ]
    }
    
    # We need to pass 'item' as ID for serializer if we were passing JSON, 
    # but here we are calling create directly or passing objects?
    # Serializer expects data. Let's mock the validated_data structure 
    # OR use the serializer to validate and create.
    
    # Let's construct data as if it came from API
    data = {
        'table': table.id,
        'items': [
            {'item': butter_chicken.id, 'quantity': 2}
        ]
    }
    
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        print("Order Validated. Creating...")
        serializer.save()
        print("Order Created.")
    else:
        print("Validation Failed:", serializer.errors)
        return

    # 3. Check Final Stock
    chicken_stock.refresh_from_db()
    final_qty = chicken_stock.quantity
    print(f"Final Chicken Stock: {final_qty} {chicken_stock.unit}")
    
    expected_qty = initial_qty - Decimal('0.6') # 0.3 * 2
    
    # Note: Inventory quantity is IntegerField in models.py? 
    # Let's check models.py. 
    # InventoryItem.quantity is IntegerField? 
    # If so, we have a problem with 0.3kg.
    # Let's check inventory/models.py content from previous turns.
    # It was IntegerField!
    
    # CRITICAL: We need to change InventoryItem.quantity to FloatField or DecimalField!
    # I will check this in the next step if verification fails or before running.
    
    if final_qty == expected_qty:
        print("SUCCESS: Inventory deducted correctly.")
    else:
        print(f"FAILURE: Expected {expected_qty}, got {final_qty}")

if __name__ == '__main__':
    verify()
