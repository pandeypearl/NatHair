from django.urls import path
from .views import ProductView,ProductDetailView

urlpatterns = [
    # Products
    path('products', ProductView.as_view(), name='products'),
    path('product_detail/<pk>/', ProductDetailView.as_view(), name='product_detail'),
]