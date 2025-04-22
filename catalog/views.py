from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def catalog_list(request):
    catalog = Product.objects.all()
    context = {"catalog": catalog}
    return render(request, "catalog_list.html", context)


def catalog_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "catalog_detail.html", context)
