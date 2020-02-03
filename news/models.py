from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class News(models.Model):
    class NEWS_STATUS:
        UNPUBLISHED = 'unpublished'
        PUBLISHED = 'published'
        WAITING_CONFIRMATION = 'waiting_confirmation'
        STATUS_CHOICES = [
            (UNPUBLISHED, _('unpublished')),
            (PUBLISHED, _('published')),
            (WAITING_CONFIRMATION, _('waiting_confirmation')),
        ]

    class Meta:
        permissions = [
            ('publish', 'can_publish_without_moderation')
        ]
        verbose_name = 'news'
        verbose_name_plural = 'news'

    title = models.CharField(max_length=30)
    content = RichTextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=NEWS_STATUS.STATUS_CHOICES,
        default='WAITING_CONFIRMATION'
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
