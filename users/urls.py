from django.contrib.auth.views import LogoutView
from django.urls import path

from .forms import LoginForm
from .views import SignUp, LoginView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html', form_class=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
