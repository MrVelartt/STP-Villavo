from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    AppInfoListAPIView,
    RutaListAPIView,
    RutaDetailAPIView,
    ParadaListAPIView,
    ParadaDetailAPIView,
    RutaParadaListAPIView  # Asegúrate de importar la vista
)

urlpatterns = [
    # Rutas API personalizadas con APIView
    path('api/app-info/', AppInfoListAPIView.as_view(), name='app-info-list'),
    path('api/rutas/', RutaListAPIView.as_view(), name='ruta-list'),
    path('api/rutas/<int:id>/', RutaDetailAPIView.as_view(), name='ruta-detail'),

    # Nuevas rutas para Paradas
    path('api/paradas/', ParadaListAPIView.as_view(), name='parada-list'),
    path('api/paradas/<int:id>/', ParadaDetailAPIView.as_view(), name='parada-detail'),

    # Nueva ruta para manejar relaciones entre Ruta y Parada (RutaParada)
    path('api/ruta-paradas/', RutaParadaListAPIView.as_view(), name='ruta-parada-list'),

    # Rutas de autenticación JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Si vuelves a usar ViewSets, descomenta:
    # path('api/', include(router.urls)),
]
