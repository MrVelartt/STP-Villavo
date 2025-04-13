from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AppInfo, Ruta, Parada, RutaParada
from .serializers import AppInfoSerializer, RutaSerializer, ParadaSerializer, RutaParadaSerializer


class AppInfoListAPIView(APIView):
    def get(self, request):
        apps = AppInfo.objects.prefetch_related('caracteristicas').all()
        serializer = AppInfoSerializer(apps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RutaListAPIView(APIView):
    def get(self, request):
        rutas = Ruta.objects.prefetch_related('rutaparada_set__parada').all()
        serializer = RutaSerializer(rutas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RutaSerializer(data=request.data)
        if serializer.is_valid():
            ruta = serializer.save()
            return Response(RutaSerializer(ruta).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RutaDetailAPIView(APIView):
    def get(self, request, id):
        try:
            ruta = Ruta.objects.prefetch_related('rutaparada_set__parada').get(id=id)
        except Ruta.DoesNotExist:
            return Response({'detail': 'Ruta no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RutaSerializer(ruta)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ParadaListAPIView(APIView):
    def get(self, request):
        ruta_id = request.query_params.get('ruta_id')
        if ruta_id:
            paradas = Parada.objects.filter(rutaparada__ruta__id=ruta_id).distinct()
        else:
            paradas = Parada.objects.all()

        paradas = paradas.prefetch_related('rutaparada_set__ruta')
        serializer = ParadaSerializer(paradas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ParadaDetailAPIView(APIView):
    def get(self, request, id):
        try:
            parada = Parada.objects.prefetch_related('rutaparada_set__ruta').get(id=id)
        except Parada.DoesNotExist:
            return Response({'detail': 'Parada no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ParadaSerializer(parada)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RutaParadaListAPIView(APIView):
    def get(self, request):
        ruta_id = request.query_params.get('ruta_id')
        parada_id = request.query_params.get('parada_id')

        if ruta_id and parada_id:
            ruta_paradas = RutaParada.objects.filter(ruta__id=ruta_id, parada__id=parada_id)
        elif ruta_id:
            ruta_paradas = RutaParada.objects.filter(ruta__id=ruta_id)
        elif parada_id:
            ruta_paradas = RutaParada.objects.filter(parada__id=parada_id)
        else:
            ruta_paradas = RutaParada.objects.all()

        serializer = RutaParadaSerializer(ruta_paradas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RutaParadaSerializer(data=request.data)
        if serializer.is_valid():
            ruta_parada = serializer.save()
            return Response(RutaParadaSerializer(ruta_parada).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
