from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

#MODELOS
from myapp.models import Area
from .models import Modelo, Tipo, Activo

#PROJECTS ROUTES
from django.contrib.auth.decorators import login_required #MAIN

#MY FORMS
from .forms import ProveedorForm


from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.conf import settings
from django.template.loader import get_template

# Create your views here.

@login_required
def new_factura(request):
    return render(request, 'inventario/new_factura.html')

@login_required
def new_activo(request):
    if request.method == 'GET':
        areas = Area.objects.all()
        responsables = User.objects.all()
        modelos = Modelo.objects.all()
        tipos = Tipo.objects.all()

        context = {
            'areas': areas,
            'responsables': responsables,
            'modelos': modelos,
            'tipos': tipos,
        }
        return render(request, 'inventario/new_activo.html', context)
    else:
        try:
            #VERIFICO CAMPOS OBLIGATORIOS
            if('cod' not in request.POST) or ('tipo' not in request.POST):
                areas = Area.objects.all()
                responsables = User.objects.all()
                modelos = Modelo.objects.all()
                tipos = Tipo.objects.all()

                context = {
                    'areas': areas,
                    'responsables': responsables,
                    'modelos': modelos,
                    'tipos': tipos,
                    'type' : 'danger',
                    'msg' : '¡Es obligario ingresar un codigo y seleccionar un tipo!'                    
                }
                return render(request, 'inventario/new_activo.html', context)
            
            else:
                add_activo = Activo(
                    cod = request.POST['cod'],
                    s_n = request.POST['sn'],
                    tipo = Tipo.objects.get(id=request.POST['tipo']),
                    modelo = Modelo.objects.get(id=request.POST['modelo']),
                    codigo_antiguo = request.POST['old_cod'],
                    area = Area.objects.get(cod_area=request.POST['area']),
                    responsable = User.objects.get(id=request.POST['responsable']),
                    comentario = request.POST['comentario'],
                    created_by = request.user,
                )

                add_activo.save()

                context = {
                        'type' : 'success',
                        'alert' : '¡El activo fue registrado con exito!'
                    }
                return render(request, 'main.html',context)
            
        except ValueError as e:
                context = {
                        'type' : 'danger',
                        'alert' : f'Error: {e}'
                    }
                return render(request, 'main.html',context)      
    

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