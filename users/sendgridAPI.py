import os

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from users.tokens import account_activation_token


class SendGridAPI:

    @staticmethod
    def send_verification_mail(user, scheme, domain):
        kwargs = {
            'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user=user)
        }
        url = reverse('user:activate', kwargs=kwargs)
        activation_link = f'{scheme}://{domain}{url}'
        text = f'Activate account: {activation_link}'
        message = Mail(
            from_email='noreply@test.com',
            to_emails=user.email,
            subject='Активация',
            html_content=text
        )
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)

    @staticmethod
    def send_new_comment_notification_mail(user, comment, request):
        print('qqq', user.email, reverse('news:detail', kwargs={'pk': comment.post.id}))
        link = f"{request.scheme}://{get_current_site(request).domain}{reverse('news:detail', kwargs={'pk': comment.post.id})}"
        text = f'''New comment on your news {link}'''
        print(text)
        message = Mail(
            from_email='noreply@test.com',
            to_emails=user.email,
            subject='New comment on your news',
            html_content=text
        )
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
