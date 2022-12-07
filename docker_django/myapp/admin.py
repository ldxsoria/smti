from django.contrib import admin
from .models import Zona, Area, Ticket, Registro, EstadosTicket

# Register your models here.
admin.site.register(Zona)
admin.site.register(Area)
admin.site.register(EstadosTicket)
admin.site.register(Ticket)
admin.site.register(Registro)
