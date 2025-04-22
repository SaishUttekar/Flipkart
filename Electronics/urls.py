from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'Electronics'  # Define the namespace for the Electronics app

urlpatterns = [
    path('register/', views.register, name='register'),  # Add the register view for Electronics
    path('login/', views.login_view, name='login'),  # Add the login view for Electronics
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Use LogoutView for logout with next_page
    
    path('', views.home, name='home'),  # Add the home view for Electronics
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
]




