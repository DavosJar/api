"""
URL configuration for gestion_usuarios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from cuentas.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'aplicaciones', AplicacionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/', include(router.urls)),
    path('api/registrar_usuario/', registro_usuario_api, name='registro_usuario_api'),
    path('api/aplicaciones_api/', lista_aplicaciones, name='aplicaciones'),


]
