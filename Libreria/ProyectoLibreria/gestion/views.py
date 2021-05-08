from django.db.models import query
from rest_framework import serializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import CategoriaModel
from .serializers import MostrarCategoriasSerializer

class ListarCategoriaController(ListCreateAPIView):
    # el atributo queryset es el encargdo de hacer la consulta a la base de datos para rellenar la respuesta en la vista generica
    #SELECT * FROM CATEGORIAS (setencia SQL) (SETENCIA RAW)
    queryset = CategoriaModel.objects.all()
    serializer_class = MostrarCategoriasSerializer

# C => CREATE (Crear)
# R => READ (Leer)
# U => UPDATE (Actualizar)
# D => DELETE (Eliminar)

class CRUDCategoriaController(RetrieveUpdateDestroyAPIView):
    queryset = CategoriaModel.objects.all()
    serializer_class = MostrarCategoriasSerializer
