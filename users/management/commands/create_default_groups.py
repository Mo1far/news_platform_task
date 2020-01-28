"""
Create default permission groups (Users, Redactors, Admins)
"""
import logging

from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.core.management.base import BaseCommand

PERMISSION_GROUPS = [
    ('users', []),
    ('redactors', ['publish']),
    ('admins', [
        'add_news', 'change_news',
        'delete_news', 'view_news',
        'add_comment', 'change_comment',
        'delete_comment', 'view_comment',
        'publish'
    ])
]


class Command(BaseCommand):
    help = 'Creates the necessary groups with the appropriate permissions'

    def handle(self, *args, **options):
        for group, permissions in PERMISSION_GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)
            for codename in permissions:
                try:
                    permission = Permission.objects.get(codename=codename)
                except Permission.DoesNotExist:
                    logging.warning(f"Permission {codename} not found")
                    continue
                new_group.permissions.add(permission)
