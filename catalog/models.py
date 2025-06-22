from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Укажите наименование",
    )
    description = models.CharField(
        max_length=150,
        verbose_name="Описание",
        help_text="Описание",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name} {self.description}"


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Модель",
        help_text="Укажите модель",
    )
    description = models.CharField(
        max_length=150,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Продукт",
        blank=True,
        null=True,
        related_name="products",
    )

    foto = models.ImageField(
        upload_to="blog/foto",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )

    date = models.DateField(
        verbose_name="Дата выпуска",
        help_text="Укажите дату выпуска",
        blank=True,
        null=True,
    )

    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Стоимость"
    )

    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения", auto_now=True
    )

    owner = models.ForeignKey(
        User,
        verbose_name="Производитель",
        help_text="Укажите производителя",
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
        permissions = [
            ("can_edit", "can edit"),
            ("can_edit_description", "can edit description"),
        ]

    def __str__(self):
        return self.name
