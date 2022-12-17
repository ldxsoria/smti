from django.contrib import admin
from .models import Zona, Area, Ticket, Registro, EstadosTicket

class TicketAdmin(admin.ModelAdmin):
    #Mostrar los caompos de solo lectura
    readonly_fields = ("fecha_solicitud", )

# Register your models here.
admin.site.register(Zona)
admin.site.register(Area)
admin.site.register(EstadosTicket)
admin.site.register(Ticket)
admin.site.register(Registro)
