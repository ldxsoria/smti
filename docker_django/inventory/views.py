from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

#PROJECTS ROUTES
from django.contrib.auth.decorators import login_required #MAIN

#MY FORMS
from .forms import ProveedorForm

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