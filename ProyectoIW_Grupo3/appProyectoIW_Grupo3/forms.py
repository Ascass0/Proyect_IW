from pyexpat import model
from django import forms
from .models import Equipo, Ticket, Empleado

#formulario de equipo
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'


#formulario de ticket
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        

#formulario de empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'