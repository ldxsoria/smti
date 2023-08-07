from django.urls import path
from . import views

urlpatterns = [
    path('inventario/add/factura', views.new_factura, name='new_factura')
]