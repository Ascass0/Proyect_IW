from django.urls import path
from . import views

urlpatterns = [
    
#indice
    path('', views.index, name='index'),

 #equipos
    path('listadoEquipos', views.listado_equipos, name='listadoEquipos'),
    path('listadoEquipos/<int:pk>/', views.DetalleEquipo.as_view(), name='detalleEquipo'),
    path('listadoEquipos/anadirEquipo', views.CreateEquipoView.as_view(), name='anadirEquipo'),

 #tickets
    path('listadoTickets', views.listado_tickets, name='listadoTickets'),
    path('listadoTickets/<int:pk>/', views.DetalleTicket.as_view(), name='detalleTicket'),
    path('listadoTickets/anadirTicket', views.CreateTicketView.as_view(), name='anadirTicket'),

 #empleados
    path('listadoEmpleados', views.listado_empleados, name='listadoEmpleados'),
    path('listadoEmpleados/<int:pk>/', views.DetalleEmpleado.as_view(), name='detalleEmpleado'),
    path('listadoEmpleados/anadirEmpleado', views.CreateEmpleadoView.as_view(), name='anadirEmpleado'),

 #borrar
    path('delete-item1/<int:id>/', views.borradoEquipo, name='borrarEquipo'),
    path('delete-item2/<int:id>/', views.borradoTicket, name='borrarTicket'),
    path('delete-item3/<int:id>/', views.borradoEmpleado, name='borrarEmpleado'),

 #actualizar
    path('actualizarEmpleado/<int:id>/', views.editarEmpleado, name='actualizarEmpleado'),
    path('actualizarTicket/<int:id>/', views.editarTicket, name='actualizarTicket'),
    path('actualizarEquipo/<int:id>/', views.editarEquipo, name='actualizarEquipo'),

 #BUSCAR
   path('buscar', views.buscar, name='buscar'),

]