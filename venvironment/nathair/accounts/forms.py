from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import HairProfile

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

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

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



