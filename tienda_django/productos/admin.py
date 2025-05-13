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
    list_display = ('from_user', 'to_user', 'producto', 'cantidad', 'fecha')
    list_filter = ('fecha', 'from_user', 'to_user')
    search_fields = ('producto__nombre',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'costo', 'ganancia', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('producto__nombre',)
