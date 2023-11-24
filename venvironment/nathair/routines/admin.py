from django.contrib import admin
from .models import HairRoutine, RoutineStep, SavedRoutine

# Register your models here.
admin.site.register(HairRoutine)
admin.site.register(RoutineStep)
admin.site.register(SavedRoutine)
