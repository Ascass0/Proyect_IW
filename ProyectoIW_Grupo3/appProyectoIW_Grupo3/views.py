from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Equipo, Ticket, Empleado
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

#devuelve los equipos
def listado_equipos(request):
	equipos = get_list_or_404(Equipo.objects.order_by('numeroSerie'))
	context = {'equipo': equipos }
	return render(request, 'listadoEquipos.html', context)