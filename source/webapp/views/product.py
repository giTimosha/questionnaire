from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class IndexView(ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'product/index.html'


class ProductView(DetailView):
    template_name = 'product/view.html'
    context_key = 'product'
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'product/create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/update.html'
    context_object_name = 'product'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/delete.html'

    def get_success_url(self):
        return reverse('webapp:index')
