from django.contrib import admin
from .models import Categoria, Noticia, Suscripcion, ProductoAdicional, Carrito

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Suscripcion)
admin.site.register(ProductoAdicional)
admin.site.register(Carrito)