from django.db import models
from django.utils import timezone
import csv
import io
import re
import requests


class AppInfo(models.Model):
    icono_app = models.ImageField(upload_to='iconos/', null=True, blank=True, verbose_name="Ícono de la App")
    nombre_app = models.CharField(max_length=255, verbose_name="Nombre de la App")
    descripcion_app = models.TextField(verbose_name="Descripción de la App")

    def __str__(self):
        return self.nombre_app

    class Meta:
        verbose_name = "Información de la App"
        verbose_name_plural = "Información de la App"


class CaracteristicaApp(models.Model):
    app = models.ForeignKey(AppInfo, on_delete=models.CASCADE, related_name="caracteristicas", verbose_name="Aplicación", null=True, blank=True)
    icono = models.ImageField(upload_to='iconos/', null=True, blank=True, verbose_name="Ícono de la Característica")
    nombre_caracteristica = models.CharField(max_length=255, verbose_name="Nombre de la Característica")
    descripcion_caracteristica = models.TextField(verbose_name="Descripción de la Característica")

    def __str__(self):
        return f"{self.nombre_caracteristica} ({self.app.nombre_app if self.app else 'Sin App'})"

    class Meta:
        verbose_name_plural = "Características de la App"


class Ruta(models.Model):
    name_route = models.CharField(max_length=255, verbose_name="Nombre de la Ruta", default="Ruta Desconocida")
    short_name = models.CharField(max_length=255, verbose_name="Abreviatura Ruta", null=True)
    description_route = models.TextField(verbose_name="Descripción General", default="Sin descripción")
    color_route = models.CharField(max_length=7, null=True, blank=True, verbose_name="Color (Hex)", default="#000000")
    image_route = models.ImageField(upload_to='rutas/', null=True, blank=True, verbose_name="Imagen de la Ruta")
    distance_route = models.CharField(max_length=100, verbose_name="Distancia de la Ruta", null=True, blank=True, default="0 km")
    time_travel = models.IntegerField(verbose_name="Tiempo Estimado de Viaje (min)", default=0)
    start_time_route = models.TimeField(default=timezone.now, verbose_name="Hora de Inicio")
    end_time_route = models.TimeField(null=True, blank=True, verbose_name="Hora de Finalización")
    frequency = models.IntegerField(verbose_name="Frecuencia (min)", default=0)
    quantity_bus = models.IntegerField(null=True, blank=True, verbose_name="Cantidad de Buses", default=0)
    barrios = models.JSONField(null=True, blank=True, default=dict, verbose_name="Lista de Barrios")
    coordenadas = models.JSONField(null=True, blank=True, default=list, verbose_name="Coordenadas (JSON generado)")
    archivo_csv = models.FileField(upload_to='csvs/', null=True, blank=True, verbose_name="Archivo CSV de Coordenadas")

    def __str__(self):
        return self.name_route

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"

    def extraer_coordenadas_csv(self):
        """
        Procesa el archivo CSV, extrayendo las coordenadas del campo WKT (formato "POINT (lon lat)").
        Retorna una lista de diccionarios con claves 'lat' y 'lon'.
        """
        if not self.archivo_csv:
            return []

        try:
            contenido = ""

            # Intentamos leer como archivo local
            try:
                self.archivo_csv.open('r')
                contenido = self.archivo_csv.read().decode('utf-8')
                self.archivo_csv.close()
            except Exception as e:
                # En caso de usar almacenamiento externo (S3, etc.)
                if hasattr(self.archivo_csv, 'url'):
                    response = requests.get(self.archivo_csv.url)
                    if response.status_code == 200:
                        contenido = response.content.decode('utf-8')
                    else:
                        return []
                else:
                    return []

            reader = csv.reader(io.StringIO(contenido))
            coordenadas_extraidas = []

            for fila in reader:
                if fila and "POINT" in fila[0]:
                    match = re.search(r'POINT\s*\(\s*([-\d\.]+)\s+([-\d\.]+)\s*\)', fila[0])
                    if match:
                        lon = float(match.group(1))
                        lat = float(match.group(2))
                        coordenadas_extraidas.append({'lat': lat, 'lon': lon})

            return coordenadas_extraidas

        except Exception as e:
            print(f"Error procesando CSV: {e}")
            return []
