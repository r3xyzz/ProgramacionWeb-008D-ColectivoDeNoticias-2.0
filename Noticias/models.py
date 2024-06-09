from django.db import models

# Create your models here.

class Usuario(models.Model):
    nom_usu     = models.CharField(max_length=20, blank=False, null=False)
    contrasenna_usu = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nom_usu)

class Categoria(models.Model):
    nom_categoria  = models.CharField(max_length=20) 
    
    def __str__(self):
        return str(self.nom_categoria)
    
class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=100)
    subtitulo_noticia = models.CharField(max_length=50)
    imagen_noticia = models.ImageField(upload_to='noticiasMedia/')
    descImg_noticia = models.CharField(max_length=50)
    cuerpo_noticia = models.TextField()
    nom_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo_noticia)
    
class Suscripcion(models.Model):
    TIPO_SUSCRIPCION = (
        ('mensual', 'Subscripción Mensual'),
        ('anual', 'Subscripción Anual'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_SUSCRIPCION)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.get_tipo_display()
    

class ProductoAdicional(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_tarjeta = models.CharField(max_length=255)
    numero_tarjeta = models.CharField(max_length=16)
    fecha_expiracion = models.DateField()
    codigo_seguridad = models.CharField(max_length=3)
    direccion_envio = models.TextField()
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
    productos_adicionales = models.ManyToManyField(ProductoAdicional, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Carrito de {self.usuario.nom_usu}"
