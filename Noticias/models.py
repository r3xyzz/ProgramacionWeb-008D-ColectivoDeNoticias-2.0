from django.db import models

# Create your models here.
class Usuario(models.Model):
    nom_usu     = models.CharField(max_length=20, blank=False, null=False)
    contrasenna_usu = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.usuario)

class Categoria(models.Model):
    nom_categoria  = models.CharField(max_length=20) 
    
    def __str__(self):
        return str(self.categoria)
    
class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=100)
    subtitulo_noticia = models.CharField(max_length=50)
    descImg_noticia = models.CharField(max_length=50)
    cuerpo_noticia = models.TextField()
    nom_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.noticia)