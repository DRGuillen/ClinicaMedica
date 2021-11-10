import uuid
from django.db import models

class Medicamento(models.Model):
	id= models.UUIDField(primary_key= True, editable= False, default=uuid.uuid4)
	nombre = models.CharField(blank=False, max_length=100)
	presentacion = models.CharField(blank=False, max_length=100)
	volumen = models.CharField(blank=False, max_length=50)
	descripcion = models.CharField(blank=False, max_length=200)
	
	class Meta:
		verbose_name = "Medicamentos"
		verbose_name_plural= "Medicamentos"
		db_table = "medicamento"
	
	def full_name(self):
		return '%s %s' % (self.nombre, self.presentacion)

	
	def __str__(self):
		return self.full_name()

