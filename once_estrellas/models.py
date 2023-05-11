from django.db import models

# Create your models here.
class Estacionamiento(models.Model):
    nombre = models.CharField(max_length=64)  # Equivalente de str
    apellido = models.CharField(max_length=64)
    cedula_de_identidad = models.CharField(max_length=32)
    numero_socio_socia = models.CharField(max_length=128)
    numero_estacionamiento = models.IntegerField()  # Equivalent de int


class Alquiler_salones(models.Model):
    tipo_salon = models.CharField(max_length=256)
    turno = models.CharField(max_length=256)
    precio_socio_socia = models.IntegerField()
    precio_nosocio_nosocia = models.IntegerField()


class Actividades(models.Model):
    nombre = models.CharField(max_length=256)
    Días = models.CharField(max_length=32)
    horario = models.TimeField()
    numero_socio_socia = models.CharField(max_length=128)
    


class Socios_socias(models.Model):
    nombre = models.CharField(max_length=64)  # Equivalente de str
    apellido = models.CharField(max_length=64)
    cedula_de_identidad = models.CharField(max_length=32)
    telefono = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    numero_socio_socia = models.CharField(max_length=128)

    #vigente = models.BooleanField(default=False)  # equivalente a bool (True, False)