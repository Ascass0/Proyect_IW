from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('listadoEquipos', views.listado_equipos, name='listadoEquipos'),
 path('listadoEquipos/<int:pk>/', views.DetalleEquipo.as_view(), name='detalleEquipo'),
 path('listadoEquipos/anadirEquipo', views.CreateEquipoView.as_view(), name='anadirEquipo'),
 path('listadoTickets', views.listado_tickets, name='listadoTickets'),
 path('listadoTickets/<int:pk>/', views.DetalleTicket.as_view(), name='detalleTicket'),
 path('listadoTickets/anadirTicket', views.CreateTicketView.as_view(), name='anadirTicket'),
 path('listadoEmpleados', views.listado_empleados, name='listadoEmpleados'),
]