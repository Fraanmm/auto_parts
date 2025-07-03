from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/costo-envio/', views.obtener_costo_envio_carrito, name='calcular_costo_envio'),
    path('api/productos/', views.api_productos, name='api_productos'),


    # Usuario normal
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('homemayorista/', views.homemayorista, name='homemayorista'),
    path('logout_mayorista/', views.logout_mayorista, name='logout_mayorista'),
    path('perfil_cliente/', views.perfil_cliente, name='perfil_cliente'),
    path('agregar_al_carrito/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('catalogo/', views.catalogo_b2c, name='catalogo_b2c'),
    path('logincliente/', views.login_cliente, name='logincliente'),
    path('carrito_cliente/', views.carrito_cliente, name='carrito_cliente'),
    path('simular_pago/', views.simular_pago, name='simular_pago'),
    path('generar_compra/', views.generar_compra, name='generar_compra'),
    path('boleta/<int:id>/', views.descargar_boleta, name='boleta_pdf'),
    path('procesar_compra/', views.procesar_compra_cliente, name='procesar_compra'),
    path('detalleproducto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('marca/<str:nombre>/', views.catalogo_por_marca, name='catalogo_por_marca'),
    path('iniciar_pago_webpay/', views.iniciar_pago_webpay, name='iniciar_pago_webpay'),
    path('webpay/return/', views.webpay_return, name='webpay_return'),
    path('procesar_compra_exitosa/', views.procesar_compra_exitosa, name='procesar_compra_exitosa'),
    path('informacion/<str:seccion>/', views.mostrar_informacion, name='mostrar_informacion'),
    path('ver_comunas/', views.ver_comunas_chilexpress, name='ver_comunas'),
    path('ver_regiones/', views.ver_regiones_disponibles, name='ver_regiones'),
    #path('vaciar-carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    path('eliminar-item-carrito/', views.eliminar_item_carrito, name='eliminar_item_carrito'),









    # Comprador mayorista
    path('registromayorista/', views.registro_mayorista, name='registromayorista'),
    path('loginmayorista/', views.login_mayorista, name='loginmayorista'),
    path('detalleproducto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('categoria/<str:categoria_nombre>/', views.categoria, name='categoria'),
    path('perfil_empresa/', views.perfil_empresa, name='perfil_empresa'),
    path('catalogo_empresa/', views.catalogo_empresa, name='catalogo_empresa'),
    path('detalle_empresa/<int:id>/', views.detalle_producto_empresa, name='detalle_producto_empresa'),
    path('agregar_carrito_empresa/', views.agregar_al_carrito_empresa, name='agregar_al_carrito_empresa'),
    path('cotizacion_empresa/', views.cotizacion_empresa, name='cotizacion_empresa'),
    path('generar_cotizacion_empresa/', views.generar_cotizacion_empresa, name='generar_cotizacion_empresa'),
    path('mis_cotizaciones_empresa/', views.mis_cotizaciones_empresa, name='mis_cotizaciones_empresa'),
    path('descargar_cotizacion/<int:id>/', views.descargar_cotizacion_pdf, name='descargar_cotizacion_pdf'),
    path('seguimiento_empresa/', views.seguimiento_empresa, name='seguimiento_empresa'),


    #Admin
    path('panel_admin/', views.panel_admin, name='panel_admin'),
    path('loginadmin/', views.login_admin, name='login_admin'),
    path('editar_b2c/<int:id>/', views.editar_b2c, name='editar_b2c'),
    path('eliminar_b2c/<int:id>/', views.eliminar_b2c, name='eliminar_b2c'),
    path('editar_b2b/<int:id>/', views.editar_b2b, name='editar_b2b'),
    path('eliminar_b2b/<int:id>/', views.eliminar_b2b, name='eliminar_b2b'),
    path('editar_cotizacion/<int:id>/', views.editar_cotizacion, name='editar_cotizacion'),
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

]
