from django import forms
from .models import Aplicacion
from django.forms import ModelForm


class AplicacionForm(ModelForm):
    class Meta:
        model = Aplicacion
        fields = ['nombre']
        widgets = {

            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
           
        }

class LoginForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
