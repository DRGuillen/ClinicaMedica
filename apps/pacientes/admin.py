from django.contrib import admin
from. models import *



class PacienteAdmin(admin.ModelAdmin):
	list_display =["Nombre","Apellido","edad","Direccion"]
	list_editable = ["Direccion"]
	search_fields =["Nombre"]
	list_filter = ["Nombre","Apellido"]
	list_per_page = 10
admin.site.register(Paciente, PacienteAdmin)

