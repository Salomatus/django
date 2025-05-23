from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        null=True,
        blank=True,
        help_text="Введите номер " "телефона",
    )
    tg_name = models.CharField(
        max_length=50,
        verbose_name="Ник Телеграм",
        null=True,
        blank=True,
        help_text="Введите ник телеграм",
    )
    avatar = models.ImageField(
        verbose_name="Аватар",
        upload_to="user/avatars/",
        null=True,
        blank=True,
        help_text="Выберите аватар",
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    token = models.CharField(
        max_length=100, verbose_name="Token", null=True, blank=True
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
