from rest_framework import viewsets
from .models import AppInfo, CaracteristicaApp, Ruta, DetalleRuta
from .serializers import AppInfoSerializer, CaracteristicaAppSerializer, RutaSerializer, DetalleRutaSerializer

class AppInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """API para obtener información de la aplicación"""
    queryset = AppInfo.objects.all()
    serializer_class = AppInfoSerializer

class CaracteristicaAppViewSet(viewsets.ReadOnlyModelViewSet):
    """API para obtener las características de la aplicación"""
    queryset = CaracteristicaApp.objects.all()
    serializer_class = CaracteristicaAppSerializer

class RutaViewSet(viewsets.ReadOnlyModelViewSet):
    """API para obtener las rutas disponibles"""
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

class DetalleRutaViewSet(viewsets.ReadOnlyModelViewSet):
    """API para obtener los detalles de las rutas"""
    queryset = DetalleRuta.objects.all()
    serializer_class = DetalleRutaSerializer
