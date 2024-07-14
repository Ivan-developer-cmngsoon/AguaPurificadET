from django.db import models

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=100)  

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente.nombre}'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'

class Recarga(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Recarga {self.id} - {self.cliente.nombre}'
