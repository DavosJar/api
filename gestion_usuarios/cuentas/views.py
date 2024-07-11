from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Aplicacion, Usuarios
from .serializers import AplicacionSerializer, UsuariosSerializer
from rest_framework import viewsets

@api_view(['POST'])
def registro_usuario_api(request):
    if request.method == 'POST':
        api_key = request.headers.get('Authorization').split(' ')[-1]  # Obtener API Key del header

        try:
            aplicacion = Aplicacion.objects.get(api_key=api_key)
        except Aplicacion.DoesNotExist:
            return Response({'error': 'Invalid API Key'}, status=status.HTTP_401_UNAUTHORIZED)

        usuario_data = {
            'aplicacion': aplicacion.id,
            'nombre': request.data.get('nombre'),
            'email': request.data.get('email'),
            'password': request.data.get('password')
        }

        serializer = UsuariosSerializer(data=usuario_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Usuario registrado correctamente.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'error': 'Solicitud no válida.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def lista_aplicaciones(request):
    aplicaciones = Aplicacion.objects.all()
    serializer = AplicacionSerializer(aplicaciones, many=True)
    return Response(serializer.data)

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class AplicacionViewSet(viewsets.ModelViewSet):
    queryset = Aplicacion.objects.all()
    serializer_class = AplicacionSerializer
