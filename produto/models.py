from django.db import models
from django.utils import timezone
from django.db.models import  F,Sum,DecimalField # Max ExpressionWrapper FloatField DecimalField Sum
from usuarios.models import Usuarios

class Categoria (models.Model):
    nome = models.CharField(max_length=50, blank=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    usuarios = models.ForeignKey(Usuarios, null=True, on_delete=models.CASCADE)

    def __str__(self): # METODO CONSTRUTOR
        return str(self.nome)+ ' - ' +str(self.id)

class Produto (models.Model):
    nome = models.CharField(max_length=30,  blank=True)
    categoria = models.ForeignKey(
        Categoria, verbose_name='Categoria', on_delete=models.CASCADE, default=1)
    codigo = models.CharField(max_length=13, blank=False)
    percentagem_de_lucro = models.DecimalField(
        max_digits=9, decimal_places=2, default=0)
    valor_venal = models.DecimalField(max_digits=9, decimal_places= 2, default=0)
    valor_compra = models.DecimalField(
        max_digits=9, decimal_places=2, blank=False, default=0)
    entrada = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    saida = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    estoque = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    data_hora = models.DateTimeField(default=timezone.now)
    imagem = models.ImageField( blank=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    usuarios = models.ForeignKey(Usuarios, null=True, on_delete=models.CASCADE)

    def __str__(self): # METODO CONSTRUTOR
        return str(self.nome)+ ' - ' +str(self.id)


    def estoque_total(self):
        quantidade_entrada = self.entradamercadoria_set.all().aggregate(
           total_entrada = Sum(F('quantidade'), output_Field=DecimalField()))
        total_entrada = quantidade_entrada['total_entrada'] or 0
        self.entrada = total_entrada
        Produto.objects.filter(id=self.id).update(entrada = total_entrada)


        quantidade_saida = self.saidamercadoria_set.all().aggregate(
            total_saida = Sum(F('quantidade'), output_Field=DecimalField()))
        total_saida = quantidade_saida['total_saida'] or 0
        self.saida = total_saida
        Produto.objects.filter(id=self.id).update(saida = total_saida)

        estoque_atual = self.entrada - self.saida
        Produto.objects.filter(id=self.id).update(estoque = estoque_atual)

    def calculo_percentagem_de_lucro(self):
        percentagem_de_lucro= float(self.percentagem_de_lucro) # calculo do valor venal
        if percentagem_de_lucro > 0:
            valor_produto= float(self.valor_compra) * float(
                self.percentagem_de_lucro) / 100 + float(self.valor_compra)
            self.valor_venal = valor_produto
            Produto.objects.filter(id=self.id).update(valor_venal = valor_produto)
        
        if percentagem_de_lucro <= 0: # caso o valo venal seja especificado, a variavel percentagem_de_lucro é preenchida automaticamente
            lucro= float(self.valor_venal) - float(self.valor_compra)
            lucro_estimado= lucro / float(self.valor_compra) * 100 
            self.percentagem_de_lucro = lucro_estimado
            Produto.objects.filter(id=self.id).update(
                percentagem_de_lucro = lucro_estimado)




