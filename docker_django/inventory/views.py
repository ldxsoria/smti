from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

#PROJECTS ROUTES
from django.contrib.auth.decorators import login_required #MAIN

# Create your views here.

def new_factura(request):
    return render(request, 'inventario/new_factura.html')
    