from django import forms
from .models import Compra, ItemCompra
from produtos.models import Produto

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['fornecedor', 'numero_nota', 'data_compra', 'data_entrega', 'observacoes']
        widgets = {
            'data_compra': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_entrega': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'numero_nota': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 001/2024'}),
        }

class ItemCompraForm(forms.ModelForm):
    class Meta:
        model = ItemCompra
        fields = ['produto', 'quantidade', 'preco_unitario']
        widgets = {
            'quantidade': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
            'preco_unitario': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.all()