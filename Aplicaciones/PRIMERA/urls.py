from django.urls import path, include, re_path
from .import views
from .views import agregar_material, listar_material
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home),
    path('quienessomos', views.qs),
    path('registro', views.registro, name='registro'),
    path('agregar-material/', views.agregar_material, name="agregar_material"),
    path('listar-material/', listar_material, name="listar_material"), 
    path('detalle', views.detalle),
    #path('detalle?id=<id>',views.detalle),
    path("buscar", views.search, name="buscar"),
    path('agregar_comentario', views.agregar_comentario, name="agregar_comentario"),
    #re_path(r'^agregar_comentario?id=(?P<id>\d+)$', views.agregar_comentario, name='agregar_comentario'),
    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns ()