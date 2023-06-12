from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User

# User Sign Up View.
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#Use Edit Profile View.
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'profile.html'
