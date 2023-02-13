from produto.models import  Produto
from rest_framework import serializers


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'estoque', 'codigo', 'categoria','percentagem_de_lucro']

