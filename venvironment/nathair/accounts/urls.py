"""
    Module for account urls
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Login and Logout
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # Sign up and Confirmation
    path('signup/',views.signup, name='signup'),
    # User profile
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/<int:pk>/follow/', views.follow, name='follow'),
    path('profile/<int:pk>/unfollow/', views.unfollow, name='unfollow'),
    path('profile/<int:pk>/followers/', views.followers, name='followers'),
    path('profile/<int:pk>/following/', views.following, name='following'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('hair_profile/', views.hair_profile, name='hair_profile'),
    path('texture_profile/', views.texture_profile, name='texture_profile'),
    path('search', views.search, name='search'),
    # Change Password
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='change-password.html',
        success_url = '/'
    ), name='change_password'),
    # Forgot Password
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password-reset/password_reset.html',
        subject_template_name='password-reset/password_reset_subject.txt',
        email_template_name='password-reset/password_reset_email.html',
        success_url='/login'
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password-reset/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password-reset/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password-reset/password_reset_complete.html'
    ), name='password_reset_complete'),
]