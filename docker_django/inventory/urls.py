from django.urls import path
from . import views

urlpatterns = [
    path('inventario/add/factura', views.new_factura, name='new_factura'),
    path('inventario/add/proveedor', views.new_proveedor, name='new_proveedor'),
    path('inventario/add/activo', views.new_activo, name='new_activo'),
    path('inventario/scanner/qr', views.scanner_qr, name='scanner_qr'),
    path('inventario/export', views.pdf_generation, name="export-pdf" )
]