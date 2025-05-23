from catalog.models import Product

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.http import HttpResponseForbidden

from django.shortcuts import get_object_or_404, redirect


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):

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
