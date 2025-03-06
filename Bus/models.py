from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from PIL import Image

class CaracteristicaApp(models.Model):
    icono = models.ImageField(upload_to='iconos/', null=True, blank=True, verbose_name="Ícono")
    nombre_caracteristica = models.CharField(max_length=255, verbose_name="Nombre de la característica")
    descripcion_caracteristica = models.TextField(verbose_name="Descripción de la característica")

    def __str__(self):
        return self.nombre_caracteristica

    class Meta:
        verbose_name = "Característica de la App"
        verbose_name_plural = "Características de la App"

class AppInfo(models.Model):
    icono_app = models.ImageField(upload_to='iconos/', null=True, blank=True, verbose_name="Ícono de la App")
    nombre_app = models.CharField(max_length=255, verbose_name="Nombre de la App")
    descripcion_app = models.TextField(verbose_name="Descripción de la App")
    caracteristicas_app = models.ManyToManyField(CaracteristicaApp, verbose_name="Características de la App")

    def __str__(self):
        return self.nombre_app

    class Meta:
        verbose_name = "Información de la App"
        verbose_name_plural = "Información de la App"

class Ruta(models.Model):
    name_route = models.CharField(max_length=255, verbose_name="Nombre de la Ruta")
    frequency_route = models.IntegerField(verbose_name="Frecuencia de la Ruta (min)")
    description_route = models.TextField(verbose_name="Descripción de la Ruta")
    color_route = models.CharField(max_length=7, verbose_name="Color de la Ruta (Hexadecimal)")

    def __str__(self):
        return self.name_route

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"

class DetalleRuta(models.Model):
    image_route = models.ImageField(upload_to='rutas/', null=True, blank=True, verbose_name="Imagen de la Ruta")
    name_route = models.CharField(max_length=255, verbose_name="Nombre de la Ruta")
    distance_route = models.CharField(max_length=100, verbose_name="Distancia de la Ruta")
    time_travel = models.IntegerField(verbose_name="Tiempo Estimado de Viaje (min)")
    start_time_route = models.DateTimeField(default=timezone.now, verbose_name="Hora de Inicio")
    end_time_route = models.DateTimeField(verbose_name="Hora de Finalización")
    frequency = models.IntegerField(verbose_name="Frecuencia (min)")
    quantity_bus = models.IntegerField(verbose_name="Cantidad de Buses en la Ruta")
    description_route = models.TextField(verbose_name="Descripción Detallada")
    barrios = models.JSONField(null=True, blank=True,verbose_name="Lista de Barrios en la Ruta")

    def __str__(self):
        return f"{self.name_route} - {self.distance_route}"

    class Meta:
        verbose_name = "Detalle de Ruta"
        verbose_name_plural = "Detalles de Rutas"