from django.db import models

# Create your models here.

class Cliente(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    dt_nasc = models.DateField()
    sexo = models.CharField(max_length=1)
    
class Imovel(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=3)
    localizacao = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)