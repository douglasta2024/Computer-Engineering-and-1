from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django import forms

class CreateUserForm(UserCreationForm): #Creates the form to receive data from user input on the login page
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UploadForm(ModelForm): #Creates the form to receive data from user input on the Physical Data Input page
    days = forms.IntegerField()
    miles = forms.IntegerField()
    class Meta:
        model = Post
        fields = ['days', 'miles']