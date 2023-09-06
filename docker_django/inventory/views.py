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

#LISTVIEW REQUIREMENTS
from django.views.generic import ListView
from django.core.paginator import Paginator #PAGINATION

#SEARCH REQUIEREMENTS
from django.db.models import Q

from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.conf import settings
from django.template.loader import get_template

# Create your views here.

@login_required
def new_factura(request):
    return render(request, 'inventario/new_factura.html')


def campo_en_blanco(post):
    if (post == ""):
        return "null"
    else:
        return post

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
                    'msg' : '¡Es obligario ingresar un codigo, seleccionar un tipo y modelo!'                    
                }
                return render(request, 'inventario/new_activo.html', context)
            
            else:
                codPost = request.POST.get('cod', None)
                s_nPost = request.POST.get('sn', None)
                
                if 'modelo' in request.POST:
                    modeloPost = Modelo.objects.get(id=request.POST['modelo'])
                else:
                    modeloPost = None

                if 'responsable' in request.POST:
                    responsablePost = User.objects.get(id=request.POST['responsable'])
                else:
                    responsablePost = None

                if 'old_cod' in request.POST:
                    old_codPost = request.POST['old_cod']
                else:
                    old_codPost = None

                add_activo = Activo(
                    cod = codPost,
                    s_n = s_nPost,
                    tipo = Tipo.objects.get(id=request.POST['tipo']),
                    modelo = modeloPost,
                    codigo_antiguo = old_codPost,
                    area = Area.objects.get(cod_area=request.POST['area']),
                    responsable = responsablePost,
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
def my_activos(request):
    activos_asignados = Activo.objects.filter(responsable=request.user)

    context = {
        'activos' : activos_asignados
    }

    print(activos_asignados)
    return render(request, 'inventario/my_activos.html', context)


@login_required
def user_activos(request, usuario):
    try:
        u = get_object_or_404(User, username=usuario)
        activos_asignados2 = Activo.objects.filter(responsable=u)
        context = {
            'activos': activos_asignados2
        }
        print(type(u))
        print(u)
        print(u.id)
        print(activos_asignados2)
        return render(request, 'inventario/my_activos.html', context)
    except User.DoesNotExist:
        # Manejar el caso en el que el usuario no existe
        pass

class SearchActivos(ListView):
    paginate_by = 10
    model = Activo
    template_name = 'inventario/search_activos_by_codigo.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        if query is None:
            return Activo.objects.all()
        else:
            print(query)
            object_list = Activo.objects.filter(
                #Q(razon__startswith=query) | Q(razon__icontains=query)
                #Q(id__icontains=query) | Q(asunto__icontains=query)
                Q(cod__icontains=query) | Q(codigo_antiguo__icontains=query)
            )
            print(object_list)
            return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Activos registrados'
        #context['lugar'] = Area.objects.all().prefetch_related('ticket')
        #context['lugar'] = Area.objects.all()
        return context

def add_view_activo(request, cod=None):
    if cod:
        activo = get_object_or_404(Activo, cod=cod)
    else:
        activo = None

    if request.method == 'POST':
        try:
            # VERIFICAR CAMPOS OBLIGATORIOS
            if 'cod' not in request.POST or 'tipo' not in request.POST:
                areas = Area.objects.all()
                responsables = User.objects.all()
                modelos = Modelo.objects.all()
                tipos = Tipo.objects.all()

                context = {
                    'areas': areas,
                    'responsables': responsables,
                    'modelos': modelos,
                    'tipos': tipos,
                    'type': 'danger',
                    'msg': '¡Es obligatorio ingresar un código, seleccionar un tipo y modelo!'
                }
                return render(request, 'inventario/new_activo.html', context)

            else:
                codPost = request.POST.get('cod', None)
                s_nPost = request.POST.get('sn', None)

                if 'modelo' in request.POST:
                    modeloPost = Modelo.objects.get(id=request.POST['modelo'])
                else:
                    modeloPost = None

                if 'responsable' in request.POST:
                    responsablePost = User.objects.get(id=request.POST['responsable'])
                else:
                    responsablePost = None

                if 'old_cod' in request.POST:
                    old_codPost = request.POST['old_cod']
                else:
                    old_codPost = None

                add_activo = Activo(
                    cod=codPost,
                    s_n=s_nPost,
                    tipo=Tipo.objects.get(id=request.POST['tipo']),
                    modelo=modeloPost,
                    codigo_antiguo=old_codPost,
                    area=Area.objects.get(cod_area=request.POST['area']),
                    responsable=responsablePost,
                    comentario=request.POST['comentario'],
                    created_by=request.user,
                )

                add_activo.save()

                context = {
                    'type': 'success',
                    'alert': '¡El activo fue registrado con exito!'
                }
                return render(request, 'main.html', context)

        except ValueError as e:
            context = {
                'type': 'danger',
                'alert': f'Error: {e}'
            }
            return render(request, 'main.html', context)
    else:
        areas = Area.objects.all()
        responsables = User.objects.all()
        modelos = Modelo.objects.all()
        tipos = Tipo.objects.all()

        context = {
            'areas': areas,
            'responsables': responsables,
            'modelos': modelos,
            'tipos': tipos,
            'activo': activo,
        }
        return render(request, 'inventario/new_activo.html', context)

    
    

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