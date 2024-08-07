from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, Carrito, ProductoAdicional, Suscripcion, Categoria
from django.contrib.auth.models import User
from .models import Noticia
from .forms import CategoriaForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
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

@staff_member_required
def noticiasEdit(request, pk):
    try:
        noticias=Noticia.objects.get(id=pk)
        context={}
        if noticias:
            print("edit encontró la noticia...")
            if request.method == "POST":
                print("edit, es un POST")
                form = NoticiaForm(request.POST, instance=noticias)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'noticia':noticias, 'form':form, 'mensaje':mensaje}
                return render(request, 'noticias_edit.html', context)
            else:
                #no es un POST
                print("edit, NO es un POST")
                form = NoticiaForm(instance=noticias)
                mensaje=""
                context = {'noticia':noticias, 'form':form, 'mensaje':mensaje}
                return render(request, 'noticias_edit.html', context)
    except:
        print("error, id no existe...")
        noticias=Noticia.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'noticia':noticias}
        return render(request, 'noticias_edit.html', context)

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


@staff_member_required
def noticiaDel(request, id_noticia):
    mensajes = []
    errores = []
    noticias = Noticia.objects.all()
    try:
        noticia = Noticia.objects.get(id = id_noticia)
        context = {}
        if noticia:
            noticia.delete()
            mensajes.append("datos eliminados")
            context = {'noticias': noticias, 'mensajes': mensajes, 'errores': errores}
            return render(request, 'noticiascaosnew.html', context)
    except:
            print("asadjkada")
            noticias = Noticia.objects.all()
            mensaje = 'error, id no existe'
            context = {'mensaje':mensaje, 'noticias':noticias}
            return render(request, 'noticiascaosnew.html', context)
    


def carritosAddd(request):
    if request.method != "POST":
        suscripciones = Suscripcion.objects.all()
        productos_adicionales = ProductoAdicional.objects.all()
        context={"suscripciones":suscripciones, "productos_adicionales":productos_adicionales}
        return render(request, 'carrito.html', context)
    
    else:
        nombre_tarjeta=request.POST["nombre"]
        numero_tarjeta=request.POST["numero"]
        fecha_expiracion=request.POST["expiracion"]
        codigo_seguridad =request.POST["codigo"]
        direccion_envio =request.POST["direccion"]
        suscripcion_id=request.POST["subscripcion"]
        periodicos =request.POST["periodicos"]
        informacion =request.POST["informacion"]
        
        
        objSuscripcion=Suscripcion.objects.get(id = suscripcion_id)
        obj=Carrito(  usuario=request.User,
                                    nombre_tarjeta=nombre_tarjeta,
                                    numero_tarjeta=numero_tarjeta,
                                    fecha_expiracion=fecha_expiracion,
                                    codigo_seguridad=codigo_seguridad,
                                    direccion_envio=direccion_envio,
                                    suscripcion=objSuscripcion,
                                    total=Suscripcion.precio,
                                    )
        obj.save()

        if periodicos:
            producto_periodicos = ProductoAdicional.objects.get(nombre='Recibir Periódicos a Domicilio')
            obj.productos_adicionales.add(producto_periodicos)
            obj.total += producto_periodicos.precio
        if informacion:
            producto_informacion = ProductoAdicional.objects.get(nombre='Recibir Información por Correo')
            obj.productos_adicionales.add(producto_informacion)

        obj.save()

        context={'mensaje':"Ok, datos grabados..."}
        return render(request, 'carrito.html', context)
        
@login_required
def carritosAdd(request):
    if request.method == 'POST':
        nombre_tarjeta = request.POST.get('nombre')
        numero_tarjeta = request.POST.get('numero')
        fecha_expiracion = request.POST.get('expiracion')
        codigo_seguridad = request.POST.get('codigo')
        direccion_envio = request.POST.get('direccion')
        suscripcion_id = request.POST.get('subscripcion')
        periodicos = request.POST.get('periodicos')
        informacion = request.POST.get('informacion')
        
        suscripcion = Suscripcion.objects.get(id=suscripcion_id)
        
        carrito = Carrito(
            usuario=request.user,
            nombre_tarjeta=nombre_tarjeta,
            numero_tarjeta=numero_tarjeta,
            fecha_expiracion=fecha_expiracion,
            codigo_seguridad=codigo_seguridad,
            direccion_envio=direccion_envio,
            suscripcion=suscripcion,
            total=suscripcion.precio
        )
        carrito.save()
        
        if periodicos == 'on':
            producto_periodicos = ProductoAdicional.objects.get(nombre='Recibir Periódicos a Domicilio')
            carrito.productos_adicionales.add(producto_periodicos)
            carrito.total = carrito.total + producto_periodicos.precio
        if informacion == 'on':
            producto_informacion = ProductoAdicional.objects.get(nombre='Recibir Información por Correo')
            carrito.productos_adicionales.add(producto_informacion)
        
        carrito.save()
        
    
    suscripciones = Suscripcion.objects.all()
    productos_adicionales = ProductoAdicional.objects.all()
    
    return render(request, 'carrito.html', {'suscripciones': suscripciones, 'productos_adicionales': productos_adicionales})



