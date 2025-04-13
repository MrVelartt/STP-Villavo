from rest_framework import serializers
from .models import AppInfo, CaracteristicaApp, Ruta, Parada, RutaParada


class CaracteristicaAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracteristicaApp
        fields = '__all__'


class AppInfoSerializer(serializers.ModelSerializer):
    caracteristicas = CaracteristicaAppSerializer(many=True, required=False)

    class Meta:
        model = AppInfo
        fields = '__all__'

    def create(self, validated_data):
        caracteristicas_data = validated_data.pop('caracteristicas', [])
        app_info = AppInfo.objects.create(**validated_data)
        for caracteristica_data in caracteristicas_data:
            CaracteristicaApp.objects.create(app=app_info, **caracteristica_data)
        return app_info


class ParadaSerializer(serializers.ModelSerializer):
    rutas = serializers.SerializerMethodField()
    lat = serializers.SerializerMethodField()
    lon = serializers.SerializerMethodField()

    class Meta:
        model = Parada
        fields = '__all__'

    def get_rutas(self, obj):
        rutas = RutaParada.objects.filter(parada=obj).select_related('ruta')
        return [
            {
                'id': r.ruta.id,
                'name_route': r.ruta.name_route,
                'color_route': r.ruta.color_route,
                'short_name': r.ruta.short_name,
                'image_route': r.ruta.image_route.url if r.ruta.image_route else None
            }
            for r in rutas
        ]

    def get_lat(self, obj):
        try:
            return float(obj.coordenada.split(',')[0])
        except:
            return None

    def get_lon(self, obj):
        try:
            return float(obj.coordenada.split(',')[1])
        except:
            return None


class RutaParadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutaParada
        fields = ['ruta', 'parada', 'orden_parada']


class RutaSerializer(serializers.ModelSerializer):
    paradas = serializers.SerializerMethodField()

    class Meta:
        model = Ruta
        fields = '__all__'

    def get_paradas(self, obj):
        relaciones = RutaParada.objects.filter(ruta=obj).select_related('parada').order_by('orden_parada')
        resultado = []
        for rel in relaciones:
            parada = rel.parada
            resultado.append({
                'id': parada.id,
                'nombre': parada.nombre,
                'lat': float(parada.coordenada.split(',')[0]) if parada.coordenada else None,
                'lon': float(parada.coordenada.split(',')[1]) if parada.coordenada else None,
                'orden': rel.orden_parada,
                'icono': parada.icono.url if parada.icono else None,
            })
        return resultado

    def create(self, validated_data):
        paradas_data = validated_data.pop('paradas', [])
        ruta = Ruta.objects.create(**validated_data)

        for parada_data in paradas_data:
            RutaParada.objects.create(ruta=ruta, **parada_data)
        return ruta

    def update(self, instance, validated_data):
        paradas_data = validated_data.pop('paradas', [])
        instance.name_route = validated_data.get('name_route', instance.name_route)
        instance.description_route = validated_data.get('description_route', instance.description_route)
        instance.color_route = validated_data.get('color_route', instance.color_route)
        instance.save()

        for parada_data in paradas_data:
            RutaParada.objects.update_or_create(
                ruta=instance,
                parada=parada_data['parada'],
                defaults={'orden_parada': parada_data['orden_parada']}
            )
        return instance
