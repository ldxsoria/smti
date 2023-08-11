from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

#PROJECTS ROUTES
from django.contrib.auth.decorators import login_required #MAIN

#MY FORMS
from .forms import ProveedorForm


from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.conf import settings
from django.template.loader import get_template

# Create your views here.

def new_factura(request):
    return render(request, 'inventario/new_factura.html')
    

@login_required
def new_proveedor(request):
    if request.user.is_staff:
        if request.method == 'GET':
            return render(request, 'inventario/new_proveedor.html', {
                'form': ProveedorForm,
            })
        else:
            try:
                form = ProveedorForm(request.POST)
                new_proveedor = form.save(commit=False)
                new_proveedor.save()
                context = {
                    'type' : 'success',
                    'alert' : '¡El proveedor fue registrado con exito!'
                }

                #return redirect('main')
                return render(request, 'main.html',context)
            except ValueError as e:
                return render(request, 'inventario/new_proveedor.html', {
                    'form': ProveedorForm,
                    'error': 'Error'
                })
            
def scanner_qr(request):
    return render(request, 'inventario/scanner_qr.html')


def pdf_generation(request):
    html_template = get_template('inventario/example.html')
    context = {}  # Puedes proporcionar un contexto si la plantilla lo requiere
    html_content = html_template.render(context)  # Renderizar la plantilla con el contexto
    pdf_file = HTML(string=html_content).write_pdf()
    
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="example.pdf"'
    return response