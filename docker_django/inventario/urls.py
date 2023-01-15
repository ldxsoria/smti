from django.urls import path
from . import views
from .views import InventarioListView

urlpatterns = [
    #path("inventario/add", new_activo.as_view(), name="new_activo")
    path("inventario/add", views.new_activo, name="new_activo"),
    #path('inventario/all', views.inventario, name='inventario'),
    path('inventario/all', InventarioListView.as_view(), name='inventario')
]
