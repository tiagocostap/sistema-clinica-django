from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm

#MÉTODO PARA LISTAR

def lista_paciente(request):
    pacientes = Paciente.objects.all()
    form = PacienteForm(request.POST or None)
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

#MÉTODO PARA CRIAR
def criar_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'pacientes/form.html', {'form': form})

#MÉTODO PARA EDITAR
def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'pacientes/form.html', {'form': form})

#MÉTODO PARA EXCLUIR
def excluir_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('lista_pacientes')


