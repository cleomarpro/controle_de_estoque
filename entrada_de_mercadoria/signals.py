from entrada_de_mercadoria.models import EntradaMercadoria
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=EntradaMercadoria)
def update_total_entrada(sender, instance, **kwargs):
    instance.produto.estoque_total()

@receiver(post_delete, sender=EntradaMercadoria)
def update_total_entrada(sender, instance, **kwargs):
    instance.produto.estoque_total()