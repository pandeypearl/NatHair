from django.urls import include, path
from. import views

urlpatterns = [
    path('create_routine', views.create_routine, name='create_routine'),
    path('routines_list', views.routines_list, name='routines_list'),
    path('routine_detail/<int:routine_id>', views.routine_detail, name='routine_detail'),
    path('delete_routine/<int:pk>', views.delete_routine, name='delete_routine'),
    path('routine_detail/<int:routine_id>/save/', views.save_routine, name='save_routine'),
    path('saved_routines', views.saved_routines, name='saved_routines'),
    path('unsave-routine/<int:routine_id>/', views.unsave_routine, name='unsave_routine'),
]