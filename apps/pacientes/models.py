import uuid
from django.db import models
from datetime  import datetime

class Paciente(models.Model):
	id= models.UUIDField(primary_key= True, editable= False, default=uuid.uuid4)
	Nombre = models.CharField('Nombres',max_length=100)
	Apellido =  models.CharField('Apellidos',max_length=100)
	Teléfono = models.CharField(max_length=500, null=False, blank=False)
	Fecha_de_Cumpleaños = models.DateField('Fecha de Nacimiento')
	Direccion = models.CharField('Dirección',max_length=50, null=False, blank=False)

	class Meta:
		verbose_name = "Control de Registro de Pacientes"
		verbose_name_plural= "Control de Registro de Paciente"
		db_table = "paciente"
		ordering= ["Nombre"]

	def full_name(self):
		return '%s %s' % (self.Nombre, self.Apellido)


	def __str__(self):
		return self.full_name()

	def edad(self):
		years = int(
			(datetime.now().date() - self.Fecha_de_Cumpleaños)
			.days /365.25)
		return '%s años' % years

	def telefono(self):
		return self.Teléfono

	def direccion(self):
		return self.Direccion