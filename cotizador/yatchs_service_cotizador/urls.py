from django.urls import path
from yatchs_service_cotizador import views

urlpatterns = [
    path('', views.cotizador, name="home"),
    path('servicio/', views.crear_servicio ,name="crear_servicio"),
    path('producto/', views.crear_producto ,name="crear_producto"),
    path('empresa/', views.crear_empresa ,name="crear_empresa"),
    path('cliente/', views.crear_cliente ,name="crear_cliente"),
    path('agente/', views.crear_agente ,name="crear_agente"),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name="eliminar_cliente"),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name="eliminar_producto"),
    path('eliminar_servicio/<int:servicio_id>/', views.eliminar_servicio, name="eliminar_servicio"),
    path('eliminar_empresa/<int:empresa_id>/', views.eliminar_empresa, name="eliminar_empresa"),
    path('eliminar_agente/<int:agente_id>/', views.eliminar_agente, name="eliminar_agente"),
    path('cotizacion/', views.guardar_cotizacion, name="guardar_cotizacion"),
    path('detalle_cotizacion/<int:cotizacion_id>/', views.detalle_cotizacion, name="detalle_cotizacion"),
    path('cotizacion_pdf/<int:cotizacion_id>/', views.crear_pdf, name="crear_pdf"),
]