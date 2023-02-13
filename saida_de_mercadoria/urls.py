from .views import SaidaMercadoriaCreate, SaidaMercadoriaDetailChangeDelete
from django.urls import path

urlpatterns = [
    path('', SaidaMercadoriaCreate.as_view()),
    path('<int:pk>/', SaidaMercadoriaDetailChangeDelete.as_view()),
]