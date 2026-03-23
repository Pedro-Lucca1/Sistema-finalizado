from django.db import models


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data = models.DateField()
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome