from django.urls import path
from .views import ProductView, ProductDetailView

urlpatterns = [
    # Products
    path('product-list', ProductView.as_view(), name='product_list'),
    path('product_detail/<pk>/', ProductDetailView.as_view(), name='product_detail'),
]