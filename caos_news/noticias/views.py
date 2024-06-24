from django.shortcuts import render
from .models import Noticia

def index(request):
    context = {}
    return render(request, 'noticias/index.html', context)

def crud(request):
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}
    return render(request, 'noticias/lista_noticias.html', context)
