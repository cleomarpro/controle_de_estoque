from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
#from django.db.models import  F,Sum,DecimalField # Max ExpressionWrapper FloatField DecimalField Sum
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from django.core.urlresolvers import reverse
#import matplotlib.pyplot as plt
#from vendas.models import ItemDoPedido
#from django.contrib.auth.models import User
#from pessoa.models import Fornecedor
#from django.contrib.auth.models import User
from usuarios.models import Usuarios
#from datetime import tade
#import math


class Categoria (models.Model):
    nome = models.CharField(max_length=50, blank=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    usuarios = models.ForeignKey(Usuarios, null=True, on_delete=models.CASCADE)

class Produto (models.Model):
    nome = models.CharField(max_length=30,  blank=True)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.CASCADE, default=1)
    codigo = models.CharField(max_length=13, blank=False)
    percentagem_de_lucro = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    valor_venal = models.DecimalField(max_digits=9, decimal_places= 2, default=0)
    valor_compra = models.DecimalField(max_digits=9, decimal_places=2, blank=False, default=0)
    entrada = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    saida = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    estoque = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    data_hora = models.DateTimeField(default=timezone.now)
    imagem = models.ImageField( blank=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    usuarios = models.ForeignKey(Usuarios, null=True, on_delete=models.CASCADE)