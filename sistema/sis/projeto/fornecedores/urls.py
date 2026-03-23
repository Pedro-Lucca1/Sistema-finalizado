from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", FornecedorList.as_view(), name="lista_fornecedores"),
    path("novo/", FornecedorCreate.as_view(), name="criar_fornecedores"),
    path("editar/<int:pk>", FornecedorUpdate.as_view(), name="editar_fornecedores"),
    path("excluir/<int:pk>", FornecedorDelete.as_view(), name="excluir_fornecedores"),
    path("cli/", views.get_fornecedores, name="get_fornecedores"),
]