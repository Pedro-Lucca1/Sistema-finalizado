from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.00)]
    )
    descricao = models.CharField(max_length=180)
    quantidade = models.PositiveIntegerField()
    validade = models.DateField()

    def __str__(self):
        return self.nome