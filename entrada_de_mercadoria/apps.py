from django.apps import AppConfig


class EntradaDeMercadoriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entrada_de_mercadoria'

    def ready(self):
        import entrada_de_mercadoria.signals
