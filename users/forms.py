from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User
from .widgets import DatePicker


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(widget=DatePicker(format='%Y-%m-%d'),
                                 input_formats=('%Y-%m-%d',),
                                 required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'birth_date')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'example@gmail.com', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
    ))
