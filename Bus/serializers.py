from rest_framework import serializers
from .models import AppInfo, CaracteristicaApp, Ruta


class CaracteristicaAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracteristicaApp
        fields = ['id', 'icono', 'nombre_caracteristica', 'descripcion_caracteristica']


class AppInfoSerializer(serializers.ModelSerializer):
    caracteristicas = CaracteristicaAppSerializer(many=True, required=False)

    class Meta:
        model = AppInfo
        fields = ['id', 'icono_app', 'nombre_app', 'descripcion_app', 'caracteristicas']

    def create(self, validated_data):
        caracteristicas_data = validated_data.pop('caracteristicas', [])
        app_info = AppInfo.objects.create(**validated_data)
        for caracteristica_data in caracteristicas_data:
            CaracteristicaApp.objects.create(app=app_info, **caracteristica_data)
        return app_info



class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'
