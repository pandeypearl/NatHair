from django.contrib import admin
from .models import UserProfile, Profile, HairProfile, TextureProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Profile)
admin.site.register(HairProfile)
admin.site.register(TextureProfile)

