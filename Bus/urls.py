from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppInfoViewSet, CaracteristicaAppViewSet, RutaViewSet, DetalleRutaViewSet

router = DefaultRouter()
router.register(r'app-info', AppInfoViewSet)
router.register(r'caracteristicas', CaracteristicaAppViewSet)
router.register(r'rutas', RutaViewSet)
router.register(r'detalle-rutas', DetalleRutaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]