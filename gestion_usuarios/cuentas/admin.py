from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Aplicacion)
class AplicacionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('creado', 'nombre',)
    ordering = ('nombre','creado',)
    
@admin.register(Usuarios)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'aplicacion')
    search_fields = ('nombre', 'email', 'aplicacion')
    list_filter = ('creado', 'nombre', 'email', 'aplicacion')
    ordering = ('nombre', 'email', 'aplicacion', 'creado')
    
    
