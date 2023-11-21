from django.contrib import admin
from .models import Product, HairProduct, ProductReview

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(HairProduct)