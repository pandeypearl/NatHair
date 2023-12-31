"""
    Module for account views.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profile, Follow, HairProfile, TextureProfile
from routines.models import HairRoutine
from products.models import HairProduct
from .forms import LoginForm, SignupForm, ProfileForm, HairProfileForm, TextureProfileForm


# Landing Page
login_required(login_url='login')
def home(request):
    template = 'home.html'
    products = HairProduct.objects.all()
    routines = HairRoutine.objects.filter(is_draft=False)

    context = {
        'products': products,
        'routines': routines,
    }

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
                   
            #create profile objects for the new user
            user_model = User.objects.get(username=username)

            new_profile = Profile.objects.create(user=user_model)
            new_profile.save()

            new_hair_profile = HairProfile.objects.create(user=user_model)
            new_hair_profile.save()

            new_texture_profile = TextureProfile.objects.create(user=user_model)
            new_texture_profile.save()

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
    ''' User profile view '''
    template = 'profile.html'

    user_object = get_object_or_404(User, pk=pk)
    user_profile = Profile.objects.get(user=user_object)
    hair_profile = HairProfile.objects.get(user=user_object)
    texture_profile = TextureProfile.objects.get(user=user_object)
    
    if request.user == user_object:
        hair_routines = HairRoutine.objects.filter(user=user_object)
    else:
        hair_routines = HairRoutine.objects.filter(user=user_object, is_draft=False)

    followers = user_object.followers.all()
    following = user_object.following.all()
    is_following = Follow.objects.filter(follower=request.user, followed=user_object).exists()
    follower_count = user_object.followers.count()
    following_count = user_object.following.count()

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'hair_profile': hair_profile,
        'texture_profile': texture_profile,
        'hair_routines': hair_routines,
        'followers': followers,
        'following': following,
        'is_following': is_following,
        'follower_count': follower_count,
        'following_count': following_count,
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

@login_required(login_url='login')
def hair_profile(request):
    ''' User hair profile view '''
    template = 'hair_profile.html'

    user = request.user

    hair_profile, created = HairProfile.objects.get_or_create(user=request.user)

    form = HairProfileForm(request.POST)

    if request.method == 'POST':
        form = HairProfileForm(request.POST, instance=hair_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hair profile updated successfully.')
            return redirect('profile', pk=user.pk)
        else:
            messages.warning(request, 'Something went wrong. Please try again.')
    else:
        form = HairProfileForm(instance=hair_profile)

    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required(login_url='login')
def texture_profile(request):
    ''' User texture profile view. '''
    template = 'texture_profile.html'

    user  = request.user

    texture_profile, created = TextureProfile.objects.get_or_create(user=request.user)

    form = TextureProfileForm(instance=texture_profile)
    if request.method == 'POST':
        form = TextureProfileForm(request.POST, request.FILES, instance=texture_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Texture profile updated successfully.')
            return redirect('profile', pk=user.pk)
        else:
            messages.warning(request, 'Something went wrong. Please try again')
    else:
        form = TextureProfileForm(instance=texture_profile)

    context = {
        'form': form,
    }

    return render(request, template, context)
    

@login_required(login_url='login')
def follow(request, pk):
    if request.method == 'POST':
        user_to_follow = get_object_or_404(User, pk=pk).profile.user

        # Checking if the user is not trying to follow themselves
        if request.user == user_to_follow:
            return redirect('profile', pk=pk)
         # Check if the user is already a follower
        if not Follow.objects.filter(follower=request.user, followed=user_to_follow).exists():
            Follow.objects.create(follower=request.user, followed=user_to_follow)

    return redirect('profile', pk=pk)


@login_required(login_url='login')
def unfollow(request, pk):
    if request.method == 'POST':
        user_to_unfollow = get_object_or_404(User, pk=pk).profile.user
        
        # Checking if the user is a follower before unfollowing
        follow_instance = Follow.objects.filter(follower=request.user, followed=user_to_unfollow).first()
        if follow_instance:
            follow_instance.delete()

    return redirect('profile', pk=pk)


@login_required(login_url='login')
def followers(request, pk):
    template = 'followers.html'
    user = get_object_or_404(User, pk=pk)
    followers = user.followers.all()

    context = {
        'user': user,
        'followers': followers,
    }
    return render(request, template, context)


@login_required(login_url='login')
def following(request, pk):
    template = 'following.html'
    user = get_object_or_404(User, pk=pk)
    following = user.following.all()

    context = {
        'user': user,
        'following': following,
    }
    return render(request, template, context)


@login_required(login_url='login')
def search(request):
    template = 'search.html'
    query = request.GET.get('q', '')

    user_results = User.objects.filter(username__icontains=query)
    routine_results = HairRoutine.objects.filter(is_draft=False, name__icontains=query)
    product_results = HairProduct.objects.filter(title__icontains=query)

    results = []

    for result in user_results:
        try:
            profile = Profile.objects.get(user=result)
            result.profile = profile
            result.model_name = "User"
            results.append(result)
        except Profile.DoesNotExist:
            result.profile = None 
            results.append(result)

    for result in routine_results:
        result.model_name = "HairRoutine"
        results.append(result)

    for result in product_results:
        result.model_name = "HairProduct"
        results.append(result)

    context = {
        'query': query,
        'results': results
    }

    return render(request, template, context)