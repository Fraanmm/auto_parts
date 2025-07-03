from django.contrib import admin
from .models import (
    Producto,
    ClienteB2C,
    ClienteB2B,
    CotizacionEmpresa,
    DetalleCotizacionEmpresa
)

# Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'marca', 'categoria', 'precio', 'stock')
    search_fields = ('nombre', 'marca', 'categoria')
    list_filter = ('marca', 'categoria')

# Cliente B2C
@admin.register(ClienteB2C)
class ClienteB2CAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'apellido', 'rut', 'correo')
    search_fields = ('nombre', 'apellido', 'rut', 'correo')

# Cliente B2B
@admin.register(ClienteB2B)
class ClienteB2BAdmin(admin.ModelAdmin):
    list_display = ('id_cliente_b2b', 'nombre_empresa', 'rut_empresa', 'correo_empresa')
    search_fields = ('nombre_empresa', 'rut_empresa', 'correo_empresa')

# Cotización de empresas
@admin.register(CotizacionEmpresa)
class CotizacionEmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'total', 'estado')
    list_filter = ('estado',)
    search_fields = ('cliente__nombre_empresa',)

# Detalles de cotización
@admin.register(DetalleCotizacionEmpresa)
class DetalleCotizacionEmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cotizacion', 'producto', 'cantidad', 'precio_unitario', 'subtotal')
    search_fields = ('cotizacion__cliente__nombre_empresa', 'producto__nombre')
