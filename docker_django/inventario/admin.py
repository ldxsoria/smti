from django.contrib import admin
from .models import Proveedor, Banco, TipoMoneda, BancoProveedor, ContactoProveedor, Factura, TipoActivo, CategoriaActivo, Activo, HistorialActivo
# Register your models here.

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(TipoMoneda)
admin.site.register(Banco)
admin.site.register(BancoProveedor)
admin.site.register(ContactoProveedor)
admin.site.register(Factura)
admin.site.register(TipoActivo)
admin.site.register(CategoriaActivo)
admin.site.register(Activo)
admin.site.register(HistorialActivo)
#admin.site.register(HistorialActivo.TipoHistorial)