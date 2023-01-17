from django.db import models #DJANGO DEFAULT
from django.contrib.auth.models import User #COLABORADOR
from myapp.models import Area

# Create your models here.


#Proveedor
class Proveedor(models.Model):
    ruc = models.BigIntegerField(primary_key=True)
    razon = models.CharField(max_length=70, blank=True, null=True)
    apodo = models.CharField(max_length=70, blank=True, null=True)
    correo = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.BigIntegerField(max_length=9, blank=True, null=True)

    def __str__(self):
        return self.razon


#tipo_moneda
class TipoMoneda(models.Model):
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
class BancoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cod_banco = models.OneToOneField(Banco, on_delete=models.CASCADE)
    moneda = models.OneToOneField(TipoMoneda, on_delete=models.CASCADE)
    nombre_cuenta = models.CharField(max_length=120, blank=True)
    cuenta  = models.BigIntegerField(max_length=30)
    cci =  models.BigIntegerField(max_length=35)

    def __str__(self):
        return f'{self.proveedor} - {self.cod_banco}'

#Proveedor contacto
class ContactoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre_contacto = models.CharField(max_length=120, blank=True)
    apellido_contacto = models.CharField(max_length=120, blank=True)
    telefono = models.BigIntegerField(max_length=35)

    def __str__(self):
        return f'{self.nombre_contacto} - {self.proveedor.apodo}'
"""
#Tipo historial
class TipoHistorial(models.Model):
    desc = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.id} - {self.desc}'
"""    

#Tipo activo
class TipoActivo(models.Model):
    desc = models.CharField(max_length=60)

    def __str__(self):
        return self.desc
    
#Categoria activo
class CategoriaActivo(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    categoria = models.CharField(max_length=15)
    #UNA CATEGORIA TIENE MUCHOS TIPOS DE ACTIVOS
    tipo = models.ManyToManyField(TipoActivo, blank=True)

    def __str__(self):
        return self.categoria
    

#Activo
class Activo(models.Model):
    cod = models.CharField(max_length=50, primary_key=True)
    serial = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)
    tipo_activo = models.ForeignKey(TipoActivo, on_delete=models.CASCADE)
    area_asignada = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True, null=True)
    responsable =  models.OneToOneField(User, on_delete=models.SET_NULL, related_name='user_as_original', null=True)

    def __str__(self):
        return f'{self.cod} - {self.tipo_activo.desc}'
    

#Factura
class Factura(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    num_factura = models.CharField(max_length=35)
    fecha_factura = models.DateField(auto_now=False, auto_now_add=False)
    #tipo_factura
    moneda = models.OneToOneField(TipoMoneda, on_delete=models.CASCADE) 
    importe_total = models.FloatField()
    #UNA FACTURA TIENE ACTIVOS
    activos = models.ManyToManyField(Activo)

    def __str__(self):
        return self.num_factura
    
#Historial activo
class HistorialActivo(models.Model):
    class TipoHistorial(models.TextChoices):
        STOCK = "1", "STOCK"
        ASIGNACION = "2", "ASIGNACION"
        DEVOLUCION = "3", "DEVOLUCION"
        BAJA = "4", "BAJA"
        DONACION = "5", "DONACION"
        # (...)

    tipo = models.CharField(
        max_length=2,
        choices=TipoHistorial.choices,
        default=TipoHistorial.STOCK
    )

    detalle_motivo = models.TextField(blank=True, null=True)
    activos = models.ManyToManyField(Activo)
    responsable_actual = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='user_as_actual', null=True)
    nuevo_responsable = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='user_as_nuevo', null=True)

    #responsable_actual = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    #nuevo_responsable = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    #id_area
    #autorizacion


#Detalle factura
#ruc
#num_factura
#num_item
#descripcion
#cod_activo
#num_serie
#importe
