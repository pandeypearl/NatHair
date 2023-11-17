"""
    Module for account views.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profile, HairProfile
from .forms import LoginForm, SignupForm, ProfileForm


# Landing Page
login_required(login_url='login')
def home(request):
    template = 'home.html'

    context = {}

    return render(request, template, context)



def signup(request):
    ''' User sign up view '''
    template = 'signup.html'
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password != password2:
                messages.warning(request, 'Passwords do not match.')
                return redirect('signup')

            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email Already Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.waring(request, 'Username unavailable')
                return redirect('signup')
                
            user = User.objects.create_user(username=username, email=email, password=password)
            user_login = authenticate(request, username=username, password=password)   
            auth.login(request, user_login)  
                   
            #create profile object for the new user
            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model)
            new_profile.save()

            return redirect('/')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    
    return render(request, template, context)


def login(request):
    ''' User login view '''
    template = 'login.html'
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Invalid username or password. Please use the correct credentials and try again.")
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required(login_url='login')
def logout(request):
    ''' User log out view '''
    auth.logout(request)
    return redirect('login')


def profile(request, pk):
    template = 'profile.html'

    user_object = get_object_or_404(User, pk=pk)
    user_profile = Profile.objects.get(user=user_object)
    # hair_profile = HairProfile.objects.get(user=user_object)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        # 'hair_profile': hair_profile,
    }

    return render(request, template, context)

@login_required(login_url='login')
def update_profile(request):
    ''' User edit profile view '''
    template = 'edit_profile.html'

    user = request.user

    profile, created = Profile.objects.get_or_create(user=request.user)

    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile', pk=user.pk)
        else:
            messages.warning(request, 'Something went wrong, please try again')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, template, context)
