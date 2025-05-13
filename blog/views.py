from django.urls import reverse_lazy, reverse

from .models import Blog
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        # Получаем только активные объекты
        return Blog.objects.filter(publication=True)


class BlogCreateView(CreateView):
    model = Blog
    fields = (
        "title",
        "content",
        "image",
    )
    success_url = reverse_lazy("blog:blogs_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "image")
    success_url = reverse_lazy("blog:blogs_list")

    def get_success_url(self):
        return reverse("blog:blogs_detail", args=[self.kwargs.get("pk")])


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blogs_list")
