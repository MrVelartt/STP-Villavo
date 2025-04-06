from django.urls import path  # No necesitas include ni DefaultRouter si usas APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (AppInfoListAPIView, RutaListAPIView, RutaDetailAPIView )


urlpatterns = [
    # Rutas API personalizadas con APIView
    path('api/app-info/', AppInfoListAPIView.as_view(), name='app-info-list'),
    path('api/rutas/', RutaListAPIView.as_view(), name='ruta-list'),
    path('api/rutas/<int:id>/', RutaDetailAPIView.as_view(), name='ruta-detail'),


    # Rutas de autenticación JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Si vuelves a usar ViewSets, descomenta:
    # path('api/', include(router.urls)),
]