from django.contrib import admin
from. models import *
# Register your models here.

class MedicamentosRecetadosAdmin(admin.ModelAdmin):
    list_display = ["id", "receta"]
    #list_editable = ["descripcion"]
    #search_fields = ["descripcion"]
    # list_filter = ["medicamento" ]
    list_per_page = 10

class MedicamentosEnReceta (admin.TabularInline):
    model = MedicamentosRecetados
    extra = 0
    min_num = 1
    max_num = 10
    autocomplete_fields = ['medicamento']

class RecetaAdmin(admin.ModelAdmin):
    inlines = [MedicamentosEnReceta]
    list_display =["consulta","descripcion",'receta']
    list_editable = ["descripcion"]
    search_fields =["descripcion"]
    # list_filter = ["medicamento" ]
    list_per_page = 10

admin.site.register(Receta, RecetaAdmin)
admin.site.register(MedicamentosRecetados, MedicamentosRecetadosAdmin)