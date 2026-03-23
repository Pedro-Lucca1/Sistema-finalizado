from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Importando modelos de outros apps
from produtos.models import Produto
from fornecedores.models import Fornecedor

class Compra(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    )
    
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name='compras')
    numero_nota = models.CharField(max_length=50, unique=True, help_text="Número da nota fiscal")
    data_compra = models.DateField(default=timezone.now)
    data_entrega = models.DateField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    observacoes = models.TextField(blank=True, null=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-data_compra']
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
    
    def __str__(self):
        return f"Compra {self.numero_nota} - {self.fornecedor.nome}"
    
    def atualizar_valor_total(self):
        total = sum(item.subtotal for item in self.itens.all())
        self.valor_total = total
        self.save()

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='compras')
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    
    class Meta:
        verbose_name = 'Item da Compra'
        verbose_name_plural = 'Itens da Compra'
    
    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"