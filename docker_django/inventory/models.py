from django.db import models
from django.utils import timezone
from myapp.models import Area, User

# PROVEEDOR
class Proveedor(models.Model):
    ruc = models.BigIntegerField(primary_key=True, max_length=11)
    razon_social = models.CharField(max_length=70, blank=True, null=True)
    apodo = models.CharField(max_length=70, blank=True, null=True)
    correo = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.BigIntegerField(max_length=9, blank=True, null=True)

    def __str__(self):
        return self.razon_social


#FACTURA
class Item(models.Model):
    desc = models.CharField(max_length=60)
    comentario = models.CharField(max_length=60)
    num_unidad = models.SmallIntegerField(max_length=9)
    total_unidades = models.SmallIntegerField(max_length=9)
    meses_garantia = models.SmallIntegerField(max_length=3)
    precio_unitario = models.FloatField()
    precio_total = models.FloatField()
    ##JOIN

    def save(self, *args, **kwargs):
        self.precio_total = self.precio_unitario * self.total_unidades
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} {self.num_unidad}/{self.total_unidades}'    

class Factura(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    serie = models.CharField(max_length=35)
    correlativo = models.CharField(max_length=35, null=True)
    fecha_factura = models.DateField(auto_now=False, auto_now_add=False)
    importe_total = models.FloatField()
    ### JOIN
    # UNA FACTURA TIENE MUCHOS ITEMS
    item = models.ManyToManyField(Item, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        return f'{self.serie}-{self.correlativo}'

#ACTIVO - PUEDE SER INDEPENDIENTE DE UNA FACTURA
class Categoria(models.Model):
    desc = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return f'{self.desc}'    


class Tipo(models.Model):
    desc = models.CharField(max_length=60, unique=True)
    ##JOIN
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.desc}'    


class Marca(models.Model):
    desc = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return f'{self.desc}'    

class Modelo(models.Model):
    desc = models.CharField(max_length=60)
    ##JOIN
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)    

    def __str__(self):
        return f'{self.marca} - {self.desc}'


class Activo(models.Model):
    cod = models.CharField(max_length=8, primary_key=True)
    s_n = models.CharField(max_length=70, blank=True, null=True)
    ##JOIN
    tipo = models.ForeignKey(Tipo, null=True, on_delete=models.SET_NULL)
    modelo = models.ForeignKey(Modelo,blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    codigo_antiguo = models.CharField(max_length=15, blank=True, null=True)
    area = models.ForeignKey(Area, blank=True, null=True, on_delete=models.SET_NULL)
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="responsable_activos")
    estado = models.SmallIntegerField(max_length=1, blank=True, null=True, default=1)
    comentario = models.TextField(max_length=200, null=True, blank=True)
    created_at = models.TimeField(auto_now_add=True, null=True)
    created_day = models.DateField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="creador_activos")
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         current_year = timezone.now().year
    #         # total_activos = Activo.objects.count()
    #         # new_code = ((current_year - 2000) * 1000000) + total_activos + 1
    #         total_activos_year = Activo.objects.filter(codigo__startswith=str(current_year - 2000)).count()
    #         new_code = ((current_year - 2000) * 1000000) + total_activos_year + 1
            
    #         self.codigo = str(new_code).zfill(8)

    #         existe = Activo.objects.filter(codigo=self.codigo).exists()

    #         if existe == False:
    #             super(Activo, self).save(*args, **kwargs)
    #         else:
    #             new_code += 1
    #             self.codigo = str(new_code).zfill(8)
    #             super(Activo, self).save(*args, **kwargs)

    """
    # METODO QUE BUSCA QUE CODIGO FALTA Y LO ASIGNA
    def save(self, *args, **kwargs):
        if not self.pk:
            current_year = timezone.now().year

            # Filtrar los activos del año actual para encontrar el primer código disponible
            # Esto evita posibles ciclos infinitos si todos los códigos están ocupados
            first_available_code = 1
            while True:
                new_code = ((current_year - 2000) * 1000000) + first_available_code
                self.codigo = str(new_code).zfill(8)

                existe = Activo.objects.filter(codigo=self.codigo).exists()
                if not existe:
                    break

                first_available_code += 1

        super(Activo, self).save(*args, **kwargs)
    """
    def __str__(self):
        return f'{self.cod} - {self.tipo}'


    
