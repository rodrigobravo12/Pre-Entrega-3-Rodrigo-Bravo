from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} ------ Fecha Inscripción: {self.fechaInscripcion}"

    nombre = models.CharField(max_length=60)
    fechaInscripcion = models.DateField()
    

class Jugador(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} ------ Apellido: {self.apellido} ------ Correo: {self.correo} ------ Posicion: {self.posicion}"  


    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()
    posicion = models.CharField(max_length=60)


class Tecnico(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} ------ Apellido: {self.apellido} ------ Correo: {self.correo}"

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()

class Competencia(models.Model):

    def __str__(self):
        
        return f"Nombre: {self.nombre} ------ Sede: {self.sede}"

    nombre = models.CharField(max_length=60)
    sede = models.CharField(max_length=60)


class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    




