from django.contrib.auth import views
from django.views.generic import CreateView

from .forms import LoginForm
from .forms import SignUpForm
from .models import User


class SignUp(CreateView):
    model = User
    template_name = 'users/login.html'
    form_class = SignUpForm
    success_url = '/news/'


class LoginView(views.LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class LogoutView(views.LogoutView):
    success_url = '/'
