"""
    Module for account urls
"""
from django.urls import path, include
from . import views
from .views import SignUpView, ActivateAccount, ProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('acivate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
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
        template_name='passsword-reset/password_reset_complete.html'
    ), name='password_reset_complete'),
]