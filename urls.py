from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('electronics/', include('Electronics.urls', namespace='Electronics')),
    path('clothing/', include('Clothing.urls', namespace='Clothing')),
]