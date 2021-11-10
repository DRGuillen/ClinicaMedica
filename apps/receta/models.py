import uuid
from django.db import models
from apps.consultas.models import Consulta
from apps.medicamentos.models import Medicamento
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe


class Receta(models.Model):
	id= models.UUIDField(primary_key= True, editable= False, default=uuid.uuid4)
	consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
	# medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
	descripcion = models.TextField(blank=False)

	class Meta:
		verbose_name = "Recetas Medicas"
		verbose_name_plural= "Recetas Medicas"
		db_table = "receta"

	def full_name(self):
		# return '%s %s' % (self.consulta, self.medicamento)
		return '%s %s' % (self.consulta, self.descripcion)

	def __str__(self):
		return self.full_name()

	def receta (self):
		return mark_safe(u'<a href="/receta/?id=%s" target="_blank">Generar</a>' % self.id)
	receta.short_description = 'Receta Médica'


class MedicamentosRecetados (models.Model):
	receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
	medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
	prescripcion = models.TextField(blank=False)

	def __str__(self):
		return '%s %s' % (self.pk, self.receta)

	class Meta:
		verbose_name = "Detalle Receta Medica"
		verbose_name_plural= "Detalles Recetas Medicas"
		db_table = "detallereceta"
