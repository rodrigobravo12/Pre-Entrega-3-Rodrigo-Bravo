from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

def inicio(request):
    
    return render(request, "AppCoder/inicio.html")

def equipo(request):

    return render(request, "AppCoder/equipos.html")

def jugador(request):

    return render(request, "AppCoder/jugadores.html") 

def tecnico(request):

    return render(request, "AppCoder/tecnicos.html")



def equipoFormulario(request):

    if request.method == "POST":
        
        formulario1 = EquipoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            equipo = Equipo(nombre=info["nombre"], fechaInscripcion=info["fechaInscripcion"])

            equipo.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario1 = EquipoFormulario()

    return render(request, "AppCoder/equipos.html", {"form1":formulario1})


def jugadorFormulario(request):

    if request.method == "POST":
        
        formulario1 = JugadorFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            equipo = Jugador(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"], posicion=info["posicion"])

            equipo.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario1 = JugadorFormulario()

    return render(request, "AppCoder/jugadores.html", {"form1":formulario1})


def tecnicoFormulario(request):

    if request.method == "POST":
        
        formulario1 = TecnicoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            equipo = Tecnico(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"])

            equipo.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario1 = TecnicoFormulario()

    return render(request, "AppCoder/tecnicos.html", {"form1":formulario1})

def buscar_equipo(request):

    return render(request, "AppCoder/buscar_equipo.html")

def resultados_equipo(request):

    if request.GET["nombre_equipo"]:

        equipo = request.GET["nombre_equipo"]

        resultados = Equipo.objects.filter(nombre__iexact=equipo)

        return render(request, "AppCoder/inicio.html", {"resultados":resultados, "nombre_equipo":equipo})
    
    else:
        respuesta = "No hay datos para tu búsqueda"

    return HttpResponse(respuesta)










    







