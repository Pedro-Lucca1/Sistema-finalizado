from django.forms import ModelForm
from .models import Cliente
from django import forms

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "email", "data", "telefone"]
        widgets = {
            # Exibe dd/mm/aaaa e aceita esse formato
            'data': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }
    
    # Define os formatos que o Django aceita na validação
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']