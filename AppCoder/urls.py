from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("equipos/", equipo, name="Equipo"),
    path("jugadores/", jugador, name="Jugador"),
    path("tecnicos/", tecnico, name="Tecnico"),
    path("equipoFormulario/", equipoFormulario, name="EquipoFormulario"),
    path("jugadorFormulario/", jugadorFormulario, name="JugadorFormulario"),
    path("tecnicoFormulario/", tecnicoFormulario, name="TecnicoFormulario"),
    path("buscar_equipo/", buscar_equipo),
    path("resultados/", resultados_equipo),
]
