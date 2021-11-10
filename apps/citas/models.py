import uuid
from django.db import models
from apps.pacientes.models import Paciente

class Cita(models.Model):
	id= models.UUIDField(primary_key= True, editable= False, default=uuid.uuid4)
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	fecha = models.DateField()
	motivo = models.TextField(blank=False)
	
	class Meta:
		verbose_name = "Control de Citas"
		verbose_name_plural= "Control de Citas"
		db_table = "cita"

	def full_name(self):
		return '%s %s' % (self.paciente, self.fecha,)
	

	def __str__(self):
		return self.full_name()