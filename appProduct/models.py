from django.db import models


# Create your models here.
class Category(models.Model):
    """ Represents categories """
    category_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class Cloth(models.Model):

    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="cloth")
    price = models.IntegerField()
    stock = models.IntegerField()

    class Meta:
        verbose_name_plural = "ChildCategories"

    def __str__(self):
        return self.title


class Product(models.Model):
    """ Represents Product entity """

    Product_name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    stock = models.IntegerField()

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.Product_name
