from django.urls import path
from .views import ListCategory, DetailsCategory, ListCloth, DetailsCloth, ListProduct, DetailsProduct

urlpatterns = [

    path('categories/', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailsCategory.as_view(), name='singlecategory'),
    path('cloth', ListCloth.as_view(), name='cloth'),
    path('cloth/,<int:pk>/', DetailsCloth.as_view(), name='singlecloth'),
    path('products', ListProduct.as_view(),name='products'),
    path('products/,<int:pk>/', DetailsProduct.as_view(), name='singleproduct'),

]
