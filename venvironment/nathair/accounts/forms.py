from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, HairProfile

#User Sign Up Form
class SignupForm(forms.Form):
    ''' User Sign up form '''
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=254, required=True, help_text='Please enter a valid email Address', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), required=True)
   

class LoginForm(forms.Form):
    ''' User Login Form '''
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)


#User Profile Form
class ProfileForm(forms.ModelForm):
    ''' User Create/Edit Profile Form '''
    class Meta:
        model = Profile
        fields = [
            'full_name',
            'bio',
            'profile_pic',
            'location',
            'date_of_birth',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Bio'}),
            'profile_pic': forms.FileInput(attrs={'class': 'file-input', 'placeholder': 'Profile Picture'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'date_of_birth': forms.TextInput(attrs={'placeholder': 'Date of Birth'}),
        }


#User Hair Profile Form
class HairProfileForm(forms.ModelForm):
    class Meta:
        model = HairProfile
        fields = (
            'user',
            'hair_type',
            'hair_porosity',
            'hair_condition',
            'hair_length',
        )



