from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView

#MODELOS
from .models import Activo

#MY REQUIREMENTS
from .forms import ActivoForm


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
"""
def inventario(request):
    if request.method == 'GET':
        activos = Activo.objects.all()
        return render(request, 'inventario/inventario.html', {
            'title': 'Activos registrados',
            'activos': activos,
        })
"""
class InventarioListView(ListView):
    model = Activo
    template_name = 'inventario/inventario.html'
    
    #def get_queryset(self):
    #    return Activo.objetcs.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Activos registrados' 
        #print(context)
        return context
