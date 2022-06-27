from .views import EntradaMercadoriaCreate, EntradaMercadoriaDetailChengeDelite
from django.urls import path

urlpatterns = [
    path('', EntradaMercadoriaCreate.as_view()),
    path('<int:pk>/', EntradaMercadoriaDetailChengeDelite.as_view()),
]