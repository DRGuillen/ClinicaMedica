from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from apps.receta.views import *
from apps.consultas.views import *

urlpatterns = [
    url(r'^', include('apps.pacientes.urls')),  
    url(r'^', include('apps.home.urls')),
    path('admin/', admin.site.urls),
    path('receta/', RecetaPDFView.as_view(), name = 'Receta'),
    path('informeconsulta/', InformeConsultaPDFView.as_view(), name = 'InformeConsulta'),
    path('historial/', HistorialClinicoPDFView.as_view(), name = 'HistorialClinico'),
]
