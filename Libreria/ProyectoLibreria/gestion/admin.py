from django.contrib import admin
from .models import CategoriaModel, ProductoModel
# Register your models here.
#sirve para registrar u nuevo modelo en el panel administrativo
admin.site.register(CategoriaModel)
admin.site.register(ProductoModel)