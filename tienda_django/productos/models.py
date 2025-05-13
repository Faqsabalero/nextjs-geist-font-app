from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    """
    Modelo de usuario personalizado con roles:
    - admin
    - distribuidor
    - revendedor
    """
    ROLES = (
        ('admin', 'Administrador'),
        ('distribuidor', 'Distribuidor'),
        ('revendedor', 'Revendedor'),
    )
    rol = models.CharField(max_length=20, choices=ROLES, default='revendedor')

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"

class Producto(models.Model):
    """
    Modelo para productos en la tienda
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

    @property
    def imagen_url(self):
        """
        Retorna la URL de la imagen o una imagen por defecto
        """
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        return '/static/productos/default.png'

class StockAssignment(models.Model):
    """
    Modelo para asignar stock de un usuario a otro
    """
    de_usuario = models.ForeignKey(Usuario, related_name='stock_asignado', on_delete=models.CASCADE)
    a_usuario = models.ForeignKey(Usuario, related_name='stock_recibido', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre} de {self.de_usuario} a {self.a_usuario}"

class Venta(models.Model):
    """
    Modelo para registrar ventas
    """
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    distribuidor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'distribuidor'}, null=True, blank=True)
    cantidad = models.PositiveIntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    ganancia = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['distribuidor__username', '-fecha']

    def __str__(self):
        return f"Venta de {self.cantidad} {self.producto.nombre} por {self.distribuidor.username} el {self.fecha.strftime('%Y-%m-%d')}"
