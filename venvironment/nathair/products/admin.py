from django.contrib import admin
from .models import HairProduct, HairProductReview, SavedHairProduct

# Register your models here.
admin.site.register(HairProductReview)
admin.site.register(HairProduct)
admin.site.register(SavedHairProduct)