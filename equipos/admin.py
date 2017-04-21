from django.contrib import admin

# Register your models here.
from .models import Equipo, Grupo

admin.site.register(Equipo)
admin.site.register(Grupo)