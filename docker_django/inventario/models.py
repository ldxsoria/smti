from django.db import models #DJANGO DEFAULT

# Create your models here.


#Proveedor
class Proveedor(models.Model):
    ruc = models.BigIntegerField(primary_key=True)
    razon = models.TextField(max_length=120, blank=True, null=True)
    apodo = models.TextField(max_length=120, blank=True, null=True)
    correo = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.BigIntegerField(max_length=9, blank=True, null=True)

    def __str__(self):
        return self.razon


#tipo_moneda
class Tipo_moneda(models.Model):
    cod_moneda = models.CharField(max_length=5, primary_key=True)
    pais = models.CharField(max_length=40)
    simbolo_monetario = models.CharField(max_length=3)

    def __str__(self):
        return self.cod_moneda


#banco
class Banco(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

#Cuentas bancarias
class Banco_Proveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cod_banco = models.OneToOneField(Banco, on_delete=models.CASCADE)
    moneda = models.OneToOneField(Tipo_moneda, on_delete=models.CASCADE)
    nombre_cuenta = models.CharField(max_length=120, blank=True)
    cuenta  = models.BigIntegerField(max_length=30)
    cci =  models.BigIntegerField(max_length=35)

    def __str__(self):
        return f'{self.proveedor} - {self.cod_banco}'

#Proveedor contacto
class Contacto_Proveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre_contacto = models.CharField(max_length=120, blank=True)
    apellido_contacto = models.CharField(max_length=120, blank=True)
    telefono = models.BigIntegerField(max_length=35)

    def __str__(self):
        return f'{self.nombre_contacto} - {self.proveedor.apodo}'
    

#Factura
class Factura(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    num_factura = models.CharField(max_length=35)
    fecha_factura = models.DateField(auto_now=False, auto_now_add=False)
    #tipo_factura
    moneda = models.OneToOneField(Tipo_moneda, on_delete=models.CASCADE) 
    importe_total = models.FloatField()

"""  
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