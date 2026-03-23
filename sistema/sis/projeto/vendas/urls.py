from django.urls import path
from . import views

app_name = 'vendas'

urlpatterns = [
    path('', views.lista_vendas, name='lista'),
    path('nova/', views.criar_venda, name='criar'),
    path('<int:venda_id>/itens/', views.adicionar_itens, name='adicionar_itens'),
    path('<int:venda_id>/finalizar/', views.finalizar_venda, name='finalizar'),
    path('<int:venda_id>/detalhes/', views.detalhes_venda, name='detalhes'),
    path('item/<int:item_id>/remover/', views.remover_item, name='remover_item'),
]