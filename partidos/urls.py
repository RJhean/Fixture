from django.conf.urls import url
from .views import ver_partidos
urlpatterns = [

    url(r'^$', ver_partidos, name='ver_partidos'),
]
