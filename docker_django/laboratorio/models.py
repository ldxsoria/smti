from django.db import models
from django.contrib.auth.models import User #NECESARIO
from myapp.models import Area

# Create your models here.

class Laboratorio(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    desc = models.CharField(max_length=35)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

class Incidencia(models.Model):
    class Actividad(models.TextChoices):
        clase = "clase" , "clase"
        taller = "taller", "taller"
        capacitacion = "capacitacion", "capacitacion"
        otro = "otro", "otro"

    actividad = models.CharField(
        max_length=12,
        choices=Actividad.choices,
        default=Actividad.clase
    )        

    fecha_reporte = models.DateField(auto_now_add=True)
    hora_reporte = models.TimeField(auto_now_add=True)
    # seccion null
    comentario = models.TextField(max_length=120,blank=True)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

