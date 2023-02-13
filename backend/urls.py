
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
    TokenVerifyView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('produto/', include('produto.urls')),
    path('login_authentication/', include('login_authentication.urls')),
    path('entrada_de_mercadoria/', include('entrada_de_mercadoria.urls')),
    path('saida_de_mercadoria/', include('saida_de_mercadoria.urls')),
]
