import django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True,
                              verbose_name='Email', help_text='User email')

    first_name = models.CharField(max_length=254, null=True,
                                  blank=True, verbose_name='First name',
                                  help_text='User first name')

    last_name = models.CharField(max_length=254, null=True,
                                 blank=True, verbose_name='Last name',
                                 help_text='User last name')

    birth_date = models.DateField(default=django.utils.timezone.now,
                                  verbose_name='Birth date',
                                  help_text='User birth date')

    last_login = models.DateTimeField(null=True, blank=True,
                                      verbose_name='Last login',
                                      help_text='User last login date')

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
