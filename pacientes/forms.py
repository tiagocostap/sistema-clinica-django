from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'placeholder': 'dd/mm/aaaa'}
        )
    )

    class Meta:
        model = Paciente
        fields = '__all__'