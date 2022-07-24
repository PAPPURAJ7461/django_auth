from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Accounts
from django import forms

class RegisterForm(UserCreationForm):

    class Meta:
        model= Accounts
        fields = ['first_name','last_name','email','mobile']
        labels={'email':'Email'}

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')
