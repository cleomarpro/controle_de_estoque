
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('produto/', include('produto.urls')),
    path('login_authentication/', include('login_authentication.urls')),
    path('entrada_de_mercadoria/', include('entrada_de_mercadoria.urls')),
]
