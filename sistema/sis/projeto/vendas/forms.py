from django import forms
from .models import Venda, ItemVenda
from produtos.models import Produto

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'data_venda', 'forma_pagamento', 'desconto', 'observacoes']
        widgets = {
            'data_venda': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'forma_pagamento': forms.Select(attrs={'class': 'form-control'}),
            'desconto': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'class': 'form-control'}),
        }

class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade', 'preco_unitario']
        widgets = {
            'quantidade': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
            'preco_unitario': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # CORRIGIDO: Use 'quantidade' em vez de 'quantidade_estoque'
        self.fields['produto'].queryset = Produto.objects.filter(quantidade__gt=0)