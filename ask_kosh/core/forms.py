from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ask_kosh.models import Question


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='',
                                 widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=30, required=False, help_text='',
                                widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(max_length=254, help_text='',
                            widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'first_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'password1': forms.PasswordInput(attrs={'class': "form-control"}),
            'password2': forms.PasswordInput(attrs={'class': "form-control"})
        }


class SignInForm(forms.Form):
    username = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))


class NewQuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=150, label="Title",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control", 'rows': '4', 'cols': '10'}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Question
        fields = ['title', 'text', 'tags']
