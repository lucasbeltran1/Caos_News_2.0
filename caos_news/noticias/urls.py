# noticias/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('crud', views.crud, name='crud'),
    #path('noticiasAdd', views.noticiasAdd, name='noticiasAdd'),
]
