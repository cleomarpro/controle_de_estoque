from django.contrib import admin
#from core.models import Caixa
from .models import(
    Categoria,
    Produto,
)

admin.site.register(Categoria)
admin.site.register(Produto)
