from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Удаляет всё, затем добавляет тестовые продукты"

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Product.objects.all().delete()

        self.stdout.write(self.style.WARNING("Все продукты и категории были удалены."))

        Category = [
            {
                "name": "tablet",
                "description": "Мобильный и удобный",
                "Product": Product,
            },
            {
                "name": "notebook",
                "description": "мобильный и удобный",
                "Product": Product,
            },
        ]

        Product.objects.create(
            name="Nokia", category="tablet", date="2024-09-09", price=19000
        )

        Product.objects.create(
            name="Msi",
            category="notebook",
            date="2024-07-09",
            price=24000,
        )

        for category_data in Category:
            category, create = Category.objects.get_or_create(**category_data)
            if create:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Категория  была успешно создана:{category.name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(f"Категория уже существует: {category.name}")
                )
