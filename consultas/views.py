from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulta
from .forms import ConsultaForm

# LISTAR
def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/lista.html', {'consultas': consultas})

# CRIAR
def criar_consulta(request):
    form = ConsultaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_consultas')

    return render(request, 'consultas/form.html', {'form': form})

# EDITAR
def editar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    form = ConsultaForm(request.POST or None, instance=consulta)

    if form.is_valid():
        form.save()
        return redirect('lista_consultas')

    return render(request, 'consultas/form.html', {'form': form})

# EXCLUIR
def excluir_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    consulta.delete()
    return redirect('lista_consultas')