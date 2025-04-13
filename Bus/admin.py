# admin.py
from django.contrib import admin
from .models import AppInfo, CaracteristicaApp, Ruta, Parada, RutaParada

# Primero definimos el inline para RutaParada
class RutaParadaInline(admin.TabularInline):
    model = RutaParada
    extra = 1  # Añadir una parada vacía por defecto
    fields = ['parada', 'orden_parada']

# Registramos la clase de administración para AppInfo
@admin.register(AppInfo)
class AppInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_app', 'descripcion_app']
    search_fields = ['nombre_app', 'descripcion_app']
    list_filter = ['nombre_app']

# Registramos la clase de administración para CaracteristicaApp
@admin.register(CaracteristicaApp)
class CaracteristicaAppAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_caracteristica', 'descripcion_caracteristica', 'app']
    search_fields = ['nombre_caracteristica', 'descripcion_caracteristica']
    list_filter = ['app']

# Registramos la clase de administración para Ruta
@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_route', 'description_route', 'get_start_time', 'get_end_time']
    search_fields = ['name_route']
    list_filter = ['name_route']
    inlines = [RutaParadaInline]  # Añadimos la relación de paradas dentro de la vista de Ruta

    def get_start_time(self, obj):
        return obj.start_time_route
    get_start_time.short_description = 'Hora Inicio'

    def get_end_time(self, obj):
        return obj.end_time_route
    get_end_time.short_description = 'Hora Fin'

# Registramos la clase de administración para Parada
@admin.register(Parada)
class ParadaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'coordenada', 'orden', 'get_rutas']
    search_fields = ['nombre', 'coordenada']
    list_filter = ['nombre']

    def get_rutas(self, obj):
        # Usamos el modelo intermedio RutaParada para mostrar las rutas relacionadas
        rutas = RutaParada.objects.filter(parada=obj)
        return ", ".join([ruta.ruta.name_route for ruta in rutas])
    get_rutas.short_description = "Rutas"
