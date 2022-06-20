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
from produto.models import Produto
#from django.contrib.auth.models import User
from usuarios.models import Usuarios
#from datetime import tade
#import math

class SaidaMercadoria(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=9, decimal_places=2, blank=False, default=1)
    data_hora = models.DateTimeField(default=timezone.now)
    validade_produto = models.DateField(blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    usuarios = models.ForeignKey(Usuarios, null=True, on_delete=models.CASCADE)