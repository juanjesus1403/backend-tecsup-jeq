from django.urls import path
from .views import CRUDCategoriaController, ListarCategoriaController

#! esta variable se tiene que llamar si o si asi:
urlpatterns = [
  path('categorias',ListarCategoriaController.as_view()),
  path('categorias/<int:pk>', CRUDCategoriaController.as_view())
]