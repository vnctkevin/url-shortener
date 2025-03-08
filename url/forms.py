from django import forms
from martor.widgets import AdminMartorWidget
from martor.fields import MartorFormField
from .models import Link, Microsite, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['longUrl', 'shortUrl']
        labels = {
            'longUrl': 'URL to shorten',
            'shortUrl': 'New Short URL'
        }
        widgets = {
            'longUrl': forms.URLInput(attrs={'class': 'form-control'})
        }

class MicrositeForm(forms.ModelForm):
    description = MartorFormField()
    content = MartorFormField()
    class Meta:
        model = Microsite
        fields = ['name', 'description', 'content', 'links']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'links': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth',
            'email' : 'Email Address',
            'phone_number': 'Phone Number'
        }

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=150)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number', 'password1', 'password2']