from django.shortcuts import render
from apps.consultas.models import *
from easy_pdf.views import PDFTemplateView
from datetime import date

# Create your views here.

class InformeConsultaPDFView(PDFTemplateView):
    template_name = "informe_consulta.html"

    def get_context_data(self, **kwargs):
        id = self.request.GET.get("id")
        consulta = Consulta.objects.get(id=id)

        return super(InformeConsultaPDFView, self).get_context_data(
            pagesize="Letter",
            titulo="Informe de Consulta",
            consulta=consulta,
            **kwargs
        )

class HistorialClinicoPDFView(PDFTemplateView):
    template_name = "historial_clinico.html"

    def get_context_data(self, **kwargs):
        id = self.request.GET.get("id")
        historial = HistorialClinico.objects.get(id=id)
        id_paciente = historial.paciente.pk
        consultas = Consulta.objects.filter(paciente_id=id_paciente)
        fecha = date.today()

        return super(HistorialClinicoPDFView, self).get_context_data(
            pagesize="Letter",
            titulo="Historial clinico",
            fecha=fecha,
            historial=historial,
            id_paciente = id_paciente,
            consultas=consultas,
            **kwargs
        )