from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_active', 'is_staff', 'username', 'password1', 'password2')
