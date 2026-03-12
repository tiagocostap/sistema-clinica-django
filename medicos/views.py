from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico
from .forms import MedicoForm

# LISTAR
def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos/lista.html', {'medicos': medicos})

# CRIAR
def novo_medico(request):
    form = MedicoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_medicos')

    return render(request, 'medicos/form.html', {'form': form})

# EDITAR
def editar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    form = MedicoForm(request.POST or None, instance=medico)

    if form.is_valid():
        form.save()
        return redirect('lista_medicos')

    return render(request, 'medicos/form.html', {'form': form})

# EXCLUIR
def excluir_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    medico.delete()
    return redirect('lista_medicos')