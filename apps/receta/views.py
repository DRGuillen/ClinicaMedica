from django.shortcuts import render
from apps.receta.models import *
from datetime import date
from easy_pdf.views import PDFTemplateView
# Create your views here.

class RecetaPDFView(PDFTemplateView):
    template_name = "receta.html"

    def get_context_data(self, **kwargs):
        id = self.request.GET.get("id")
        receta = Receta.objects.get(id=id)
        fecha = date.today()
        medicamentos = MedicamentosRecetados.objects.filter(receta=id)

        return super(RecetaPDFView, self).get_context_data(
            pagesize="Letter",
            titulo="Receta",
            receta=receta,
            fecha=fecha,
            medicamentos=medicamentos,
            **kwargs
        )