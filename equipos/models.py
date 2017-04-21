from django.db import models

# Create your models here.
class Grupo(models.Model):
	letra = models.CharField(max_length=1, unique=True)

	def __str__(self):
		return "Grupo " + self.letra


class Equipo(models.Model):
	nombre = models.CharField(max_length=100)
	grupo = models.ForeignKey(Grupo, related_name='equipos')
	bandera = models.ImageField(upload_to="banderas")

	def __str__(self):
		return self.nombre
