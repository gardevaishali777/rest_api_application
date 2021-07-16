from django.contrib import admin
from .models import Category, Product, Cloth


admin.site.register(Category)
admin.site.register(Cloth)
admin.site.register(Product)
