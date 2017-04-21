from django.db import models
from equipos.models import Equipo


class Partido(models.Model):
	local = models.ForeignKey(Equipo, related_name='partidos_de_local')
	visitante = models.ForeignKey(Equipo, related_name='partidos_de_visitante')
	fecha = models.DateTimeField()

	def __str__(self):
		return str(self.local) + ' vs ' + str(self.visitante) +  ' ' + str(self.fecha)

