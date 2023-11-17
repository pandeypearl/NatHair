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
    path('update_profile/', views.update_profile, name='update_profile'),
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