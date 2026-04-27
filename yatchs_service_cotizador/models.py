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
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)

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
    fecha_caducidad = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, )
    iva = models.DecimalField(max_digits=10, decimal_places=2, )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cotizacion  = models.CharField(max_length=20, unique=True, blank=True)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to="cotizaciones_pdfs/", null=True, blank=True)
    fecha_creacion = models.DateField()

    #sobreescribo el metodo save
    def save(self, *args, **kwargs):
        #genera el numero si el campo esta vacio
        if not self.numero_cotizacion:
            #busca la ultima cotizacion
            ultimo = Cotizacion.objects.order_by("-id").first()
            #si no hya cotizacion empeiza en 1 si si hay toma el ultimo id y le sumas 1
            siguiente = 1 if not ultimo else ultimo.id + 1
            #05d significa llenar ceras hast 5 digitos
            self.numero_cotizacion = f"COT-{siguiente:05d}"
        #llamo al metodo original para guardar todo
        super().save(*args, **kwargs)



class DetalleCotizacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)


