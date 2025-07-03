
from django import forms
from .models import ClienteB2B, ClienteB2C, Producto
from django.shortcuts import render, get_object_or_404, redirect

class RegistroClienteForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ClienteB2C
        fields = ['nombre', 'apellido', 'rut', 'telefono', 'correo', 'contrasena']


class LoginClienteForm(forms.Form):
    correo = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput)

class ClienteB2CForm(forms.ModelForm):
    class Meta:
        model = ClienteB2C
        fields = ['nombre', 'apellido', 'rut', 'telefono', 'correo', 'contrasena']

class ClienteB2BForm(forms.ModelForm):
    class Meta:
        model = ClienteB2B
        fields = ['nombre_empresa', 'rut_empresa', 'direccion', 'telefono', 'correo_empresa', 'contrasena']
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 'marca', 'categoria', 'precio',
            'stock', 'peso', 'alto', 'ancho', 'largo'  
        ]