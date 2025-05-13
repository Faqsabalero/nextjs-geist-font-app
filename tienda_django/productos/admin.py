from django.contrib import admin
from .models import Usuario, Producto, StockAssignment, Venta

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'rol', 'email')
    list_filter = ('rol',)
    search_fields = ('username', 'email')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'imagen')
    list_filter = ('stock',)
    search_fields = ('nombre', 'descripcion')

@admin.register(StockAssignment)
class StockAssignmentAdmin(admin.ModelAdmin):
    list_display = ('de_usuario', 'a_usuario', 'producto', 'cantidad', 'fecha_asignacion')
    list_filter = ('fecha_asignacion', 'de_usuario', 'a_usuario')
    search_fields = ('producto__nombre',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'distribuidor', 'cantidad', 'costo', 'ganancia', 'fecha')
    list_filter = ('fecha', 'distribuidor')
    search_fields = ('producto__nombre', 'distribuidor__username')
    ordering = ('distribuidor__username', '-fecha')
