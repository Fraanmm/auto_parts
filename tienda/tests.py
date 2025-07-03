import pytest
from tienda.models_test import (
    ClienteB2C, ClienteB2B, Administrador
)


@pytest.mark.django_db
def test_cliente_b2c_creacion():
    cliente = ClienteB2C.objects.create(
        nombre="María",
        apellido="López",
        rut="12345678-9",
        telefono="987654321",
        correo="maria@example.com",
        contrasena="segura123"
    )
    assert cliente.nombre == "María"
    assert cliente.rut == "12345678-9"

@pytest.mark.django_db
def test_cliente_b2b_creacion():
    empresa = ClienteB2B.objects.create(
        nombre_empresa="Repuestos S.A.",
        rut_empresa="76321123-0",
        direccion="Av. Industriales 1000",
        telefono="223344556",
        correo_empresa="ventas@repuestos.cl",
        contrasena="empresasegura"
    )
    assert empresa.nombre_empresa == "Repuestos S.A."
    assert empresa.rut_empresa.startswith("7632")


@pytest.mark.django_db
def test_administrador_creacion():
    admin = Administrador.objects.create(
        nombre="Superadmin",
        correo="admin@autoparts.cl",
        contrasena="adminsecure"
    )
    assert admin.nombre == "Superadmin"
    assert admin.correo.endswith("@autoparts.cl")

