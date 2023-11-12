from django.contrib.auth.models import AbstractUser
from azu_bot_django.settings import PERMISSIONS_LIST
from django.contrib.auth.models import Permission


from django.db import models
from cafes.models import Cafe


class CustomUser(AbstractUser):
    is_staff = models.BooleanField(
        "staff status",
        default=True,
        help_text="Designates whether the user can log into this admin site.",
    )
    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        verbose_name='В кафе',
        blank=True,
        null=True,
        help_text="Для сотрудников кафе обязателен выбор к привязанному кафе",
    )

    def __str__(self):
        return self.username

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        """
        Автоматическое добавление прав доступа при создании
        """
        super().save(force_insert, force_update, *args, **kwargs)
        if self.is_staff:
            for permission_codename in PERMISSIONS_LIST:
                permission = Permission.objects.get(
                    codename=permission_codename)
                self.user_permissions.add(permission)