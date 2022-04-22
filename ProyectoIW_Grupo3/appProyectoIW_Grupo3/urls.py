from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('listadoEquipos', views.listado_equipos, name='listadoEquipos'),
 path('listadoTickets', views.listado_tickets, name='listadoTickets'),
 path('listadoEmpleados', views.listado_empleados, name='listadoEmpleados'),
]