from rest_framework import serializers
from .models import Aplicacion, Usuarios

class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplicacion
        fields = ['id', 'nombre', 'creado']

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['aplicacion', 'nombre', 'email', 'password']