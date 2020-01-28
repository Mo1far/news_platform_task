# Generated by Django 3.0 on 2020-01-26 10:16

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0007_auto_20200125_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 26, 10, 16, 50, 74911)),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]