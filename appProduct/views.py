from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySeriallizer, ClothSeriallizer, ProductSeriallizer
from .models import Category, Cloth, Product


class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySeriallizer


class DetailsCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySeriallizer


class ListCloth(generics.ListCreateAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSeriallizer


class DetailsCloth(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSeriallizer


class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeriallizer


class DetailsProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeriallizer

