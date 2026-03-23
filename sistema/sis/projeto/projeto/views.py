from django.views.generic import TemplateView

from clientes.models import Cliente
from produtos.models import Produto
from fornecedores.models import Fornecedor

class DashboardView(TemplateView):
    template_name = "dashboard.html"

    # Função que envia dados extras para o HTML
    def get_context_data(self, **kwargs):
        
        # Recupera o pacote de contexto padrão
        context = super().get_context_data(**kwargs)

        context['total_clientes'] = Cliente.objects.count()
        context['total_produtos'] = Produto.objects.count()
        context['total_fornecedores'] = Fornecedor.objects.count()
        
        return context
    