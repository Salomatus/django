from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="admin@example.com")
        user.set_password("1234qwe")
        user.is_active(True)
        user.is_staff(True)
        user.is_superuser(True)
        user.save()
