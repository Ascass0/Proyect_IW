from pickle import TRUE
from django.db import models



# modelo de la clase equipo
class Equipo(models.Model):
    numeroSerie = models.IntegerField(unique=TRUE)
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=30)
    tipoEquipo = models.CharField(max_length=30)
    fechaAdquisicion = models.DateField(blank=True, null=True)
    fechaPuestaMarcha = models.DateField(blank=True, null=True)
    proveedorNombre = models.CharField(max_length=30)
    proveedorTelefono = models.IntegerField()
    planta = models.CharField(max_length=100)

    #funcion que muestra el nombre que se visualiza
    def __str__(self):
         return str(self.numeroSerie)


#modelo de la clase empleado
class Empleado(models.Model):
    DNI = models.CharField(max_length=9, unique=TRUE)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telfono = models.IntegerField()

    #funcion que muestra el nombre que se visualiza
    def __str__(self):
        return str(self.DNI)



#modelo de la clase ticket
NIVEL_URGENCIA_CHOICES = [
    ('ALTO', 'Alto'),
    ('MEDIO', 'Medio'),
    ('BAJO', 'Bajo'),
]

TIPO_TICKET_CHOICES = [
    ('AVERIA', 'Avería'),
    ('MEJORA', 'Mejora'),
    ('MANTENIMIENTO', 'Mantenimiento'),
]

ESTADO_TICKET_CHOICES = [
    ('ABIERTO', 'Abierto'),
    ('CERRADO', 'Cerrado'),
    ('BLOQUEADO', 'Bloqueado'),
    ('SUSPENDIDO', 'Suspendido'),
]

class Ticket(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    numeroReferencia = models.IntegerField(unique=TRUE)
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    fechaApertura = models.DateField(blank=True, null=True)
    fechaResolucion = models.DateField(blank=True, null=True)
    nivelUrgencia = models.CharField(max_length=5, choices = NIVEL_URGENCIA_CHOICES, default='MEDIO')
    tipoTicket = models.CharField(max_length=20, choices = TIPO_TICKET_CHOICES, default='MANTENIMIENTO')
    estado = models.CharField(max_length=30, choices = ESTADO_TICKET_CHOICES, default='ABIERTO')
    comentarios = models.CharField(max_length=500)

    #funcion que muestra el nombre que se visualiza
    def __str__(self):
        return str(self.numeroReferencia)
    
