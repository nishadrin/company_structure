from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User=get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(f'Запущен Command BaseCommand')
        if not User.objects.filter(id=1):
            username = 'admin'
            email = 'admin@example.com'
            password = 'Qwerty123'
            User.objects.create_user(username=username,
                                    email=email,
                                    password=password,
                                    is_staff=True,
                                    is_active=True,
                                    is_superuser=True
            )
            print(f'Создан пользователь с ником {username}')
