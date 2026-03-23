from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Fornecedor
from .forms import FornecedorForm

from rest_framework.decorators import api_view
from .serializers import FornecedorSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class FornecedorCreate(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "fornecedores/form.html"
    success_url = reverse_lazy("lista_fornecedores")

class FornecedorList(ListView):
    model = Fornecedor
    template_name = "fornecedores/lista.html"
    context_object_name = "fornecedores"

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "fornecedores/form.html"
    success_url = reverse_lazy("lista_fornecedores")

class FornecedorDelete(DeleteView):
    model = Fornecedor
    template_name = "fornecedores/excluir.html"
    success_url = reverse_lazy("lista_fornecedores")

@api_view(['GET'])
def get_fornecedores(request):

    if request.method == 'GET':
        forecedores = Fornecedor.objects.all()
        serializer = FornecedorSerializer(forecedores, many=True)
        return Response(serializer.data)
    
    return Response(status.HTTP_404_NOT_FOUND)