from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", ProdutoList.as_view(), name="lista_produtos"),
    path("novo/", ProdutoCreate.as_view(), name="criar_produtos"),
    path("editar/<int:pk>", ProdutoUpdate.as_view(), name="editar_produtos"),
    path("excluir/<int:pk>", ProdutoDelete.as_view(), name="excluir_produtos"),
    path("cli/", views.get_produtos, name="get_produtos"),
]