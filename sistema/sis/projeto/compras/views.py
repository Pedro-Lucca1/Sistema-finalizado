from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Compra, ItemCompra
from .forms import CompraForm, ItemCompraForm
from produtos.models import Produto

def lista_compras(request):
    compras = Compra.objects.all()
    return render(request, 'compras/lista_compras.html', {'compras': compras})

def criar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            if request.user.is_authenticated:
                compra.criado_por = request.user
            compra.save()
            
            messages.success(request, 'Compra criada com sucesso!')
            return redirect('compras:adicionar_itens', compra_id=compra.id)
    else:
        form = CompraForm()
    
    return render(request, 'compras/criar_compra.html', {'form': form})

def adicionar_itens(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    itens = compra.itens.all()
    
    if request.method == 'POST':
        form = ItemCompraForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.compra = compra
            item.save()
            
            # CORRIGIDO: Use 'quantidade' em vez de 'quantidade_estoque'
            produto = item.produto
            produto.quantidade += item.quantidade
            produto.save()
            
            # Atualizar total da compra
            compra.atualizar_valor_total()
            
            messages.success(request, f'{item.quantidade}x {item.produto.nome} adicionado com sucesso!')
            return redirect('compras:adicionar_itens', compra_id=compra.id)
    else:
        form = ItemCompraForm()
    
    context = {
        'compra': compra,
        'itens': itens,
        'form': form,
    }
    return render(request, 'compras/adicionar_itens.html', context)

def finalizar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    
    if request.method == 'POST':
        compra.status = 'concluida'
        compra.save()
        
        messages.success(request, f'Compra {compra.numero_nota} finalizada com sucesso!')
        return redirect('compras:lista')
    
    return render(request, 'compras/finalizar_compra.html', {'compra': compra})

def remover_item(request, item_id):
    item = get_object_or_404(ItemCompra, id=item_id)
    compra_id = item.compra.id
    
    # CORRIGIDO: Use 'quantidade' em vez de 'quantidade_estoque'
    produto = item.produto
    produto.quantidade -= item.quantidade
    produto.save()
    
    item.delete()
    compra = get_object_or_404(Compra, id=compra_id)
    compra.atualizar_valor_total()
    
    messages.success(request, 'Item removido com sucesso!')
    return redirect('compras:adicionar_itens', compra_id=compra_id)