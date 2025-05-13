from catalog.models import Product
from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

