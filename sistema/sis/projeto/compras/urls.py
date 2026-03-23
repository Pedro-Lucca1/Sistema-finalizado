from django.urls import path
from . import views

app_name = 'compras'

urlpatterns = [
    path('', views.lista_compras, name='lista'),
    path('nova/', views.criar_compra, name='criar'),
    path('<int:compra_id>/itens/', views.adicionar_itens, name='adicionar_itens'),
    path('<int:compra_id>/finalizar/', views.finalizar_compra, name='finalizar'),
    path('item/<int:item_id>/remover/', views.remover_item, name='remover_item'),
]