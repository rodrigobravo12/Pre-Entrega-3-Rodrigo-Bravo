from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar


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

class CompetenciaFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    sede = forms.CharField(max_length=60)

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name","password1", "password2"]

class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name","password1", "password2"]


class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["imagen"]

        
