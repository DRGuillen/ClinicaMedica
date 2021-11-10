from django.contrib import admin
from. models import *
# Register your models here.

class HistorialClinicoAdmin (admin.ModelAdmin):
	list_display = ["paciente", "historial"]
	search_fields = ["paciente__nombre"]
	list_per_page = 10

class ConsultaAdmin(admin.ModelAdmin):
	list_display =["paciente","diagnostico","fecha","informeconsulta"]
	search_fields =["diagnostico"]
	list_editable = ["fecha", "diagnostico"]
	list_filter = ["fecha","paciente"]
	list_per_page = 10
	autocomplete_fields = ["diagnostico", "paciente"]

class DiagnosticoAdmin (admin.ModelAdmin):
	filter_horizontal = ['sintomas']
	list_display = ["nombre","Sintomas"]
	search_fields = ["nombre","sintomas__nombre"]
	list_per_page = 10

	def Sintomas(self, obj):
		return ", ".join([str(s) for s in obj.sintomas.all()])

class SintomaAdmin (admin.ModelAdmin):
	list_display = ["nombre",]
	search_fields = ["nombre",]
	list_filter = ["nombre",]
	list_per_page = 10

admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(HistorialClinico, HistorialClinicoAdmin)
admin.site.register(Sintoma, SintomaAdmin)
admin.site.register(Diagnostico, DiagnosticoAdmin)

