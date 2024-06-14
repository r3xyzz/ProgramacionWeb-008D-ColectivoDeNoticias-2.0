from django.shortcuts import render
from .models import Noticia, Carrito, ProductoAdicional, Suscripcion, Categoria, Usuario

# IMPORTANTE MODELS, VIEWS, TEMPLATES

# Create your views here.

def principal(request):
    context={}
    return render(request, 'principal.html', context)

def carrito(request):
    context={}
    return render(request, 'carrito.html', context)

def contacto(request):
    context={}
    return render(request, 'contacto.html', context)

def logincaosnew(request):
    context={}
    return render(request, 'logincaosnew.html', context)

def FormNoticia(request):
    context={}
    return render(request, 'FormNoticia.html', context)

# Pagina de prueba
def Test(request):
    noticias = Noticia.objects.all()
    carritos = Carrito.objects.all()
    usuarios = Usuario.objects.all()
    productoAdicionales = ProductoAdicional.objects.all()
    categorias = Categoria.objects.all()
    subscripciones = Suscripcion.objects.all()

    context = {
        "subscripciones": subscripciones,
        "categorias": categorias,
        "productoAdicionales": productoAdicionales,
        "usuarios": usuarios,
        "carritos": carritos,
        "noticias": noticias
    }
    return render(request, 'test.html', context)

#Importación de las Noticias :-P

#Deportes
def noticia_esport(request):
    context={}
    return render(request, 'noticias/deportes/noticia_esport.html', context)
def noticia_furbo(request):
    context={}
    return render(request, 'noticias/deportes/noticia_furbo.html', context)
def noticia_karate(request):
    context={}
    return render(request, 'noticias/deportes/noticia_karate.html', context)

#Internacional
def noticia_hospital(request):
    context={}
    return render(request, 'noticias/internacional/noticia_hospital.html', context)
def noticia_incendio(request):
    context={}
    return render(request, 'noticias/internacional/noticia_incendio.html', context)

#Nacional
def noticia_carabinero(request):
    context={}
    return render(request, 'noticias/nacional/noticia_carabinero.html', context)
def noticia_mascotas(request):
    context={}
    return render(request, 'noticias/nacional/noticia_mascotas.html', context)
def noticia_prestamo(request):
    context={}
    return render(request, 'noticias/nacional/noticia_prestamo.html', context)

#Politica
def noticia_diputado(request):
    context={}
    return render(request, 'noticias/politica/noticia_diputado.html', context)
def noticia_gobierno(request):
    context={}
    return render(request, 'noticias/politica/noticia_gobierno.html', context)

#Cositas CRUD
def crud(request):
    noticias = noticias.objects.all()
    context = {'noticias': noticias}
    return render(request, 'test.html',context)

#Noticias SIN TERMINAR- CRUD
def noticiasAdd(request):
    if request.method is not "POST":

        return render(request, 'test.html', context)

