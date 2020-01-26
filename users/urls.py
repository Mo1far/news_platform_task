from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import SignUp, LoginView, EmailConfirmationRequests, ActivateView, EmailConfirmationSuccessful

app_name = 'user'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('email_confirmation_request/', EmailConfirmationRequests.as_view(), name='email_confirmation_request'),
    path('email_confirmation_successful/', EmailConfirmationSuccessful.as_view(), name='email_confirmation_successful'),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name='activate'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
