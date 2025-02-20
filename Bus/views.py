from rest_framework import viewsets
from .models import AppInfo, Ruta, DetalleRuta
from .serializers import AppInfoSerializer, RutaSerializer, DetalleRutaSerializer

class AppInfoViewSet(viewsets.ModelViewSet):
    queryset = AppInfo.objects.all()
    serializer_class = AppInfoSerializer

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

class DetalleRutaViewSet(viewsets.ModelViewSet):
    queryset = DetalleRuta.objects.all()
    serializer_class = DetalleRutaSerializer
