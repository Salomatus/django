from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blogs_list"),
    path("blog/create", BlogCreateView.as_view(), name="blogs_create"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blogs_detail"),
    path("blog/<int:pk>/update", BlogUpdateView.as_view(), name="blogs_update"),
    path("blog/<int:pk>/delete", BlogDeleteView.as_view(), name="blogs_delete"),
]
