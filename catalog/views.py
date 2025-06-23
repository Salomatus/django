import catalog.forms
import catalog.services
from catalog.models import Product

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm, ProductModeratorForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.http import HttpResponseForbidden

from django.shortcuts import get_object_or_404, redirect
from catalog.services import get_catalog_from_cache


class ProductListView(ListView):
    model = Product

def get_queryset(self):
    return get_catalog_from_cache()

class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.view_count += 1
            self.object.save()
        return self.object
        raise PermissionDenied


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_edit") and user.has_perm(
            "catalog.can_edit_description"
        ):
            return ProductModeratorForm
        raise PermissionDenied("У вас нет прав на редактирование этого продукта.")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        return reverse("catalog:product", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")

    permission_required = "catalog.delete_product"


class UnpublishProductView(LoginRequiredMixin):

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden(
                "У вас недостаточно прав для снятия продукта с публикации"
            )

        product.is_published = False
        product.save()

        return redirect("catalog:product", pk=product.id)


class ProductCategoryListView(ListView):
    model = Product
    template_name = "catalog/products_list_by_category.html"
    context_object_name = "category"
