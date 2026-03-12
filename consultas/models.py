from django.db import models
from pacientes.models import Paciente
from medicos.models import Medico

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.paciente} - {self.medico} - {self.data}"