from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"
    
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def _str_(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    datadenascimento = models.CharField(max_length=8)
    cidade = models.ForeignKey(max_length=10)