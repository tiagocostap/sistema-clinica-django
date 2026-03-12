from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = '__all__'

        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'observacao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2
            }),
        }