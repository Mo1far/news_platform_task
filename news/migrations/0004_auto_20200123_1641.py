# Generated by Django 3.0 on 2020-01-23 16:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0003_news_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': [('publish', 'can_publish_without_moderation')]},
        ),
    ]