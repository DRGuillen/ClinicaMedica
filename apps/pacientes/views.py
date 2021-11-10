from django.shortcuts import render
from apps.pacientes.models import Paciente
from . import forms


def lista_pacientes(request):
	pacientes = Paciente.objects.all()
	context= {'pacientes':pacientes}
	return render(request,'pacientes/lista-pacientes.html',context)





