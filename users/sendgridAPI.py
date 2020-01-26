import os

from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from users.tokens import account_activation_token


class SendGridAPI:
    @staticmethod
    def send_veritification_mail(user):
        kwargs = {
            'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user=user)
        }
        url = reverse('user:activate', kwargs=kwargs)
        activation_link = f'http://127.0.0.1:8000{url}'
        print(activation_link)
        text = f'Activate account: {activation_link}'
        message = Mail(
            from_email='noreply@test.com',
            to_emails=user.email,
            subject='Активация',
            html_content=text
        )
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        # print(response.status)
#
# user = User.objects.get(id=32)
# SendGridAPI.send_veritification_mail(user=user)
