from django.db import models

# Create your models here.

class Equipo(models.Model):

    nombre = models.CharField(max_length=60)
    fechaInscripcion = models.DateField()
    

class Jugador(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()
    posicion = models.CharField(max_length=60)


class Tecnico(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()



