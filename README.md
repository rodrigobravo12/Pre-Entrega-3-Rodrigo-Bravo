# Proyecto Final-Rodrigo-Bravo
Proyecto Final creado para el curso de Python de Coderhouse

## Superusuario
user: rbravo
password: rodriboca2000

## Descripción

El proyecto se trata de una página web de un torneo de fútbol online similar a "Fútbol Manager".
Los jugadores pueden crear equipos, crear jugadores, crear torneos, ser managers o crear managers
y divertirse con un juego de simulación.

## Orden

1. Primero hacer las migraciones si es necesario: `python manage.py makemigrations`
2. Luego de las migraciones: `python manage.py migrate`
3. Finalmente se debe correr el servidor: `python manage.py runserver`

## URLS

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
