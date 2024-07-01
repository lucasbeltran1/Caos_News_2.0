from django.shortcuts import render
from .models import Noticia

def index(request):
    context = {}
    return render(request, 'noticias/index.html', context)

def apifutbol(request):
    return render(request, 'noticias/apifutbol.html')

def cine(request):
    return render(request, 'noticias/cine.html')

def compra(request):
    return render(request, 'noticias/compra.html')

def deporte(request):
    return render(request, 'noticias/deporte.html')

def espectaculo(request):
    return render(request, 'noticias/espectaculo.html')

def formulario(request):
    return render(request, 'noticias/formulario.html')

def lista_noticias(request):
    return render(request, 'noticias/lista_noticias.html')

def musica(request):
    return render(request, 'noticias/musica.html')

def noticia_editar(request):
    return render(request, 'noticias/noticia_editar.html')

def publicar(request):
    return render(request, 'noticias/publicar.html')

def videojuegos(request):
    return render(request, 'noticias/videojuegos.html')



def crud(request):
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}
    return render(request, 'noticias/lista_noticias.html', context)

def noticiasAdd(request):
    if request.method != "POST":
        #debido a que no es un post, se muestra el formulario el formulario para agregar
        context = {}
        return render(request, 'noticias/publicar.html', context)
    else:


        codigo=request.POST["codigo"]
        titulo=request.POST['titulo']
        reportero=request.POST['reportero']
        descripcion=request.POST['descripcion']

        obj=Noticia.objects.create( codigo=codigo,
                                    titulo=titulo,
                                    reportero=reportero,
                                    descripcion=descripcion,
                                    )
        obj.save()
        context={'mensaje' : "Datos guardados..."}
        return render(request, 'noticias/publicar.html', context)

def noticias_del(request, pk):
    context = {}
    try:
        noticia = Noticia.objects.get(codigo=pk)  # Cambié 'noticias' a 'noticia'
        noticia.delete()
        mensaje = "Datos eliminados..."
        noticias = Noticia.objects.all()
        context = {'noticias': noticias, 'mensaje': mensaje}
    except Noticia.DoesNotExist:
        mensaje = "Error, el código no existe..."
        noticias = Noticia.objects.all()
        context = {'noticias': noticias, 'mensaje': mensaje}
    return render(request, 'noticias/lista_noticias.html', context)

def noticias_findEdit(request,pk):

    if pk != "":
        noticia=Noticia.objects.get(codigo=pk)
        
        context={'noticia':noticia}
        if noticia:
            return render(request, 'noticias/noticia_editar.html', context)
        else:
            context={'mensaje':"Error, el código no existe..."}
            return render(request, 'noticias/noticia_editar.html', context)
        
def noticiasUpdate(request):
    if request.method == "POST":
        #es un POST, por lo tanto, se recuperan los datos del formulario y las graban en una tabla
        codigo=request.POST["codigo"]
        titulo=request.POST['titulo']
        reportero=request.POST['reportero']
        descripcion=request.POST['descripcion']

        noticia= Noticia()
        noticia.codigo=codigo
        noticia.titulo=titulo
        noticia.reportero=reportero
        noticia.descripcion=descripcion
        noticia.save()

        context={'mensaje':"Datos actualizados...", 'noticia':noticia}
        return render(request, 'noticias/noticia_editar.html', context)
    else:
        #no es un post, nos mostraría el form de agregar
        noticias = Noticia.objects.all()
        context={'noticias':noticias}
        return render(request, 'noticias/lista_noticias.html', context)


