from django.contrib import admin
from .models import Proveedor, Item, Factura, Categoria, Tipo, Marca, Modelo, Activo

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Item)
admin.site.register(Factura)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Activo)