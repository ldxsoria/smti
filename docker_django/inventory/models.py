from django.db import models

# PROVEEDOR
class Proveedor(models.Model):
    ruc = models.BigIntegerField(primary_key=True, max_length=11)
    razon_social = models.CharField(max_length=70, blank=True, null=True)
    apodo = models.CharField(max_length=70, blank=True, null=True)
    correo = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.BigIntegerField(max_length=9, blank=True, null=True)

    def __str__(self):
        return self.razon
    



#FACTURA
class Activo(models.Model):
    pass

class ItemFactura(models.Model):
    nombre = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)
    comentario = models.CharField(max_length=60)
    unidades = models.SmallIntegerField(max_length=9)
    meses_garantia = models.SmallIntegerField(max_length=3)
    precio_unitario = models.FloatField()
    precio_total = models.FloatField()


class Factura(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    serie = models.CharField(max_length=35)
    fecha_factura = models.DateField(auto_now=False, auto_now_add=False)
    importe_total = models.FloatField()
    ### JOIN
    # UNA FACTURA TIENE MUCHOS ITEMS
    item = models.ManyToManyField(ItemFactura)
    

    def __str__(self) -> str:
        return self.serie
    
