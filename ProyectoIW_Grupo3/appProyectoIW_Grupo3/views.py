from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Equipo, Ticket, Empleado
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView
from .forms import EquipoForm, TicketForm

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

class CreateEquipoView(View):
	
	# Llamada para mostrar la página con el formulario de creación al usuario
	def get(self, request, *args, **kwargs):
		form = EquipoForm()
		context = {
			'form': form,
			'titulo_pagina': 'Crear nuevo equipo'
		}
		return render(request, 'anadirEquipo.html', context)

	# Llamada para procesar la creación de la categoría
	def post(self, request, *args, **kwargs):
		form = EquipoForm(request.POST)
		if form.is_valid():

			form.save()

			# Volvemos a la lista de equipos
			#return redirect('equipo')

		return render(request, 'anadirEquipo.html', {'form': form, 'titulo_pagina': 'Crear nuevo equipo'})

class DetalleEquipo(DetailView):
	model = Equipo
	template_name = 'detalleEquipo.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class CreateTicketView(View):
	
	# Llamada para mostrar la página con el formulario de creación al usuario
	def get(self, request, *args, **kwargs):
		form = TicketForm()
		context = {
			'form': form,
			'titulo_pagina': 'Crear nuevo tiquet'
		}
		return render(request, 'anadirTicket.html', context)

	# Llamada para procesar la creación de la categoría
	def post(self, request, *args, **kwargs):
		form = TicketForm(request.POST)
		if form.is_valid():

			form.save()

			# Volvemos a la lista de equipos
			#return redirect('equipo')

		return render(request, 'anadirTicket.html', {'form': form, 'titulo_pagina': 'Crear nuevo ticket'})
	
class DetalleTicket(DetailView):
	model = Ticket
	template_name = 'detalleTicket.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
