from cProfile import label
from pyexpat import model
from django import forms
from .models import Equipo, Ticket, Empleado


#formulario de equipo
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('numeroSerie','modelo','marca','tipoEquipo','fechaAdquisicion','fechaPuestaMarcha','proveedorNombre','proveedorTelefono','planta')
        labels = {'numeroserie': ('Número de serie'),'modelo': ('Modelo'),'marca': ('Marca'),'tipoEquipo': ('Tipo de equipo'),'fechaAdquisicion': ('Fecha de adquisición'),
                  'fechaPuestaMarcha': ('Fecha de puesta en marcha'),'proveedorNombre': ('Nombre del proveedor'),'proveedorTelefono': ('Teléfono del proveedor'),'planta': ('Planta'),}
        widgets = {
            'fechaAdquisicion': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'fechaPuestaMarcha': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }


#formulario de ticket
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('equipo','empleado','numeroReferencia','titulo','descripcion','fechaApertura','fechaResolucion','nivelUrgencia','tipoTicket','estado','comentarios')
        labels = {'equipo': ('Equipo'),'empleado': ('Empleado'),'numeroReferencia': ('Número de Referencia'),'titulo': ('Título'),'descripcion': ('Descripción'),
                  'fechaApertura': ('Fecha de apertura'),'fechaResolucion': ('Fecha de resolución'),'nivelUrgencia': ('Nivel de urgencia'),
                  'tipoTicket': ('Tipo de ticket'),'estado': ('Estado'),'comentarios': ('Comentarios'),}
        widgets = {
            'fechaApertura': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'fechaResolucion': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'descripcion': forms.Textarea(attrs={'cols' : 50, 'rows' : 3}),
            'comentarios': forms.Textarea(attrs={'cols' : 50, 'rows' : 10}),
        }



#formulario de empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('DNI','nombre','apellido','email','telfono')
        labels = {'DNI': ('DNI'),'nombre': ('Nombre'),'apellido': ('Apellido'),'email': ('Email'),'telfono': ('Teléfono'),}