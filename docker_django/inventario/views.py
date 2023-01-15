from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

#MY REQUIREMENTS
from .forms import ActivoForm


# Create your views here.
def new_activo(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'new_activo.html', {
                'form': ActivoForm,
            })
        else:
            try:
                form = ActivoForm(request.POST)
                new_activo = form.save(commit=False)
                new_activo.save()
                return redirect('main')
            except ValueError as e:
                return render(request, 'new_activo.html', {
                    'form': ActivoForm,
                    'error': 'Error'
                })