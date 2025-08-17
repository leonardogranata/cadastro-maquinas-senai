from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ColaboradoresForm, MaquinasForm
from .models import Colaboradoes, Maquinas

def gerenciadorMaquinas(request):
    maquinas = Maquinas.objects.all()
    return render(request, 'core/gerenciadorMaquinas.html', {'maquinas': maquinas})

def cadastrarMaquina(request):
    if request.method == 'POST':
        form = MaquinasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Máquina cadastrada com sucesso.')
            return redirect('gerenciadorMaquinas')
    else:
        form = MaquinasForm()
    return render(request, 'core/cadastrarMaquinas.html', {'form': form})

def cadastrarColaborador(request):
    if request.method == 'POST':
        form = ColaboradoresForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso.')
            return redirect('gerenciadorMaquinas')
    else:
        form = ColaboradoresForm()
    return render(request, 'core/cadastrarColaboradores.html', {'form': form})

def editarMaquina(request, pk):
    maquinas = get_object_or_404(Maquinas, pk=pk)
    if request.method == 'POST':
        form = MaquinasForm(request.POST, instance=maquinas)
        if form.is_valid():
            form.save()
            return redirect('gerenciadorMaquinas')
    else:
        form = MaquinasForm(instance=maquinas)
    return render(request, 'core/editarMaquina.html', {'form': form, 'tarefa': maquinas})

def excluirMaquina(request, pk):
    maquinas = get_object_or_404(Maquinas, pk=pk)
    if request.method == 'POST':
        maquinas.delete()
        return redirect('gerenciadorMaquinas')
    
    return render(request, 'core/excluirMaquina.html', {'maquinas': maquinas})

