from reportlab.lib.pagesizes import A4                                      # Importa el formato de página A4 ( 595.2755905511812, 841.8897637795277 ) puntos
from reportlab.pdfgen import canvas                                         # Importa el módulo de canvas para generar archivos en .PDF

import itertools
from random import randint
from statistics import mean

def grouper( iterable, n ):

    args = [ iter( iterable ) ] * n
    return itertools.zip_longest( *args )

def Exportar_a_PDF(Datos):

    ObjetoCanvas = canvas.Canvas("Tabla_Alumnos.pdf", pagesize = A4)            # Crea el archivo "InformeGMP.pdf" en formato .PDF con las dimensiones de una hoja A4
    Ancho_Pagina, Alto_Pagina = A4                                              # Almacena las dimensiones en variables: A4 ( 595.2755905511812, 841.8897637795277 ) puntos

    Espacio_entre_filas = 15                                                    # Espacio entre filas
    Maximo_Filas_Por_Pagina = 45                                                # Establece el número máximo de filas por página
    x_offset = 50                                                               # Margen X
    y_offset = 50                                                               # Margen Y
    
    Lista_X = [ x + x_offset for x in [ 0, 200, 250, 300, 350, 400, 480 ] ]
    Lista_Y = [ Alto_Pagina - y_offset - i * Espacio_entre_filas for i in range( Maximo_Filas_Por_Pagina + 1 ) ]
    
    for Filas in grouper( Datos, Maximo_Filas_Por_Pagina ):

        Filas = tuple( filter( bool, Filas ) )
        ObjetoCanvas.grid( Lista_X, Lista_Y[ : len( Filas ) + 1 ] )

        for y, Fila in zip( Lista_Y[ : -1 ], Filas ):
            for x, Celda in zip( Lista_X, Fila ):
                ObjetoCanvas.drawString( x + 2, y - Espacio_entre_filas + 3, str( Celda ) )

        ObjetoCanvas.showPage()
    
    ObjetoCanvas.save()

Datos = [ ( "NOMBRE", "NOTA 1", "NOTA 2", "NOTA 3", "PROM", "ESTADO" ) ]    # Cabecera de la tabla

for i in range( 1, 11 ):
    Notas_examenes = [ randint(0, 10) for x in range(3) ]                   # Un bucle for que asignará 3 notas aleatorias (0-10) a cada examen en una lista [Nota1, Nota2, Nota3]
    Promedio = round( mean( Notas_examenes ), 2 )                           # mean():  Devuelve la media aritmética de la muestra de datos
                                                                            # round(): Redondea un número a una precisión determinada en dígitos decimales.
    Estado = "Aprobado" if Promedio >= 4 else "Suspendido"
    Datos.append( ( f"Alumno {i}", *Notas_examenes, Promedio, Estado ) )

    """
    Dentro de un encabezado de función:

    * recopila todos los argumentos posicionales en una tupla.
    ** recopila todos los argumentos de palabras clave en un diccionario.

    En una llamada de función:

    * descomprime una lista o tupla en argumentos de posición.
    ** descomprime un diccionario en argumentos de palabras clave.

    """

print( Notas_examenes )

Exportar_a_PDF( Datos )