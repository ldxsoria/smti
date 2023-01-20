from django.urls import path
from . import views
from .views import InventarioListView, ProveedorListView, SearchProveedorListView

urlpatterns = [
    #path("inventario/add", new_activo.as_view(), name="new_activo")
    path("inventario/add", views.new_activo, name="new_activo"),
    path("proveedor/add", views.new_proveedor, name="new_proveedor"),
    #path('inventario/all', views.inventario, name='inventario'),
    path('inventario/all', InventarioListView.as_view(), name='inventario'),
    path('proveedores/all', ProveedorListView.as_view(), name='proveedores'),
    #SEARCH
    path('proveedores/search/', SearchProveedorListView.as_view(), name='search_proveedores'),
    #EXPORT URLS
    path('inventario/export', views.export_activos, name='export_activos_csv'),
    #IMPORT URLS
    path('inventario/import', views.import_activos, name='import_activos_csv')
]
