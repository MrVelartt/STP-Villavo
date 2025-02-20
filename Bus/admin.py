from django.contrib import admin
from .models import AppInfo, CaracteristicaApp, Ruta, DetalleRuta

admin.site.register(AppInfo)
admin.site.register(CaracteristicaApp)
admin.site.register(Ruta)
admin.site.register(DetalleRuta)