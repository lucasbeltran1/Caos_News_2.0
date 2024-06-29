from django.shortcuts import render
from .models import Noticia

def index(request):
    context = {}
    return render(request, 'noticias/index.html', context)

def crud(request):
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}
    return render(request, 'noticias/lista_noticias.html', context)

def noticiasAdd(request):
    if request.method is not "POST":
        #debido a que no es un post, se muestra el formulario el formulario para agregar
        context = {}
        return render(request, 'publicar.html', context)
    else:


        codigo=request.POST["rut"]
        titulo=request.POST['titulo']
        reportero=request.POST['reportero']
        descripcion=request.POST['descripcion']
        activo="1"

        obj=Noticia.objects.create( codigo=codigo,
                                    titulo=titulo,
                                    reportero=reportero,
                                    descripcion=descripcion,
                                    activo=1
                                    )
        obj.save()
        context={'mensaje' : "Datos guardados..."}
        return render(request, 'publicar.html', context)

def noticias_del(request,pk):
    context={}
    try:
        noticias=Noticia.objects.get(codigo=pk)

        noticia.delete()
        mensaje="Datos eliminados..."
        noticias = Noticia.objects.all()
        context = {'noticias': noticias,    'mensaje': mensaje}
        return render(request, 'lista_noticias.html', context)
    except:
        mensaje="Error, el código no existe..."
        noticias = Noticia.objects.all()
        context = {'noticias': noticias,  'mensaje': mensaje}
        return render(request, 'lista_noticias.html', context)
