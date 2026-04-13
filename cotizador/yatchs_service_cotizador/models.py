from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    

class Empresa(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    dueño = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.nombre

    
class Agente(models.Model):
    nombre= models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=13)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=13)
    correo = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre
    


class Cotizacion(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, )
    fecha = models.DateField(auto_now_add=True, )
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, )
    iva = models.DecimalField(max_digits=10, decimal_places=2, )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cotizacion = models.IntegerField()
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)


class DetalleCotizacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)


