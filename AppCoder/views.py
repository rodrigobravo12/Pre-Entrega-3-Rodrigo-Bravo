from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user:

                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Hola {user}!!!"})
            
        else:

                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
            
    else:

            form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"formulario":form})


def aboutMe(request):

    return render(request, "AppCoder/aboutme.html")



def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario creado"})
    else:

        form = UsuarioRegistro()

    return render(request, "AppCoder/registro.html", {"formulario":form})

@login_required
def cierreSesion(request):

    logout(request)

    return render(request, "AppCoder/logout.html", {"mensaje":"Cerraste sesión"})


@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppCoder/inicio.html")
   
    else:

        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })

    return render(request, "AppCoder/editarUsuario.html", {"formulario":form, "usuario":usuario})



def inicio(request):
    
    return render(request, "AppCoder/inicio.html")


def equipo(request):

    return render(request, "AppCoder/equipos.html")


def jugador(request):

    return render(request, "AppCoder/jugadores.html") 


def tecnico(request):

    return render(request, "AppCoder/tecnicos.html")


def competencia(request):
    return render(request, "AppCoder/competencia.html")




@login_required
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


@login_required
def jugadorFormulario(request):

    if request.method == "POST":
        
        formulario1 = JugadorFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            jugador = Jugador(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"], posicion=info["posicion"])

            jugador.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario1 = JugadorFormulario()

    return render(request, "AppCoder/jugadores.html", {"form1":formulario1})


@login_required
def tecnicoFormulario(request):

    if request.method == "POST":
        
        formulario1 = TecnicoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            tecnico = Tecnico(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"])

            tecnico.save()

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


@login_required
def competenciaFormulario(request):

    if request.method == "POST":
        
        formulario1 = CompetenciaFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            competencia = Competencia(nombre=info["nombre"], sede=info["sede"])

            competencia.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario1 = CompetenciaFormulario()

    return render(request, "AppCoder/competencias.html", {"form1":formulario1})


@login_required
def leerJugadores(request):

    jugadores = Jugador.objects.all

    contexto = {"jugadores": jugadores}

    return render(request, "AppCoder/leerJugadores.html", contexto)


@login_required
def leerEquipos(request):

    equipos = Equipo.objects.all

    contexto = {"equipos": equipos}

    return render(request, "AppCoder/leerEquipos.html", contexto)


@login_required
def leerTecnicos(request):

    tecnicos = Tecnico.objects.all

    contexto = {"tecnicos": tecnicos}

    return render(request, "AppCoder/leerTecnicos.html", contexto)


@login_required
def leerCompetencias(request):

    competencias = Competencia.objects.all

    contexto = {"competencias": competencias}

    return render(request, "AppCoder/leerCompetencias.html", contexto)


@login_required
def eliminarJugadores(request, jugadorNombre):

    jugador = Jugador.objects.get(nombre=jugadorNombre)
    jugador.delete()

    jugadores = Jugador.objects.all()

    contexto = {"jugadores":jugadores}

    return render(request, "AppCoder/leerJugadores.html", contexto)


@login_required
def eliminarEquipos(request, equipoNombre):

    equipo = Equipo.objects.get(nombre=equipoNombre)
    equipo.delete()

    equipos = Equipo.objects.all()

    contexto = {"equipos":equipos}

    return render(request, "AppCoder/leerEquipos.html", contexto)


@login_required
def eliminarTecnicos(request, tecnicoNombre):

    tecnico = Tecnico.objects.get(nombre=tecnicoNombre)
    tecnico.delete()

    tecnicos = Tecnico.objects.all()

    contexto = {"tecnicos":tecnicos}

    return render(request, "AppCoder/leerTecnicos.html", contexto)


@login_required
def eliminarCompetencias(request, competenciaNombre):

    competencia = Competencia.objects.get(nombre=competenciaNombre)
    competencia.delete()

    competencias = Competencia.objects.all()

    contexto = {"competencias":competencias}

    return render(request, "AppCoder/leerCompetencias.html", contexto)


@login_required
def editarJugadores(request, jugadorNombre):
    
    jugador = Jugador.objects.get(nombre=jugadorNombre)

    if request.method == "POST":

        formulario1 = JugadorFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            jugador.nombre = info["nombre"]
            jugador.apellido = info["apellido"]
            jugador.correo = info ["correo"]
            jugador.posicion = info["posicion"]    

            jugador.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario1 = JugadorFormulario(initial={"nombre":jugador.nombre, "apellido":jugador.apellido,
        "correo":jugador.correo, "posicion":jugador.posicion})

    return render(request, "AppCoder/editarJugadores.html", {"form1":formulario1, "nombre":jugadorNombre})


@login_required
def editarEquipos(request, equipoNombre):
    
    equipo = Equipo.objects.get(nombre=equipoNombre)

    if request.method == "POST":

        formulario1 = EquipoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            equipo.nombre = info["nombre"]
            equipo.fechaInscripcion = info["fechaInscripcion"]
             
            equipo.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario1 = EquipoFormulario(initial={"nombre":equipo.nombre, "fechaInscripcion":equipo.fechaInscripcion})

    return render(request, "AppCoder/editarEquipos.html", {"form1":formulario1, "nombre":equipoNombre})


@login_required
def editarTecnicos(request, tecnicoNombre):
    
    tecnico = Tecnico.objects.get(nombre=tecnicoNombre)

    if request.method == "POST":

        formulario1 = TecnicoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            tecnico.nombre = info["nombre"]
            tecnico.apellido = info["apellido"]
            tecnico.correo = info["correo"]
             
            tecnico.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario1 = TecnicoFormulario(initial={"nombre":tecnico.nombre, "apellido":tecnico.apellido,
        "correo":tecnico.correo})

    return render(request, "AppCoder/editarTecnicos.html", {"form1":formulario1, "nombre":tecnicoNombre})


@login_required
def editarCompetencias(request, competenciaNombre):
    
    competencia = Competencia.objects.get(nombre=competenciaNombre)

    if request.method == "POST":

        formulario1 = CompetenciaFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            competencia.nombre = info["nombre"]
            competencia.sede = info["sede"]
                         
            competencia.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario1 = CompetenciaFormulario(initial={"nombre":competencia.nombre, "sede":competencia.sede})

    return render(request, "AppCoder/editarCompetencias.html", {"form1":formulario1, "nombre":competenciaNombre})



@login_required
def agregarAvatar(request):

    if request.method == "POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "AppCoder/inicio.html")
        
    else:

        form = AvatarFormulario()

    return render(request, "AppCoder/agregarAvatar.html", {"formulario":form})