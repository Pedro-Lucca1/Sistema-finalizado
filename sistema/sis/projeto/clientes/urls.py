from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", ClienteList.as_view(), name="lista_clientes"),
    path("novo/", ClienteCreate.as_view(), name="criar_clientes"),
    path("editar/<int:pk>", ClienteUpdate.as_view(), name="editar_clientes"),
    path("excluir/<int:pk>", ClienteDelete.as_view(), name="excluir_clientes"),
    path("cli/", views.get_clientes, name="get_clientes"),
]