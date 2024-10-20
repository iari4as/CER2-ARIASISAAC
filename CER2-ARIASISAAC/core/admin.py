from django.contrib import admin
from .models import Pedido, Producto
# Register your models here.

admin.site.register(Producto)
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'precio_parcial', 'estado', 'correo')  # Campos a mostrar
    list_filter = ('estado',)  # Filtro por estado
