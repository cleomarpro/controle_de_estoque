from django.db import models
#from django.db.models import Count
from django.utils import timezone
from django.contrib.auth.models import User


class Usuarios(models.Model):
    cpf_cnpj = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_cliente= models.CharField(max_length=100,blank=False)
    razao_social= models.CharField(max_length=30, blank=True, verbose_name='Razão Social')
    inscricao_estadual= models.CharField(max_length=30, blank=True, verbose_name='Inscrição estadual')
    inscricao_municipal= models.CharField(max_length=30, blank=True, verbose_name='Inscrição municipal')
    nascionalidade = models.CharField(max_length=50, blank=True)
    cep = models.CharField(max_length=12, blank=True)
    rua = models.CharField(max_length=50, blank=True)
    quadra = models.CharField(max_length=10, blank=True)
    numero = models.CharField(max_length=10, blank=True,verbose_name="Número")
    setor = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=10, blank=True)
    cidade = models.CharField(max_length=10, blank=True)
    pais = models.CharField(max_length=10, blank=True, verbose_name="País")
    complemento = models.CharField(max_length=50, blank=True)
    DDD = models.CharField(max_length=8, blank=True)
    Celular = models.CharField(max_length=20, blank=True)
    DDD = models.CharField(max_length=8, blank=True)
    Telefone = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=50, blank=True)
    nome_fantazia = models.CharField(max_length=50, blank=True)
    data_de_criacao = models.DateField(max_length=30, null= True, blank=True, verbose_name="Data de criação")
    data_hora = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
            return str(self.id)+ ' ' + str(self.nome_fantazia) + ' User' + str(self.user.id)