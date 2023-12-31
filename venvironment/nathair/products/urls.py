from django.urls import path
from . import views

urlpatterns = [
    path('product_list', views.product_list, name='product_list'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('product_detail/<int:product_id>/save/', views.save_product, name='save_product'),
    path('saved_products', views.saved_products, name='saved_products'),
    path('unsave-product/<int:product_id>/', views.unsave_product, name='unsave_product')
]