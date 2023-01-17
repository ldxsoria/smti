from django import forms
from .models import Activo, Proveedor, Factura
"""
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['asunto', 'descripcion', 'lugar']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '¿Que paso?'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control','placeholder' : '¿Nos das más detalles?','style':'height: 100px'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '¿En donce se presento el incidente?'}),
        }
"""

class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = ['cod','serial', 'marca', 'modelo', 'desc', 'tipo_activo', 'area_asignada', 'responsable']


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['ruc', 'razon', 'apodo', 'correo', 'telefono'] 
        widgets = {
            'ruc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el RUC registrado en SUNAT'}),
            'razon': forms.TextInput(attrs={'class': 'form-control','placeholder' : '¿Cual es la razon social?','style':'height: 100px'}),
            'apodo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un nombre para identificarlos'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo de la empresa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un numero de contacto'}),
        }