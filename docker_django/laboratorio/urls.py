from django.urls import path
from . import views

urlpatterns = [
    #URL LABORATORIO
    path('laboratorio/registrar-incidencia', views.registrar_incidencia, name = 'registrar_incidencia')

    ]    