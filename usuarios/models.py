from django.db import models


class Empresa(models.Model):
    id = models.AutoField(primary_key=True, db_column="Id_Empresa")
    nombre = models.CharField(max_length=100, db_column="Nombre")

    class Meta:
        managed = False
        db_table = "empresa"
        ordering = ["nombre", "id"]

    def __str__(self):
        return f"{self.nombre} ({self.id})"


class Rol(models.Model):
    id = models.AutoField(primary_key=True, db_column="Id_Rol")
    nombre = models.CharField(max_length=50, db_column="Nombre")

    class Meta:
        managed = False
        db_table = "rol"
        ordering = ["nombre", "id"]

    def __str__(self):
        return f"{self.nombre} ({self.id})"


class Usuario(models.Model):
    id = models.AutoField(primary_key=True, db_column="Id_Usuario")
    empresa = models.ForeignKey(Empresa, models.PROTECT, db_column="Id_Empresa")
    rol = models.ForeignKey(Rol, models.PROTECT, db_column="Id_Rol")
    nombre = models.CharField(max_length=100, db_column="Nombre")
    correo = models.EmailField(max_length=100, db_column="Correo")
    password = models.CharField(max_length=255, db_column="Password")
    estado = models.BooleanField(null=True, db_column="Estado")

    class Meta:
        managed = False
        db_table = "usuario"
        ordering = ["-id"]
