from .models import Item

def get_available_items():
    return Item.objects.filter(is_available=True)
