from django.contrib import admin
from .models import Proveedor, Banco, Tipo_moneda, Banco_Proveedor, Contacto_Proveedor

# Register your models here.

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Tipo_moneda)
admin.site.register(Banco)
admin.site.register(Banco_Proveedor)
admin.site.register(Contacto_Proveedor)