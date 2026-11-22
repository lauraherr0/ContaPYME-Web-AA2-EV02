from django import forms
from django.contrib.auth.hashers import make_password

from .models import Empresa, Rol, Usuario


class RegistroUsuario(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField(max_length=100)
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all())
    rol = forms.ModelChoiceField(queryset=Rol.objects.all())
    password = forms.CharField(
        label="Contraseña", min_length=8, max_length=128, strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    estado = forms.TypedChoiceField(
        choices=[("1", "Activo"), ("0", "Inactivo")],
        coerce=lambda valor: valor == "1", initial="1",
    )

    def guardar(self):
        datos = self.cleaned_data.copy()
        datos["password"] = make_password(datos["password"])
        return Usuario.objects.create(**datos)


class FiltroUsuarios(forms.Form):
    q = forms.CharField(label="Buscar nombre o correo", required=False, max_length=100)
    estado = forms.ChoiceField(
        required=False, choices=[("", "Todos"), ("1", "Activo"), ("0", "Inactivo")],
    )


class EdicionUsuario(RegistroUsuario):
    def __init__(self, *args, usuario, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario
        self.fields["password"].required = False
        self.fields["password"].help_text = "Déjala vacía para conservar la contraseña."

    def guardar(self):
        datos = self.cleaned_data.copy()
        password = datos.pop("password")
        if password:
            datos["password"] = make_password(password)
        Usuario.objects.filter(pk=self.usuario.pk).update(**datos)
