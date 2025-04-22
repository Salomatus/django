from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import catalog_list, catalog_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", catalog_list, name="catalog_list"),
    path("product/<int:pk>/", catalog_detail, name="catalog_detail"),
]
