from django.urls import path
from .import views
from .views import agregar_material, listar_material
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home),
    path('top', views.top),
    path('registro', views.registro, name='registro'),
    path('agregar-material/', views.agregar_material, name="agregar_material"),
    path('listar-material/', listar_material, name="listar_material"), 
    path('detalle', views.detalle),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)