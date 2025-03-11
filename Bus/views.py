from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import AppInfo, CaracteristicaApp, Ruta, DetalleRuta
from .serializers import AppInfoSerializer, CaracteristicaAppSerializer, RutaSerializer, DetalleRutaSerializer

class AppInfoViewSet(viewsets.ModelViewSet): 
    """API para obtener información de la aplicación"""
    queryset = AppInfo.objects.all()
    serializer_class = AppInfoSerializer
    permission_classes = [IsAuthenticated]  # Requiere autenticación

class CaracteristicaAppViewSet(viewsets.ModelViewSet): 
    """API para obtener las características de la aplicación"""
    queryset = CaracteristicaApp.objects.all()
    serializer_class = CaracteristicaAppSerializer
    permission_classes = [IsAuthenticated]  # Requiere autenticación

class RutaViewSet(viewsets.ModelViewSet): 
    """API para obtener las rutas disponibles"""
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    permission_classes = [IsAuthenticated]  # Requiere autenticación

class DetalleRutaViewSet(viewsets.ReadOnlyModelViewSet):
    """API para obtener detalles de las rutas y permitir login"""
    queryset = DetalleRuta.objects.all()
    serializer_class = DetalleRutaSerializer
    #permission_classes = [IsAuthenticated]

