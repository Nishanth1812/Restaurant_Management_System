from rest_framework import viewsets, permissions
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from accounts.permissions import IsAdminOrReadOnly

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]
