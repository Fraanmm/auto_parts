from tienda.models_test import (
    Producto, ClienteB2C, ClienteB2B, CompraCliente, DetalleCompraCliente,
    CotizacionEmpresa, DetalleCotizacionEmpresa, Administrador
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
def test_compra_cliente_y_detalle():
    cliente = ClienteB2C.objects.create(
        nombre="Carlos",
        apellido="Zúñiga",
        rut="22222222-2",
        telefono="912345678",
        correo="carlos@dominio.cl",
        contrasena="clave"
    )
    producto = Producto.objects.create(
        nombre="Amortiguador",
        precio=25000,
        stock=10
    )
    compra = CompraCliente.objects.create(
        cliente=cliente,
        total=50000,
        estado="Pagado"
    )
    detalle = DetalleCompraCliente.objects.create(
        compra=compra,
        producto=producto,
        cantidad=2,
        precio_unitario=25000,
        subtotal=50000
    )
    assert detalle.compra.estado == "Pagado"
    assert detalle.cantidad == 2
    assert detalle.producto.nombre == "Amortiguador"

@pytest.mark.django_db
def test_cotizacion_empresa_y_detalle():
    cliente_b2b = ClienteB2B.objects.create(
        nombre_empresa="Autopartes Ltda",
        rut_empresa="76881123-5",
        direccion="Ruta 5 Norte, KM 20",
        telefono="998877665",
        correo_empresa="contacto@autopartes.cl",
        contrasena="autopwd"
    )
    producto = Producto.objects.create(
        nombre="Radiador",
        precio=45000,
        stock=15
    )
    cotizacion = CotizacionEmpresa.objects.create(
        cliente=cliente_b2b,
        total=90000,
        estado="Pendiente"
    )
    detalle = DetalleCotizacionEmpresa.objects.create(
        cotizacion=cotizacion,
        producto=producto,
        cantidad=2,
        precio_unitario=45000,
        subtotal=90000
    )
    assert cotizacion.estado == "Pendiente"
    assert detalle.subtotal == 90000

@pytest.mark.django_db
def test_administrador_creacion():
    admin = Administrador.objects.create(
        nombre="Superadmin",
        correo="admin@autoparts.cl",
        contrasena="adminsecure"
    )
    assert admin.nombre == "Superadmin"
    assert admin.correo.endswith("@autoparts.cl")

