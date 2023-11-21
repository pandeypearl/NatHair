from django.urls import path
from .views import ProductView, ProductDetailView
from . import views

urlpatterns = [
    # Products
    # path('product-list', ProductView.as_view(), name='product_list'),
    # path('product_detail/<pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_list', views.product_list, name='product_list'),
    path('product_detail<int:product_id>', views.product_detail, name='product_detail'),
]