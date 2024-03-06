from django import forms

class EquipoFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    fechaInscripcion = forms.DateField()

class JugadorFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    correo = forms.EmailField()
    posicion = forms.CharField(max_length=60)


class TecnicoFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    correo = forms.EmailField()