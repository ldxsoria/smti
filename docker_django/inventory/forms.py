from django import forms
from .models import Activo, Proveedor, Factura

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['ruc', 'razon_social', 'apodo', 'correo', 'telefono'] 
        widgets = {
            'ruc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el RUC registrado en SUNAT'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control','placeholder' : '¿Cual es la razon social?','style':'height: 100px'}),
            'apodo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un nombre para identificarlos'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo de la empresa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un numero de contacto'}),
        }