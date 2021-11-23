from django.urls import path
from .import views
from .views import agregar_material, listar_material

urlpatterns = [
    path('', views.home),
    path('top', views.top),
    path('registro', views.registro, name='registro'),
    path('agregar-material/', agregar_material, name="agregar_producto"),
    path('listar-material/', listar_material, name="listar_material"), 
]