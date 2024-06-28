from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, Carrito, ProductoAdicional, Suscripcion, Categoria
from django.contrib.auth.models import User
from .models import Noticia
from .forms import CategoriaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import NoticiaForm

# IMPORTANTE MODELS, VIEWS, TEMPLATES

# Create your views here.

def register_view(request):
    print("DEBUG 1")
    if request.method == "POST":
        print("DEBUG 2: POST REQUEST")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("DEBUG 3: FORM VÁLIDO")
            form.save()
            return redirect('principal')
        else:
            print("DEBUG 4: FORM INVÁLIDO")
    else:
        print("DEBUG 5: GET REQUEST")
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "resgistrocaosnew.html", context)

def principal(request):
    context={}
    return render(request, 'principal.html', context)

@login_required
def carrito(request):
    context={}
    return render(request, 'carrito.html', context)

def contacto(request):
    context={}
    return render(request, 'contacto.html', context)

def login(request):
    context={}
    return render(request, 'registration/login.html', context)

@login_required
def noticiascaosnew(request):
    context={}
    return render(request, 'noticiascaosnew.html', context)

def buscar_noticias(request):
    query = request.GET.get('q', '').strip()
    if query:
        resultados = Noticia.objects.filter(titulo__icontains=query)
        return render(request, 'resultados_busqueda.html', {'resultados': resultados, 'query': query})
    else:
        return redirect('noticiascaosnew')


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

#Crud request noticias

def crudNoticias(request):
    noticias=Noticia.objects.all()
    context={"noticias":noticias}
    return render(request, 'noticiascaosnew.html', context)

#Noticias SIN TERMINAR- CRUD
def noticiasAdd(request):
    print("Se llama la función")
    if request.method == "POST":
        print("El metodo es post")
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            print("Gol de huachipato")
            form.save()
            return redirect('principal')
    else:
        form = NoticiaForm()
    context = {"form": form}
    return render(request, "FormNoticia.html", context)

def noticiaDel(request, id_noticia):
    noticia = get_object_or_404(Noticia, pk = id_noticia)
    if request.method == "POST":
        noticia.delete()
        return redirect('principal')
    return render(request, 'noticiascaosnew.html')



