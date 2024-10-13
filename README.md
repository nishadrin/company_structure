# Company structure

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT
## Запуск
### Поднимаем контейнер
```docker-compose up -d```
### Создаем администратора
```docker-compose run --rm django python manage.py createsuperuser```
## URLS
### Админка
```http://127.0.0.1:8000/admin/```
### API
```http://127.0.0.1:8000/api/docs/```
