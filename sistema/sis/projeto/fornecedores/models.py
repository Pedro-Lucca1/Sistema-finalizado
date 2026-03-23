from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome