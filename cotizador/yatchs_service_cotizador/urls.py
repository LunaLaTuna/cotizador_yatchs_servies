from django.urls import path
from yatchs_service_cotizador import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.cotizador, name="home"),
    path('servicio/', views.crear_servicio ,name="crear_servicio"),
    path('producto/', views.crear_producto ,name="crear_producto"),
    path('empresa/', views.crear_empresa ,name="crear_empresa"),
    path('cliente/', views.crear_cliente ,name="crear_cliente"),
    path('eliminar_cliente/<int:cliente_id>', views.eliminar_cliente, name="eliminar_cliente")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)