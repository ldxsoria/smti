from django import forms
from .models import Ticket, Registro, Reporte

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['asunto', 'descripcion',]
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '¿Que paso?'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control','placeholder' : '¿Nos das más detalles?','style':'height: 100px'}),
            #'lugar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '¿En donce se presento el incidente?'}),
        }

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['estado','comment_estado','comment_visible']

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['contexto', 'diagnostico', 'recomendacion',]

        widgets = {
            'contexto': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe la situación...','style':'height: 100px'}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '¿Que paso?','style':'height: 100px'}),
            'recomendacion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '¿Que se deberia de hacer?','style':'height: 100px'})
        }