from pyexpat import model
from django import forms
from .models import Equipo, Ticket, Empleado

#formulario de equipo
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'fechaAdquisicion': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'fechaPuestaMarcha': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }


#formulario de ticket
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        widgets = {
            'fechaApertura': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'fechaResolucion': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

        
#formulario de empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


#formulario de actualizar empleado
class EmpleadoActualizarForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


#formulario de actualizar ticket
class TicketActualizarForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'


#formulario de actualizar equipo
class EquipoActualizarForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'