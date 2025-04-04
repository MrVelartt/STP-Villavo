from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# from rest_framework.permissions import IsAuthenticated

from .models import AppInfo, Ruta
from .serializers import AppInfoSerializer, RutaSerializer


class AppInfoListAPIView(APIView):
    # permission_classes = [IsAuthenticated]  # Opcional para proteger la vista

#   @method_decorator(cache_page(60 * 15))  # Cache de 15 minutos
    def get(self, request):
        apps = AppInfo.objects.prefetch_related('caracteristicas').all()
        serializer = AppInfoSerializer(apps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RutaListAPIView(APIView):
    def get(self, request):
        rutas = Ruta.objects.all()
        serializer = RutaSerializer(rutas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RutaSerializer(data=request.data)
        if serializer.is_valid():
            ruta = serializer.save()  # Aquí se activa el save() del modelo con coordenadas
            return Response(RutaSerializer(ruta).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)