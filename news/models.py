from ckeditor.fields import RichTextField
from django.db import models

from users.models import User


class News(models.Model):
    STATUS_CHOICES = [
        ('WAITING_CONFIRMATION', 'waiting_confirmation'),
        ('PUBLISHED', 'published'),
        ('UNPUBLISHED', 'unpublished'),
    ]

    class Meta:
        permissions = [
            ('publish', 'can_publish_without_moderation')
        ]

    title = models.CharField(max_length=30)
    content = RichTextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='WAITING_CONFIRMATION'
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
