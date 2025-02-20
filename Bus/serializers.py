from rest_framework import serializers
from .models import AppInfo, CaracteristicaApp, Ruta, DetalleRuta

class CaracteristicaAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracteristicaApp
        fields = '__all__'

class AppInfoSerializer(serializers.ModelSerializer):
    caracteristicas_app = CaracteristicaAppSerializer(many=True)

    class Meta:
        model = AppInfo
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'

class DetalleRutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleRuta
        fields = '__all__'
