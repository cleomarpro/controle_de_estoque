from django.contrib import admin
#from core.models import Caixa
from .models import(
    Categoria,
    Produto,
    SaidaMercadoria,
    EntradaMercadoria,
    
)

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(SaidaMercadoria)
admin.site.register(EntradaMercadoria)
