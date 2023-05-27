from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Product, Category
from .permission import IsOwnerOrReadOnly
from .serializers import ProductSerializer, CategorySerializer, CategoryMakeSerializer, ProductMakeSerializer


class ProductCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductMakeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'category']
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user.id
        return Product.objects.filter(owner=user)

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryMakeSerializer
    permission_classes = [IsAuthenticated]


class CategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'name'
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CategoryUpdate(generics.UpdateAPIView):
    queryset = Category.objects.all()
    lookup_field = 'name'
    serializer_class = CategoryMakeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
