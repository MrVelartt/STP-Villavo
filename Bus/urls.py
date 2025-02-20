from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppInfoViewSet, RutaViewSet, DetalleRutaViewSet

router = DefaultRouter()
router.register(r'appinfo', AppInfoViewSet)
router.register(r'rutas', RutaViewSet)
router.register(r'detalle_rutas', DetalleRutaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
