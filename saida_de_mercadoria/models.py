from django.db import models
from django.utils import timezone
from usuarios.models import Usuarios
from produto.models import Produto

class SaidaMercadoria(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(
        max_digits=9, decimal_places=2, blank=False, default=1)
    data_hora = models.DateTimeField(default=timezone.now)
    estoque_fisico_atual = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, default=0)
    user = models.CharField(max_length=100, blank=True, null=True)
    usuarios = models.ForeignKey(Usuarios, null=True, on_delete=models.CASCADE)

    def __str__(self):# METODO CONSTRUTOR
        return str(self.produto.nome)+ ' - ' + str(self.quantidade)

    def estoque_atual(self):
        if self.estoque_fisico_atual > 0 :
            produtos_em_estoque = float(
                self.produto.entrada - self.estoque_fisico_atual)
            SaidaMercadoria.objects.filter(
                id=self.id).update(quantidade = produtos_em_estoque)
                

    
