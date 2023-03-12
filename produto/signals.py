from produto.models import Produto
from saida_de_mercadoria.models import SaidaMercadoria
from entrada_de_mercadoria.models import EntradaMercadoria
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Produto)
def update_total_estoque(sender, instance, **kwargs):
    instance.calculo_percentagem_de_lucro()
