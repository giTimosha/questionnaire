from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Product, Review


class ReviewCreate(CreateView):
    template_name = 'review/create.html'
    form_class = ReviewForm

    def form_valid(self, form):
        user = self.request.user
        product_pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_pk)
        product.products.create(author=user, **form.cleaned_data)
        return redirect('webapp:view', pk=product_pk)


class ReviewUpdate(UpdateView):
    model = Review
    template_name = 'review/update.html'
    form_class = ReviewForm
    context_object_name = 'object'

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.product.pk})


class ReviewDelete(DeleteView):
    template_name = 'review/delete.html'
    model = Review
    context_object_name = 'object'

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.product.pk})
