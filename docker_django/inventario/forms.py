from django import forms
from .models import Activo
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
        fields = ['cod','serial', 'marca', 'modelo', 'desc', 'tipo_activo', 'area_asignada']
