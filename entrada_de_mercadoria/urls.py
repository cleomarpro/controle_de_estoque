from .views import EntradaMercadoriaCreate
from django.urls import path

urlpatterns = [
    path('', EntradaMercadoriaCreate.as_view()),
]