from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404

#MODELOS
from .models import Area, Incidencia, Laboratorio

#PROJECTS ROUTES
from django.contrib.auth import login, logout, authenticate #para crear cookie de inicio de sesion
from django.contrib.auth.decorators import login_required #MAIN

@login_required      
def registrar_incidencia(request):
    if request.method == 'GET':
        areas = Area.objects.all()
        incidencias = Incidencia.objects.all()
        laboratorios = Laboratorio.objects.all()
        context = {
            'areas' : areas,
            'incidencias': incidencias,
            'laboratorios': laboratorios,
        }

        return render (request, 'laboratorio/registrar_incidencia.html', context)

    else:
        new_incidencia = Incidencia (
             actividad = request.POST['actividad'],
             comentario = request.POST['comentario'],
             laboratorio = Laboratorio.objects.get(id=request.POST['laboratorio']),
            created_by = request.user,
        )
        new_incidencia.save()

        context = {
                'type' : 'success',
                'alert' : '¡La incidencia fue registrado con exito!'
            }
        return render(request, 'main.html',context)

