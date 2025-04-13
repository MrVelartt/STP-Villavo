from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import AppInfo, CaracteristicaApp, Ruta, Parada, RutaParada

# Inline para RutaParada
class RutaParadaInline(admin.TabularInline):
    model = RutaParada
    extra = 1  # Añade una parada vacía por defecto
    fields = ['parada', 'orden_parada']

@admin.register(AppInfo)
class AppInfoAdmin(VersionAdmin):  # Usamos VersionAdmin para versionar
    list_display = ['id', 'nombre_app', 'descripcion_app']
    search_fields = ['nombre_app', 'descripcion_app']
    list_filter = ['nombre_app']

@admin.register(CaracteristicaApp)
class CaracteristicaAppAdmin(VersionAdmin):
    list_display = ['id', 'nombre_caracteristica', 'descripcion_caracteristica', 'app']
    search_fields = ['nombre_caracteristica', 'descripcion_caracteristica']
    list_filter = ['app']

@admin.register(Ruta)
class RutaAdmin(VersionAdmin):
    list_display = ['id', 'name_route', 'description_route', 'get_start_time', 'get_end_time']
    search_fields = ['name_route']
    list_filter = ['name_route']
    inlines = [RutaParadaInline]  # Incluye la relación de paradas en la vista de Ruta

    def get_start_time(self, obj):
        return obj.start_time_route
    get_start_time.short_description = 'Hora Inicio'

    def get_end_time(self, obj):
        return obj.end_time_route
    get_end_time.short_description = 'Hora Fin'

@admin.register(Parada)
class ParadaAdmin(VersionAdmin):
    list_display = ['id', 'nombre', 'coordenada', 'orden', 'get_rutas']
    search_fields = ['nombre', 'coordenada']
    list_filter = ['nombre']

    def get_rutas(self, obj):
        # Se usa el modelo intermedio RutaParada para listar las rutas asociadas a la parada
        rutas = RutaParada.objects.filter(parada=obj)
        return ", ".join([ruta.ruta.name_route for ruta in rutas])
    get_rutas.short_description = "Rutas"
