from django.forms import ModelForm, Textarea
from apps.pacientes.models import Paciente

from django import forms


class PacienteForm(ModelForm):

    Nombre = forms.CharField(label='Nombre',  widget=forms.TextInput( attrs={'class': 'form-control',}))
    Apellido = forms.CharField(label= 'Apellido', widget=forms.TextInput( attrs={'class': 'form-control',}))  
    Teléfono = forms.CharField(label= 'Teléfono', widget=forms.NumberInput(attrs={'class': 'form-control'}) )
    Edad = forms.IntegerField(label='Edad',  widget=forms.NumberInput( attrs={'class': 'form-control',}))
    class Meta:
        model = Paciente
        fields = (
    'Nombre',
    'Apellido',
    'Edad',
    'Teléfono'
    )