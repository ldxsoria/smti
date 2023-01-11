from django.db import models #DJANGO DEFAULT

# Create your models here.


#Proveedor
class Proveedor(models.Model):
    ruc = models.BigIntegerField(primary_key)
    razon = models.TextField(max_length=120, blank=True)
    correo = models.EmailField(max_length=254, **options)
    telefono = models.BigIntegerField(max_length=9)

"""
#tipo_moneda
class Tipo_moneda(models.Model):
    cod_moneda = models.TextField(max_length=5, primary_key)
    pais = models.TextField(max_length=40)
    simbolo_monetario = models.TextField(max_length=3)

#banco
class Banco(models.Model):
    nombre = models.TextField(max_length=60)

#Cuentas bancarias
class Banco_Proveedor
    ruc = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cod_banco = models.OneToOneField(Banco, on_delete=models.CASCADE)
    moneda = models.OneToOneField(Tipo_moneda, on_delete=models.CASCADE)
    nombre_cuenta = models.TextField(max_length=120, blank=True)
    cuenta  = models.BigIntegerField(max_length=30)
    cci =  models.BigIntegerField(max_length=35)

#Proveedor contacto
ruc
nombre_contacto
apellido_contacto
telefono

#Factura
ruc
num_factura
fecha_factura
tipo_factura
importe_total

#Detalle factura
ruc
num_factura
num_item
descripcion
cod_activo
num_serie
importe

#Tipo activo

#Activo

#Tipo historial

#Historial activo
"""