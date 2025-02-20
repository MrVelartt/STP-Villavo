from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bus/', include('Bus.urls')),  # Asegúrate de que 'bus.urls' exista o reemplázalo por el nombre de tu app
]