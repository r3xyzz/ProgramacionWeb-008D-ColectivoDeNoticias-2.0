from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from Noticias.views import register_view, noticiasAdd, noticiaDel

urlpatterns = [
    # Otras rutas existentes
    path('', views.principal, name='principal'),
    path('carrito', views.carrito, name='carrito'),
    path('contacto', views.contacto, name='contacto'),
    path('categoriasAdd', views.categoriasAdd, name='categoriasAdd'),
    path('test.html', views.Test, name='test'),
    path('buscar/', views.buscar_noticias, name='buscar_noticias'),
    path('noticiascaosnew/', views.noticiascaosnew, name='noticiascaosnew'),
    path('resgistrocaosnew', register_view, name='resgistrocaosnew'),

    path('noticiaDel/', noticiaDel, name='noticiaDel'),
    

    

    # Ruta para la búsqueda
    # path('buscar/', views.buscar, name='buscar'),

    # Otras rutas existentes
    path('noticias/deportes/noticia_esport', views.noticia_esport, name='noticia_esport'),
    path('noticias/deportes/noticia_furbo', views.noticia_furbo, name='noticia_furbo'),
    path('noticias/deportes/noticia_karate', views.noticia_karate, name='noticia_karate'),

    path('noticias/internacional/noticia_hospital', views.noticia_hospital, name='noticia_hospital'),
    path('noticias/internacional/noticia_incendio', views.noticia_incendio, name='noticia_incendio'),

    path('noticias/nacional/noticia_carabinero', views.noticia_carabinero, name='noticia_carabinero'),
    path('noticias/nacional/noticia_mascotas', views.noticia_mascotas, name='noticia_mascotas'),
    path('noticias/nacional/noticia_prestamo', views.noticia_prestamo, name='noticia_prestamo'),

    path('noticias/politica/noticia_diputado', views.noticia_diputado, name='noticia_diputado'),
    path('noticias/politica/noticia_gobierno', views.noticia_gobierno, name='noticia_gobierno'),

    path('crud_categorias', views.crud_categorias, name='crud_categorias'),
    path('FormNoticia/', views.noticiasAdd, name='formNoticia'),
    path('crudNoticias', views.crudNoticias, name='crudNoticias'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)