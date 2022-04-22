from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Equipo, Ticket, Empleado
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

#devuelve los equipos
def listado_equipos(request):
	equipos = Equipo.objects.order_by('numeroSerie')
	context = {'equipo': equipos }
	return render(request, 'listadoEquipos.html', context)

def listado_tickets(request):
	tickets = Ticket.objects.order_by('titulo')
	context = {'ticket': tickets }
	return render(request, 'listadoTickets.html', context)

def listado_empleados(request):
	empleados = Empleado.objects.order_by('DNI')
	context = {'empleado': empleados }
	return render(request, 'listadoEmpleados.html', context)