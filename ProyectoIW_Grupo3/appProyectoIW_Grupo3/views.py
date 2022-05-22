
from asyncio.windows_events import NULL
from pickle import FALSE, TRUE
from unicodedata import name
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Equipo, Ticket, Empleado
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import DetailView
from .forms import EquipoForm, TicketForm, EmpleadoForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import CharField
from django.db.models.functions import Lower

CharField.register_lookup(Lower)
 

# devuelve la página principal
def index(request):
    return render(request, 'index.html')

# devuelve  el listado de los equipos
def listado_equipos(request):
    equipos = Equipo.objects.order_by('numeroSerie')
    context = {'equipo': equipos}
    return render(request, 'listadoEquipos.html', context)


# devuelve  el listado de los tickets
def listado_tickets(request):
    tickets = Ticket.objects.order_by('titulo')
    context = {'ticket': tickets}
    return render(request, 'listadoTickets.html', context)


# devuelve  el listado de los empleados
def listado_empleados(request):
    empleados = Empleado.objects.order_by('DNI')
    context = {'empleado': empleados}
    return render(request, 'listadoEmpleados.html', context)


# ---------------------------------EQUIPO--------------------------------------

# clase para el formulario de añadir equipo
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
            return redirect('listadoEquipos')
        return render(request, 'anadirEquipo.html', {'form': form, 'titulo_pagina': 'Crear nuevo equipo'})


# clase para los detalles de cada equipo
class DetalleEquipo(DetailView):
    model = Equipo
    template_name = 'detalleEquipo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# ---------------------------------TICKET--------------------------------------

# clase para el formulario de añadir ticket
class CreateTicketView(View):

    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        form = TicketForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear nuevo ticket'
        }
        return render(request, 'anadirTicket.html', context)

    # Llamada para procesar la creación de la categoría
    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadoTickets')
        return render(request, 'anadirTicket.html', {'form': form, 'titulo_pagina': 'Crear nuevo ticket'})


# clase para los detalles de cada ticket
class DetalleTicket(DetailView):
    model = Ticket
    template_name = 'detalleTicket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# ---------------------------------EMPLEADO--------------------------------------

# clase para el formulario de añadir empleado
class CreateEmpleadoView(View):

    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        form = EmpleadoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear nuevo empleado'
        }
        return render(request, 'anadirEmpleado.html', context)

    # Llamada para procesar la creación de la categoría
    def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('listadoEmpleados')
        return render(request, 'anadirEmpleado.html', {'form': form, 'titulo_pagina': 'Crear nuevo empleado'})


# clase para los detalles de cada empleado
class DetalleEmpleado(DetailView):
    model = Empleado
    template_name = 'detalleEmpleado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# ---------------------------------BORRADOS--------------------------------------

# funcion que coge el id del empleado para borrar
def borradoEmpleado(request, id):
    item = Empleado.objects.get(id=id)
    item.delete()
    return redirect('listadoEmpleados')


# funcion que coge el id del equipo para borrar
def borradoEquipo(request, id):
    item = Equipo.objects.get(id=id)
    item.delete()
    return redirect('listadoEquipos')


# funcion que coge el id del ticket para borrar
def borradoTicket(request, id):
    item = Ticket.objects.get(id=id)
    item.delete()
    return redirect('listadoTickets')


# ---------------------------------ACTUALIZAR--------------------------------------

def editarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    form = EmpleadoForm(request.POST or None, instance=empleado)
    if form.is_valid():
        empleado = form.save(commit=False)
        form.save()
        return redirect('listadoEmpleados')
    return render(request, 'actualizarEmpleado.html', {"titulo": 'actualizar empleado', "form": form})


def editarTicket(request, id):
    ticket = Ticket.objects.get(id=id)
    form = TicketForm(request.POST or None, instance=ticket)
    if form.is_valid():
        ticket = form.save(commit=False)
        form.save()
        return redirect('listadoTickets')
    return render(request, 'actualizarTicket.html', {"titulo": 'actualizar ticket', "form": form})


def editarEquipo(request, id):
    equipo = Equipo.objects.get(id=id)
    form = EquipoForm(request.POST or None, instance=equipo)
    if form.is_valid():
        equipo = form.save(commit=False)
        form.save()
        return redirect('listadoEquipos')
    return render(request, 'actualizarEquipo.html', {"titulo": 'actualizar equipo', "form": form})




# ---------------------------------BUSCAR--------------------------------------

def buscarEquipo(request):
    if request.method=='POST':
        busqueda=request.POST.get('busqueda')
        resultado=Equipo.objects.filter(modelo__contains=busqueda)
        prueba=False
        if not resultado:
            prueba = True
        return render(request, 'buscarEquipo.html', {'busqueda':busqueda, 'resultado':resultado, 'prueba':prueba})
    else:
        return render(request, 'buscarEquipo.html', {})


def buscarTicket(request):
    if request.method=='POST':
        busqueda=request.POST.get('busqueda')
        resultado=Ticket.objects.filter(titulo__contains=busqueda)
        prueba=False
        if not resultado:
            prueba = True
        return render(request, 'buscarTicket.html', {'busqueda':busqueda, 'resultado':resultado, 'prueba':prueba})
    else:
        return render(request, 'buscarTicket.html', {})


def buscarEmpleado(request):
    if request.method=='POST':
        busqueda=request.POST.get('busqueda')
        resultado=Empleado.objects.filter(DNI__contains=busqueda)
        prueba=False
        if not resultado:
            prueba = True
        return render(request, 'buscarEmpleado.html', {'busqueda':busqueda, 'resultado':resultado, 'prueba':prueba})
    else:
        return render(request, 'buscarEmpleado.html', {})