from .views import EntradaMercadoriaCreate, EntradaMercadoriaDetailChangeDelete
from django.urls import path

urlpatterns = [
    path('', EntradaMercadoriaCreate.as_view()),
    path('<int:pk>/', EntradaMercadoriaDetailChangeDelete.as_view()),
]