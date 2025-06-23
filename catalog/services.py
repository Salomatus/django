from catalog.models import Product
from django.core.cache import cache
from config.settings import CACHE_ENABLED



def get_catalog_from_cache():
    """Получаем данные из кэша, если кэш пустой, то заполняем его данными из БД"""

    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'catalog_list'
    catalog = cache.get(key)
    if catalog is not None:
        return catalog
    catalog = Product.objects.all()
    cache.set(key, catalog)
    return catalog
