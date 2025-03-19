from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование производителя",
        help_text="Укажите производителя",
    )
    description = models.TextField(
        verbose_name="Описание производителя",
        help_text="Укажите описание производителя",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование модели",
        help_text="Укажите модель",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Производитель",
        help_text="Укажите производителя",
        blank=True,
        null=True,
        related_name="catalog",
    )
    foto = models.ImageField(
        upload_to="catalog/foto",
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

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name
