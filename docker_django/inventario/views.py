from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

#MODELOS
from .models import Activo, TipoActivo, Area, Proveedor

#MY REQUIREMENTS
from .forms import ActivoForm, ProveedorForm

#IMPORT CSV REQUIREMENTS
import csv, io
from import_export import resources

#LISTVIEW REQUIREMENTS
from django.views.generic import ListView
from django.core.paginator import Paginator #PAGINATION

#SEARCH REQUIEREMENTS
from django.db.models import Q

# Create your views here.
def new_activo(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'inventario/new_activo.html', {
                'form': ActivoForm,
            })
        else:
            try:
                form = ActivoForm(request.POST)
                new_activo = form.save(commit=False)
                new_activo.save()
                return redirect('main')
            except ValueError as e:
                return render(request, 'inventario/new_activo.html', {
                    'form': ActivoForm,
                    'error': 'Error'
                })

def new_proveedor(request):
    if request.user.is_authenticated:
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

"""
def inventario(request):
    if request.method == 'GET':
        activos = Activo.objects.all()
        return render(request, 'inventario/inventario.html', {
            'title': 'Activos registrados',
            'activos': activos,
        })
"""

#LIST VIEWS##########################################################################################
class InventarioListView(ListView):
    paginate_by = 25
    model = Activo
    template_name = 'inventario/inventario.html'
    
    #def get_queryset(self):
    #    return Activo.objetcs.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Activos registrados' 
        #print(context)
        return context

class ProveedorListView(ListView):
    paginate_by = 25
    model = Proveedor
    template_name = 'inventario/proveedores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Proveedores registrados'
        return context

class SearchProveedorListView(ListView):
    model = Proveedor
    template_name = 'inventario/result_search_proveedores.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        print(query)
        object_list = Proveedor.objects.filter(
            #Q(razon__startswith=query) | Q(razon__icontains=query)
            Q(razon__icontains=query) | Q(ruc__icontains=query)
        )
        print(object_list)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Proveedores registrados'
        return context

#EXPORT VIEWS##########################################################################################

def export_activos(request):
    activos_resource = resources.modelresource_factory(model=Activo)()
    dataset = activos_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'atachment; filename="activos_export.csv"'
    return response

#IMPORT VIEWS##########################################################################################

def import_activos(request):
    template = 'general/import.html'
    context = {}
    if request.method == 'GET':
        return render(request, template, context)
    try:
        csv_file = request.FILES['file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)

        for column in csv.reader(io_string, delimiter=',', quotechar='|'):
            created = Activo.objects.update_or_create(
                cod = column[0],
                serial = column[1],
                marca = column[2],
                modelo = column[3],
                desc = column[4],
                tipo_activo = TipoActivo.objects.get(id=column[5]),
                area_asignada = Area.objects.get(cod_area=column[6]),
                #responsable = column[7],
            )

        context = {
            'type' : 'success',
            'alert' : '¡El CSV fue cargardo con exito!'
        }
        return render(request, template, context)
    except ValueError as e:
        context = {
        'type' : 'danger',
        'alert' : f'Selecciona un .CSV {e}'
        }
        return render(request, template, context)
    else:
        return redirect('main')
