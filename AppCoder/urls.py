from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("equipos/", equipo, name="Equipo"),
    path("jugadores/", jugador, name="Jugador"),
    path("tecnicos/", tecnico, name="Tecnico"),
    path("competencias/", competencia, name="Competencia"),
    path("equipoFormulario/", equipoFormulario, name="EquipoFormulario"),
    path("jugadorFormulario/", jugadorFormulario, name="JugadorFormulario"),
    path("tecnicoFormulario/", tecnicoFormulario, name="TecnicoFormulario"),
    path("competenciaFormulario/", competenciaFormulario, name="CompetenciaFormulario"),
    path("buscar_equipo/", buscar_equipo),
    path("resultados/", resultados_equipo),
    path("leerJugadores/", leerJugadores, name="leerJugadores"),
    path("leerEquipos/", leerEquipos, name="leerEquipos"),
    path("leerTecnicos/", leerTecnicos, name="leerTecnicos"),
    path("leerCompetencias/", leerCompetencias, name="leerCompetencias"),
    path("eliminarJugadores/<jugadorNombre>/", eliminarJugadores, name="EliminarJugador"),
    path("eliminarEquipos/<equipoNombre>/", eliminarEquipos, name="EliminarEquipo"),
    path("eliminarTecnicos/<tecnicoNombre>/", eliminarTecnicos, name="EliminarTecnico"),
    path("eliminarCompetencias/<competenciaNombre>/", eliminarCompetencias, name="EliminarCompetencia"),
    path("editarJugadores/<jugadorNombre>/", editarJugadores, name="EditarJugador"),
    path("editarEquipos/<equipoNombre>/", editarEquipos, name="EditarEquipo"),
    path("editarTecnicos/<tecnicoNombre>/", editarTecnicos, name="EditarTecnico"),
    path("editarCompetencias/<competenciaNombre>/", editarCompetencias, name="EditarCompetencia"),
    path("login/", inicioSesion, name="Login"),
    path("registro/", registro, name="Registro"),
    path("logout/", cierreSesion, name="CerrarSesion"),
    path("editarUsuario/", editarUsuario, name="EditarUsuario"),
    path("agregarAvatar/", agregarAvatar, name="AgregarAvatar" ),
    path("aboutme/", aboutMe, name= "AboutMe"),
   

]
