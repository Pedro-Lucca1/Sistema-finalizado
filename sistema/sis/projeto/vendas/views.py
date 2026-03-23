from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Venda, ItemVenda
from .forms import VendaForm, ItemVendaForm
from produtos.models import Produto

def lista_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/lista_vendas.html', {'vendas': vendas})

def criar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            if request.user.is_authenticated:
                venda.criado_por = request.user
            venda.save()
            
            messages.success(request, 'Venda criada com sucesso!')
            return redirect('vendas:adicionar_itens', venda_id=venda.id)
    else:
        form = VendaForm()
    
    return render(request, 'vendas/criar_venda.html', {'form': form})

def adicionar_itens(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    itens = venda.itens.all()
    
    if request.method == 'POST':
        form = ItemVendaForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.venda = venda
            
            # CORRIGIDO: Use 'quantidade' em vez de 'quantidade_estoque'
            if item.quantidade > item.produto.quantidade:
                messages.error(request, f'Estoque insuficiente! Disponível: {item.produto.quantidade}')
                return redirect('vendas:adicionar_itens', venda_id=venda.id)
            
            item.save()
            
            # CORRIGIDO: Use 'quantidade' em vez de 'quantidade_estoque'
            produto = item.produto
            produto.quantidade -= item.quantidade
            produto.save()
            
            # Atualizar total da venda
            venda.atualizar_valor_total()
            
            messages.success(request, f'{item.quantidade}x {item.produto.nome} adicionado com sucesso!')
            return redirect('vendas:adicionar_itens', venda_id=venda.id)
    else:
        form = ItemVendaForm()
    
    context = {
        'venda': venda,
        'itens': itens,
        'form': form,
    }
    return render(request, 'vendas/adicionar_itens.html', context)

def finalizar_venda(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    
    if request.method == 'POST':
        venda.status = 'confirmada'
        venda.save()
        
        messages.success(request, f'Venda #{venda.id} finalizada com sucesso!')
        return redirect('vendas:lista')
    
    return render(request, 'vendas/finalizar_venda.html', {'venda': venda})

def remover_item(request, item_id):
    item = get_object_or_404(ItemVenda, id=item_id)
    venda_id = item.venda.id
    
    # CORRIGIDO: Use 'quantidade' em vez de 'quantidade_estoque'
    produto = item.produto
    produto.quantidade += item.quantidade
    produto.save()
    
    item.delete()
    venda = get_object_or_404(Venda, id=venda_id)
    venda.atualizar_valor_total()
    
    messages.success(request, 'Item removido com sucesso!')
    return redirect('vendas:adicionar_itens', venda_id=venda_id)

def detalhes_venda(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    return render(request, 'vendas/detalhes_venda.html', {'venda': venda})