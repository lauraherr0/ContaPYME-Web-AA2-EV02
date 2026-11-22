import logging

from django.db import DatabaseError, IntegrityError
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from .forms import EdicionUsuario, FiltroUsuarios, RegistroUsuario
from .models import Usuario

logger = logging.getLogger(__name__)


@require_http_methods(["GET", "POST"])
def usuarios(request):
    formulario = RegistroUsuario(request.POST if request.method == "POST" else None)
    filtro = FiltroUsuarios(request.GET)
    try:
        if request.method == "POST" and formulario.is_valid():
            try:
                formulario.guardar()
            except IntegrityError:
                formulario.add_error(None, "No se pudo guardar. Revisa la empresa, el rol y los datos.")
            else:
                return HttpResponseRedirect(reverse("usuarios") + "?guardado=1")

        registros = Usuario.objects.select_related("empresa", "rol").defer("password")
        if filtro.is_valid():
            texto = filtro.cleaned_data["q"]
            estado = filtro.cleaned_data["estado"]
            if texto:
                registros = registros.filter(Q(nombre__icontains=texto) | Q(correo__icontains=texto))
            if estado:
                registros = registros.filter(estado=estado == "1")

        return render(request, "usuarios/listado.html", {
            "formulario": formulario,
            "filtro": filtro,
            "registros": list(registros[:100]),
            "guardado": request.method == "GET" and request.GET.get("guardado") == "1",
        })
    except DatabaseError:
        logger.exception("Error de acceso a MySQL")
        return render(request, "usuarios/error.html", status=503)


@require_http_methods(["GET", "POST"])
def editar(request, pk):
    usuario = get_object_or_404(Usuario.objects.defer("password"), pk=pk)
    formulario = EdicionUsuario(
        request.POST if request.method == "POST" else None,
        usuario=usuario,
        initial={
            "nombre": usuario.nombre, "correo": usuario.correo,
            "empresa": usuario.empresa_id, "rol": usuario.rol_id,
            "estado": "" if usuario.estado is None else str(int(usuario.estado)),
        },
    )
    if request.method == "POST" and formulario.is_valid():
        try:
            formulario.guardar()
        except IntegrityError:
            formulario.add_error(None, "No se pudo actualizar. Revisa los datos.")
        else:
            return HttpResponseRedirect(reverse("usuarios"))
    return render(request, "usuarios/accion.html", {
        "titulo": "Editar usuario", "usuario": usuario, "formulario": formulario,
    })


@require_http_methods(["GET", "POST"])
def eliminar(request, pk):
    usuario = get_object_or_404(Usuario.objects.defer("password"), pk=pk)
    error = ""
    if request.method == "POST":
        try:
            usuario.delete()
        except IntegrityError:
            error = "El usuario está vinculado a otros registros y no se puede eliminar."
        else:
            return HttpResponseRedirect(reverse("usuarios"))
    return render(request, "usuarios/accion.html", {
        "titulo": "Eliminar usuario", "usuario": usuario, "error": error,
    })
