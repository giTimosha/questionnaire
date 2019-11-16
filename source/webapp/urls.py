from django.urls import path

from webapp.views.product import IndexView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='view'),
    path('product/add', ProductCreateView.as_view(), name='create_view'),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name='update_view'),
    path('task/<int:pk>/delete', ProductDeleteView.as_view(), name='delete_view'),
]

app_name = 'webapp'
