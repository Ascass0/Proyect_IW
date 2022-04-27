
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Equipo, Ticket, Empleado
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView
from .forms import EquipoForm, TicketForm, EmpleadoForm


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




#---------------------------------EQUIPO--------------------------------------

#clase para el formulario de añadir equipo
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
            # return redirect('equipo')
        return render(request, 'anadirEquipo.html', {'form': form, 'titulo_pagina': 'Crear nuevo equipo'})


#clase para los detalles de cada equipo
class DetalleEquipo(DetailView):
    model = Equipo
    template_name = 'detalleEquipo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





#---------------------------------TICKET--------------------------------------

#clase para el formulario de añadir ticket
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

            # Volvemos a la lista de equipos
            # return redirect('equipo')
        return render(request, 'anadirTicket.html', {'form': form, 'titulo_pagina': 'Crear nuevo ticket'})


#clase para los detalles de cada ticket
class DetalleTicket(DetailView):
    model = Ticket
    template_name = 'detalleTicket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    





#---------------------------------EMPLEADO--------------------------------------

#clase para el formulario de añadir empleado
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

            # Volvemos a la lista de equipos
            # return redirect('equipo')
        return render(request, 'anadirEmpleado.html', {'form': form, 'titulo_pagina': 'Crear nuevo empleado'})


#clase para los detalles de cada empleado
class DetalleEmpleado(DetailView):
    model = Empleado
    template_name = 'detalleEmpleado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#funcion que coge el id del empleado para borrar
def borradoEmpleado(request, id):
    item = Empleado.objects.get(id=id)
    item.delete()
    return redirect ('listadoEmpleados')


#funcion que coge el id del equipo para borrar
def borradoEquipo(request, id):
    item = Equipo.objects.get(id=id)
    item.delete()
    return redirect ('listadoEquipos')
    

#funcion que coge el id del ticket para borrar
def borradoTicket(request, id):
    item = Ticket.objects.get(id=id)
    item.delete()
    return redirect ('listadoTickets')



def modificadoTicket(request, id):
    Ticket.objects.filter(pk=id).update(numeroReferencia = 9999)
    return redirect ('listadoTickets')