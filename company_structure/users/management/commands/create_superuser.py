from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(id=1):
            User.objects.create_user(username= 'admin',
                                    email='admin@example.com',
                                    password='Qwerty123',
                                    is_staff=True,
                                    is_active=True,
                                    is_superuser=True
            )
