from django.urls import path

from webapp.views.product import IndexView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView
from webapp.views.review import ReviewCreate, ReviewUpdate, ReviewDelete

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='view'),
    path('product/add/', ProductCreateView.as_view(), name='create_view'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='update_view'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_view'),
    path('product/<int:pk>/add-review/', ReviewCreate.as_view(), name='review_create'),
    path('review/<int:pk>/edit/', ReviewUpdate.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDelete.as_view(), name='review_delete'),
]

app_name = 'webapp'
