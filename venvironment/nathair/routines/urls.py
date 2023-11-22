from django.urls import include, path
from. import views

urlpatterns = [
    path('create_routine', views.create_routine, name='create_routine'),
    path('routine_detail/<int:routine_id>', views.routine_detail, name='routine_detail'),
]