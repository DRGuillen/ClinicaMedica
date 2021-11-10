from django.contrib import admin
from. models import *



class CitaAdmin(admin.ModelAdmin):
	list_display =["paciente","fecha","motivo",]
	search_fields =["motivo"]
	list_editable = ["fecha", "motivo"]
	list_filter = ["fecha", "paciente"]
	list_per_page = 10
admin.site.register(Cita, CitaAdmin)

