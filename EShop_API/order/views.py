from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from product.permission import IsOwnerOrReadOnly
from .models import Order
from .serializers import MyOrderSerializer, OrderSerializer, OrderChangeSerializer


class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        paid_amount = sum(
            item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])
        serializer.save(owner=self.request.user, paid_amount=paid_amount)


class OrdersList(generics.ListAPIView):
    serializer_class = MyOrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'paid_amount']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        return Order.objects.filter(owner=user)


class OrderDetails(generics.RetrieveDestroyAPIView):
    serializer_class = MyOrderSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user.id
        return Order.objects.filter(owner=user)


class OrderUpdate(generics.UpdateAPIView):
    serializer_class = OrderChangeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user.id
        return Order.objects.filter(owner=user)
