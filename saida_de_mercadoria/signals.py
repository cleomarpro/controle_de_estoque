from saida_de_mercadoria.models import SaidaMercadoria
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=SaidaMercadoria)
def update_quantidade_vendida(sender, instance, **kwargs):
    instance.estoque_atual()
    instance.produto.estoque_total()

@receiver(post_delete, sender=SaidaMercadoria)
def update_quantidade_vendida(sender, instance, **kwargs):
    instance.estoque_atual()
    instance.produto.estoque_total()
