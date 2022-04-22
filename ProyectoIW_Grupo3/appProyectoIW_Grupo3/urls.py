from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('listadoEquipos', views.listado_equipos, name='listado_equipos'),
]