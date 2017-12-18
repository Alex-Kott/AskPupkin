from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='')
    last_name = forms.CharField(max_length=30, required=False, help_text='')
    email = forms.EmailField(max_length=254, help_text='')

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'password1', 'password2']


class SignInForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, help_text='')
    password = forms.CharField(widget=forms.PasswordInput())

    # class Meta:
    #     model = User
    #     fields = ['username', 'password']