from django.contrib.auth import views
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView

from .forms import LoginForm
from .forms import SignUpForm
from .models import User
from .sendgridAPI import SendGridAPI, account_activation_token


class SignUp(CreateView):
    model = User
    template_name = 'users/login.html'
    form_class = SignUpForm
    success_url = '/user/email_confirmation_request/'

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        user = form.save()
        SendGridAPI.send_veritification_mail(user)
        return valid


class EmailConfirmationRequests(TemplateView):
    template_name = 'users/activation_request.html'


class EmailConfirmationSuccessful(TemplateView):
    template_name = 'users/activation_successful.html'


class ActivateView(TemplateView):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=uid)
        except(TypeError, ValueError):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect(reverse('user:email_confirmation_successful'))
        else:
            return HttpResponse('Invalid Token')


class LoginView(views.LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class LogoutView(views.LogoutView):
    success_url = '/'
