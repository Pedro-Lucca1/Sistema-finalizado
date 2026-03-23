from django.forms import ModelForm
from .models import Produto
from django import forms

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "preco", "descricao", "quantidade", "validade"]
        widgets = {
            # Exibe dd/mm/aaaa e aceita esse formato
            'validade': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }
    
    # Define os formatos que o Django aceita na validação
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['validade'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']