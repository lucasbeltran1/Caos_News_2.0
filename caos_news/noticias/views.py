# noticias/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia

def index(request):
    context={}
    return render(request, 'templates/index.html', context)

def crud(request):
    noticias = Noticia.objects.all()
    context = {'noticias' : noticias}
    return render(request, 'lista_noticias.html', context)
