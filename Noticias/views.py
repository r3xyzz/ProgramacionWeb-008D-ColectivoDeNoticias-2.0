from django.shortcuts import render
from .models import Noticia, Carrito, ProductoAdicional, Suscripcion, Categoria
from django.contrib.auth.models import User
from .forms import CategoriaForm

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


#Formularios para agregar datos
def FormNoticia(request):
    context={}
    return render(request, 'FormNoticia.html', context)


# Pagina de prueba
def Test(request):
    noticias = Noticia.objects.all()
    carritos = Carrito.objects.all()
    usuarios = User.objects.all()
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
def crud_categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    print("enviado datos categorias_list")
    return render(request, 'test.html',context)

def categoriasAdd(request):
    print("controlador categoriasAdd...")
    context={}
    
    if request.method == "POST":
        print("es un POST...")
        form = CategoriaForm(request.POST)
        if form.is_valid:
            print("estoy en agregar...")
            form.save()
            
            #limpiar form
            form=CategoriaForm()
            
            context={'mensaje':"Ok, datos grabados...","form":form}
            return render(request,"categorias_add.html",context)
    else:
        form = CategoriaForm()
        context={'form':form}
        return render(request, 'categorias_add.html',context)

#Noticias SIN TERMINAR- CRUD

def noticiasAdd(request):
    if request.method != "POST":
        categorias=Categoria.objects.all()
        context={"categorias":categorias}
        return render(request, 'FormNoticia.html', context)
    
    else:
        titulo_noticia=request.POST.get('titulo_noticia', False)
        subtitulo_noticia=request.POST.get('subtitulo_noticia', False)
        imagen_noticia=request.POST.get('imagen_noticia', False)
        descImg_noticia=request.POST.get('descImg_noticia', False)
        cuerpo_noticia=request.POST.get('cuerpo_noticia', False)
        nom_categoria=request.POST.get('nom_categoria', False)
            
        objCategoria=Categoria.objects.get(id = nom_categoria)
        obj=Noticia.objects.create(  titulo_noticia=titulo_noticia,
                                    subtitulo_noticia=subtitulo_noticia,
                                    imagen_noticia=imagen_noticia,
                                    descImg_noticia=descImg_noticia,
                                    cuerpo_noticia=cuerpo_noticia,
                                    nom_categoria=objCategoria,
                                    )
        obj.save()
        context={'mensaje':"Ok, datos grabados..."}
        return render(request, 'FormNoticia.html', context)


