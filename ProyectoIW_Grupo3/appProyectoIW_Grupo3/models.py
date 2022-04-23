from pickle import TRUE
from django.db import models



# modelo de la clase equipo
class Equipo(models.Model):
    numeroSerie = models.IntegerField(unique=TRUE)
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=30)
    tipoEquipo = models.CharField(max_length=30)
    fechaAdquisicion = models.DateField
    fechaPuestaMarcha = models.DateField
    proveedorNombre = models.CharField(max_length=30)
    proveedorTelefono = models.IntegerField()
    planta = models.CharField(max_length=100)


#modelo de la clase empleado
class Empleado(models.Model):
    DNI = models.CharField(max_length=9, unique=TRUE)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telfono = models.IntegerField()


#modelo de la clase ticket
class Ticket(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    numeroReferencia = models.IntegerField(unique=TRUE)
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    fechaApertura = models.DateField
    fechaResolucion = models.DateField
    nivelUrgencia = models.CharField(max_length=5)
    tipoTicket = models.CharField(max_length=20)
    estado = models.CharField(max_length=30)
    comentarios = models.CharField(max_length=500)
