import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "company_structure.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import company_structure.users.signals  # noqa: F401
