from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto
from .forms import ProdutoForm

from rest_framework.decorators import api_view
from .serializers import ProdutoSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ProdutoCreate(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/form.html"
    success_url = reverse_lazy("lista_produtos")

class ProdutoList(ListView):
    model = Produto
    template_name = "produtos/lista.html"
    context_object_name = "produtos"

class ProdutoUpdate(UpdateView):
    model = Produto
    form_class = ProdutoForm 
    template_name = "produtos/form.html"
    success_url = reverse_lazy("lista_produtos")

class ProdutoDelete(DeleteView):
    model = Produto
    template_name = "produtos/excluir.html"
    success_url = reverse_lazy("lista_produtos")

@api_view(['GET'])
def get_produtos(request):

    if request.method == 'GET': 
       produtos = Produto.objects.all()
       serializer = ProdutoSerializer(produtos, many=True)
       return Response(serializer.data)

    return Response(status.HTTP_404_NOT_FOUND)