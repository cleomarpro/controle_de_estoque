from produto.models import  EntradaMercadoria
from rest_framework import serializers


class EntradaMercadoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntradaMercadoria
        fields = ['id', 'quantidade', 'produto','validade_produto']

