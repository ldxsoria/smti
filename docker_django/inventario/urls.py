from django.urls import path
from . import views

urlpatterns = [
    #path("inventario/add", new_activo.as_view(), name="new_activo")
    path("inventario/add", views.new_activo, name="new_activo")
]
