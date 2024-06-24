# noticias/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Esta es la ruta para la URL raíz
    path('index', views.index, name='index'),  # Esto es redundante si solo deseas '/index'
    path('crud', views.crud, name='crud'),
    # Otras rutas de tu aplicación noticias
]

