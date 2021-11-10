from django.contrib import admin
from. models import *
# Register your models here.


class MedicamentoAdmin(admin.ModelAdmin):
	list_display =["nombre","presentacion","volumen","descripcion"]
	search_fields =["presentacion"]
	list_editable = ["presentacion", "descripcion"]
	list_filter = ["nombre","presentacion"]
	list_per_page = 10

admin.site.register(Medicamento, MedicamentoAdmin)

