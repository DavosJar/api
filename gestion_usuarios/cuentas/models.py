from django.db import models
import secrets



class Aplicacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre