from django.urls import path
from . import views

app_name = 'Clothing'  # Ensure this matches the namespace used in reverse()

urlpatterns = [
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
    path('', views.home, name='home'),
]   