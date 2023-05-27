from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'owner', 'category', 'name', 'get_absolute_url', 'description', 'price', 'date_added']
        lookup_field = 'name'


class ProductMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'owner', 'category', 'name', 'get_absolute_url', 'description', 'price', 'image']
        lookup_field = 'name'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'get_absolute_url', 'products']
        lookup_field = 'name'


class CategoryMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        lookup_field = 'name'

# class UserSerializer(serializers.ModelSerializer):
#     products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'products']
