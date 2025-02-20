from django.db import models

class CaracteristicaApp(models.Model):
    icono = models.CharField(max_length=255)
    nombre_caracteristica = models.CharField(max_length=255)
    descripcion_caracteristica = models.TextField()

class AppInfo(models.Model):
    icono_app = models.CharField(max_length=255)
    nombre_app = models.CharField(max_length=255)
    descripcion_app = models.TextField()
    caracteristicas_app = models.ManyToManyField(CaracteristicaApp)

class Ruta(models.Model):
    name_route = models.CharField(max_length=255)
    frequency_route = models.IntegerField()
    description_route = models.TextField()
    color_route = models.CharField(max_length=7)  # Código hexadecimal

class DetalleRuta(models.Model):
    image_route = models.CharField(max_length=255)
    name_route = models.CharField(max_length=255)
    distance_route = models.CharField(max_length=100)
    time_travel = models.IntegerField()
    start_time_route = models.DateTimeField()
    end_time_route = models.DateTimeField()
    frequency = models.IntegerField()
    quantity_bus = models.IntegerField()
    description_route = models.TextField()
    barrios = models.JSONField()  # Lista de nombres de barrios