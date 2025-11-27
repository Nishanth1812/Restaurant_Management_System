from rest_framework import viewsets, permissions
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer
from accounts.permissions import IsAdminOrReadOnly



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAdminOrReadOnly]
