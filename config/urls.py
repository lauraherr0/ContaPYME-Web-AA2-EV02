from django.urls import path
from usuarios.views import editar, eliminar, usuarios

urlpatterns = [
    path("", usuarios, name="usuarios"),
    path("usuarios/<int:pk>/editar/", editar, name="editar"),
    path("usuarios/<int:pk>/eliminar/", eliminar, name="eliminar"),
]
