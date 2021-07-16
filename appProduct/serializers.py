from rest_framework import serializers
from .models import Category, Cloth, Product


class CategorySeriallizer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'id',
            'category_name'
        )
        model = Category


class ClothSeriallizer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'id',
            'title',
            'category',
            'price',
            'stock'
        )
        model = Cloth


class ProductSeriallizer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'id',
            'Product_name',
            'category',
            'price',
            'stock'
        )
        model = Product
