from .models import CategoriaModel
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

class ListarCategoriaController(ListAPIView)
    # el atributo queryset es el encargdo de hacer la consulta a la base de datos para rellenar la respuesta en la vista generica
    #SELECT * FROM CATEGORIAS (setencia SQL) (SETENCIA RAW)
    queryset = CategoriaModel.objects.all()