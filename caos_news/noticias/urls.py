# noticias/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Esta es la ruta para la URL raíz
    path('index', views.index, name='index'),  # Esto es redundante si solo deseas '/index'
    path('apifutbol/', views.apifutbol, name='apifutbol'),
    path('cine/', views.cine, name='cine'),
    path('compra/', views.compra, name='compra'),
    path('deporte/', views.deporte, name='deporte'),
    path('espectaculo/', views.espectaculo, name='espectaculo'),
    path('formulario/', views.formulario, name='formulario'),
    path('lista_noticias/', views.lista_noticias, name='lista_noticias'),
    path('musica/', views.musica, name='musica'),
    path('noticia_editar/', views.noticia_editar, name='noticia_editar'),
    path('publicar/', views.publicar, name='publicar'),
    path('videojuegos/', views.videojuegos, name='videojuegos'),
    path('crud', views.crud, name='crud'),
    path('crud/', views.crud, name='crud'),
    path('noticiasAdd', views.noticiasAdd, name='noticiasAdd'),
    path('noticias_del/<str:pk>', views.noticias_del, name='noticias_del'),
    path('noticias_findEdit/<str:pk>', views.noticias_findEdit, name='noticias_findEdit'),
    path('noticiasUpdate',views.noticiasUpdate, name='noticiasUpdate')
    # Otras rutas de la aplicación noticias
]

