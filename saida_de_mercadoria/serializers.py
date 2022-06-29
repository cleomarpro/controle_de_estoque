from produto.models import  SaidaMercadoria
from rest_framework import serializers


class SaidaMercadoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaidaMercadoria
        fields = ['id', 'quantidade', 'produto','usuarios','user', 'estoque_fisico_atual']

