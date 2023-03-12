from django.apps import AppConfig


class SaidaDeMercadoriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'saida_de_mercadoria'

    def ready(self):
        import saida_de_mercadoria.signals