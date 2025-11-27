from .models import InventoryItem

def get_low_stock_items():
    items = InventoryItem.objects.all()
    return [item for item in items if item.is_low_stock]
