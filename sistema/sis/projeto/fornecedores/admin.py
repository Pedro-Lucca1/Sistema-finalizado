from django.contrib import admin
from .models import Fornecedor

# Register your models here.
@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email','telefone')