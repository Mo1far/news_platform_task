from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class News(models.Model):
    class NewsStatus(models.TextChoices):
        UNPUBLISHED = 'unpublished', _('unpublished')
        PUBLISHED = 'published', _('published')
        WAITING_CONFIRMATION = 'waiting_confirmation', _('waiting_confirmation')

    class Meta:
        permissions = [
            ('publish', 'can_publish_without_moderation')
        ]
        verbose_name = 'news'
        verbose_name_plural = 'news'

    title = models.CharField(max_length=30, verbose_name='Title', help_text='Use short roomy title')
    content = RichTextField(verbose_name='News content', help_text='Insert your news here')
    posted_date = models.DateTimeField(auto_now_add=True, verbose_name='Posted date', help_text='Date of posted')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', help_text='Link to author')
    status = models.CharField(
        max_length=20,
        choices=NewsStatus.choices,
        default=NewsStatus.WAITING_CONFIRMATION,
        verbose_name='Confirmation status',
        help_text='This is status of news publication'
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=100, verbose_name='Content', help_text='Comment text')
    posted_date = models.DateTimeField(auto_now_add=True, verbose_name='Posted date', help_text='Date of posted')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', help_text='Link to author')
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='News', help_text='Link to news')
