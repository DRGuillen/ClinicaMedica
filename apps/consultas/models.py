import uuid
from django.db import models
from apps.pacientes.models import Paciente
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

class Sintoma (models.Model):
	nombre = models.CharField(max_length=100, blank=False)

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		verbose_name = "Síntoma"
		verbose_name_plural= "Síntomas"
		db_table = "sintoma"

class Diagnostico (models.Model):
	nombre = models.CharField(max_length=100, blank=False)
	sintomas = models.ManyToManyField(Sintoma)

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		verbose_name = "Diagnóstico"
		verbose_name_plural= "Diagnósticos"
		db_table = "diagnostico"

class Consulta(models.Model):
	# id = models.UUIDField(primary_key= True, editable= False, default=uuid.uuid4)
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	sintomatologia = models.TextField(blank=True)
	# diagnostico = models.TextField(blank=True)
	diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, blank=True, null=True)
	fecha = models.DateField()

	class Meta:
		verbose_name = "Control de Consulta Medica"
		verbose_name_plural= "Control de Consulta Medica"
		db_table = "consulta"

	def full_name(self):
		return '%s %s' %(self.paciente,  self.diagnostico)

	def __str__(self):
		return self.full_name()

	def informeconsulta (self):
		return mark_safe(u'<a href="/informeconsulta/?id=%s" target="_blank">Generar</a>' % self.id)
	informeconsulta.short_description = 'Informe de Consulta'

class HistorialClinico (models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

	def __str__(self):
		return '%s' % (self.paciente)

	class Meta:
		verbose_name = "Historial clínico"
		verbose_name_plural= "Historiales clínicos"
		db_table = "historial_clinico"

	def historial (self):
		return mark_safe(u'<a href="/historial/?id=%s" target="_blank">Generar</a>' % self.id)
	historial.short_description = 'Historial Clinico'