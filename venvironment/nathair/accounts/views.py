"""
    Module for account views.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, HairProfile


# Landing Page
login_required(login_url='login')
def home(request):
    template = 'home.html'

    context = {}

    return render(request, template, context)



def signup(request):
    
    if request.method == 'POST':
        username = username.POST['username']
        email = email.POST['email']
        password = password.POST['password']
        password2 = password2.POST['password2']

        if password == password2:
            if User.object.filter(email=email).exists():
                messages.warning(request, 'Email Already Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.waring(request, 'Username unavailable')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #login user and redirect to settings page
                user_login = auth.authenticate.get(username=username)
                auth.login(request, user_login)

                #create profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = UserProfile.objects.create(user=user_model, id_user=user.id)
                new_profile.save()
        else:
            messages.warning(request, 'Passwords do not match')
            return redirect(signup)
    else:
        return render(request, 'signup')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Incorrect email or password')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


def profile(request, pk):
    template = 'profile.html'

    user_object = User.objects.get(username=pk)
    user_profile = UserProfile.objects.get(user=user_object)
    hair_profile = HairProfile.objects.get(user=user_object)

    user = pk

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'hair_profile': hair_profile,
    }

    return render(request, context, template)

