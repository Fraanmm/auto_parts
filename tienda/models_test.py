from django.db import models

class ClienteB2C(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)

    class Meta:
        app_label = 'tests'
        managed = True

class ClienteB2B(models.Model):
    id_cliente_b2b = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    rut_empresa = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=12)
    correo_empresa = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)

    class Meta:
        app_label = 'tests'
        managed = True

class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=100)

    class Meta:
        app_label = 'tests'
        managed = True
