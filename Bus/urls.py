from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    AppInfoViewSet, 
    CaracteristicaAppViewSet, 
    RutaViewSet, 
    DetalleRutaViewSet
)

# Configuración del enrutador para las vistas basadas en ViewSets
router = DefaultRouter()
router.register(r'app-info', AppInfoViewSet, basename="app-info")
router.register(r'caracteristicas', CaracteristicaAppViewSet, basename="caracteristicas")
router.register(r'rutas', RutaViewSet, basename="rutas")
router.register(r'detalle-rutas', DetalleRutaViewSet, basename="detalle-rutas")

urlpatterns = [
    # Rutas de la API principal
    path('api/', include(router.urls)),

    # Rutas de autenticación con JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
