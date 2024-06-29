# noticias/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Esta es la ruta para la URL raíz
    path('index', views.index, name='index'),  # Esto es redundante si solo deseas '/index'
    path('crud', views.crud, name='crud'),
    path('noticiasAdd', views.noticiasAdd, name='noticiasAdd'),
    path('noticias_del/<str:pk>', views.noticias_del, name='noticias_del'),
    # Otras rutas de la aplicación noticias
]

