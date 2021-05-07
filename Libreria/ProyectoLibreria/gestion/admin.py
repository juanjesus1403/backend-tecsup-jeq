from django.contrib import admin
from .models import CategoriaModel, ProductoModel
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
  #para modificar la vista del modelo
  list_display = ['productoId','productoNombre','productoDescripcion']

  #para agregar un buscador
  search_fields = ['productoNombre','categoria__categoriaNombre']


#sirve para registrar u nuevo modelo en el panel administrativo
admin.site.register(CategoriaModel)
admin.site.register(ProductoModel, ProductoAdmin)