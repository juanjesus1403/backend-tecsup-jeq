from django.db import models

# Create your models here.
class CategoriaModel(models.Model):
  categoriaId = models.AutoField(
      primary_key=True, #sirve para indicar que ser PK
      unique=True, #no se repetira en otro registro
      null=False, #no podra aceptar valores nulos
      db_column='id' #nombre en la base de datos
  )
  categoriaNombre = models.CharField(
      max_length=45, #longitud maxima del varchar
      null=False,
      db_column='nombre',
      verbose_name='nombre', #mostrar en el panel administrativo
      help_text='Nombre de la categoria' #ayuda para que sea visible en el panel administrativo

  )
  def __str__(self):
      #metodo magico que permite la sobre escritura de la representacion del objeto tanto en consola como en el panel administrativo
      #todo metodo magico tiene __nombre__ esa nomenclatura
      # * siempre se retorna un STRING!!!
      return self.categoriaNombre

  class Meta:
      db_table = 'categorias'#para cambiar el nombre de la tabla en la bd
      verbose_name = 'categoria' #visualizar el modelo en el panel admin
      verbose_name_plural = 'categorias' #visualizar el modelo en plural en el Panel Admin.
      

class ProductoModel(models.Model):
    productoId = models.AutoField(
      primary_key=True,
      unique=True,
      null=False,
      db_column='id',
    )
    productoNombre = models.CharField(
      db_column='nombre',
      help_text='Nombre del producto',
      max_length=45  
    )
    productoPrecio = models.DecimalField(
      max_digits=4,
      decimal_places=2,
      db_column='precio',
      verbose_name='precio del producto',
      help_text='precio del producto',
    )
    productoDescripcion = models.TextField(
      db_column='descipcion',
        
    )
    productoCantidad = models.IntegerField(
        db_column='cantidad',
        null=False,
    )
    #Para hacer las relaciones:
    #opciones para eliminar a un padre:
    #CASCADE => permite eliminar al padre y consecuentemente eliminar a los hijos
    #PROTECT => no permite eliminar al padre siempre y cuando tenga hijos pendientes(primero se elimina a los hijos y luego al padre)
    #SET_NULL => permite eliminar al padre y luego a sus hijos su col. FK la setea en NULL(se queda huerfano)
    #DO_NOTHING => no hace nada, permite eliminar al padre y de la FK con su valor anterior aunque este ya no exista (genera una mala integridad de los datos)
    #RESTRICT => no permite la eliminacion y lanzara un error de tipo RestrictedErros, muy similar al PROTECT

    categoria = models.ForeignKey(
        to=CategoriaModel,
        db_column='categorias_id',
        on_delete=models.CASCADE,#que sucede cuando el padre desea ser eliminado
        related_name='categoriaProductos',#sirve para accecer a las relaciones inversas (para sabaer todos los productos de una categoria), crea un atribito en el padre
        verbose_name='categoria',
        help_text='categoria del producto',
    )

    class Meta:
       db_table = 'productos'
       verbose_name = 'producto' 

class CabeceraModel(models.Model):
    #*la cabId tiene que se PK, no acepta valores nulos, es autoincrementable,
    #*la cabFecha no acepta valores nulos
    #*la cabTipo no acepta valores nulos, su verbose_name es 'tipo de la cabecera', agregar opciones para que solamente pueda ser O VENTA O COMPRA (utilice el paramentro CHOICES)
    # ! adiconal agrega el nombre de la tabla (cabecera) y su verbose name (cabecera)
    TIPO_VENTA = [
        ('VEN', 'VENTA'),
        ('COM', 'COMPRA')
    ]
    cabeceraId = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_column='id'
    )
    cabeceraFecha = models.DateTimeField(
        null=False,
        db_column='fecha'
    )
    cabeceraTipo = models.CharField(
        max_length=45,
        db_column='tipo',
        null=False,
        verbose_name='tipo de la cabecera',
        choices=TIPO_VENTA,
    )

    class Meta:
        db_table = 'cabecera'
        verbose_name = 'cabecera'

class DetalleModel(models.Model):
    # ! ninguna puede admitir valores nulos
    detalleId = models.AutoField(
        primary_key=True,
        null=False,
        db_column='id'
    )
    detalleCantidad = models.IntegerField(
        null=False,
        db_column='cantidad',
        help_text='cantidad de producto a comprar'
    )
    detallePrecio = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        db_column='precio',
        verbose_name='precio',
        help_text='precio del producto'
    )
    producto = models.ForeignKey(
        to=ProductoModel,
        on_delete=models.CASCADE,
        related_name='productoDetalles',
        db_column='producto_id'
    )        

    cabecera = models.ForeignKey(
        to=CabeceraModel,
        on_delete=models.CASCADE,
        related_name='cabeceraDetalles',
        db_column='cabecera_id',
        verbose_name='cabecera'

    )

    class Meta:
        db_table = 'detalle'
        verbose_name = 'detalle'


        

