from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, HairProfile

#User Sign Up Form
class SignupForm(forms.Form):
    ''' User Sign up form '''
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=254, required=True, help_text='Please enter a valid email Address', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already taken. Please use a different email or sign in.')
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 =cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError('Passwords do not match')
        
        return cleaned_data

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
            'hair_type',
            'hair_porosity',
            'hair_condition',
            'hair_length',
        )
        widgets = {
            'hair_type': forms.Select(attrs={'placeholder': 'Hair Type'}),
            'hair_porosity': forms.Select(attrs={'placeholder': 'Hair Porosity'}),
            'hair_condition': forms.Select(attrs={'placeholder': 'Hair Condition'}),
            'hair_length': forms.Select(attrs={'placeholder': 'Hair Length'}),
        }



