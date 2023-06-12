from django.urls import path
from . import views
from .views import SignUpView, ProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]