# --------------------------------------------------------------------------#
#               Crea un archivo en formato A4 .pdf                          #
# --------------------------------------------------------------------------#

from reportlab.lib.pagesizes import A4                                      # Importa el formato de página A4 ( 595.2755905511812, 841.8897637795277 ) puntos
from reportlab.pdfgen import canvas                                         # Importa el módulo de canvas para generar archivos en .PDF

ObjetoCanvas = canvas.Canvas("Ejemplo2.pdf", pagesize = A4)                 # Crea el archivo "InformeGMP.pdf" en formato .PDF con las dimensiones de una hoja A4
Ancho_Pagina, Alto_Pagina = A4                                              # Almacena las dimensiones en variables: A4 ( 595.2755905511812, 841.8897637795277 ) puntos

x = 180                                                                     # Define un márgen horizontal arbitrario
y = Alto_Pagina - 50                                                        # Define un márgen vertical arbitrario

# --------------------------------------------------------------------------#
#                      Dibujar figuras geométricas                          #
# --------------------------------------------------------------------------#

# Dibujar una línea
ObjetoCanvas.setFont( "Helvetica-Bold", 10 )                                # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente", Tamaño )
ObjetoCanvas.setFillColorRGB( 0, 0, 255 )                                   # Asigna el color "Azul" al ObjetoCanvas
ObjetoCanvas.drawString( 30, y - 50, "Línea" )                              # Escribe el texto "Línea" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje")
ObjetoCanvas.line( x + 10, y - 50, x + 100, y - 50 )                        # Crea una línea con la función: line( Posicion_X1, Posicion_Y1, Posicion_X2, Posicion_Y2 )
ObjetoCanvas.setStrokeColorRGB( 0, 0, 255 )                                 # Asigna el color del borde del ObjetoCanvas

# Dibujar un rectangulo
ObjetoCanvas.setFont( "Times-Roman", 11 )                                   # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente", Tamaño )
ObjetoCanvas.setFillColorRGB( 0, 255, 0 )                                   # Asigna el color "Verde" al ObjetoCanvas
ObjetoCanvas.drawString( 30, y - 100, "Rectángulo" )                        # Escribe el texto "Rectángulo" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje")
ObjetoCanvas.rect( x + 10, y - 120, 100, 50, fill = True )                  # Crea un rectangulo con la función: rect( Posicion_X, Posicion_Y, Ancho_rectangulo, Alto_rectangulo, ¿Relleno? )
ObjetoCanvas.setStrokeColorRGB( 0, 255, 0 )                                 # Asigna el color del borde del ObjetoCanvas

# Dibujar un rectangulo con los vertices redondeados
ObjetoCanvas.setFont( "Courier", 12 )                                       # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente", Tamaño )
ObjetoCanvas.setFillColorRGB( 0, 255, 255 )                                 # Asigna el color "Cyan" al ObjetoCanvas
ObjetoCanvas.drawString( 30, y - 170, "Rectángulo redondeado" )             # Escribe el texto "Rectángulo redondeado" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje")
ObjetoCanvas.roundRect( x + 10, y - 190, 100, 50, 5, fill = False )         # Crea un rectangulo con los vertices redondeados con la función: roundRect( Posicion_X, Posicion_Y, Ancho_rectangulo, Alto_rectangulo, Radio_vertice, ¿Relleno? )
ObjetoCanvas.setStrokeColorRGB( 0, 255, 255 )                               # Asigna el color del borde del ObjetoCanvas

# Dibujar un círculo
ObjetoCanvas.setFont( "Helvetica-Oblique", 13 )                             # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente", Tamaño )
ObjetoCanvas.setFillColorRGB( 255, 0, 0 )                                   # Asigna el color "Rojo" al ObjetoCanvas
ObjetoCanvas.drawString( 30, y - 240, "Círculo" )                           # Escribe el texto "Círculo" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje")
ObjetoCanvas.circle( x + 40, y - 240, 30, fill = True )                     # Crea un círculo con la función: roundRect( Posicion_X, Posicion_Y, Radio_circulo, ¿Relleno? )
ObjetoCanvas.setStrokeColorRGB( 255, 0, 0 )                                 # Asigna el color del borde del ObjetoCanvas

# Dibujar una elípse
ObjetoCanvas.setFont( "Times-Roman", 14 )                                   # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente", Tamaño )
ObjetoCanvas.setFillColorRGB( 255, 0, 255 )                                 # Asigna el color "Magenta" al ObjetoCanvas
ObjetoCanvas.drawString( 30, y - 310, "Elipse" )                            # Escribe el texto "Elipse" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje")
ObjetoCanvas.ellipse( x + 10, y - 320, 280, y - 290, fill = False )         # Crea una elipse con la función: ellipse( Posicion_X, Posicion_Y, Alto_elipse, Ancho_elipse, ¿Relleno? )
ObjetoCanvas.setStrokeColorRGB( 255, 0, 255 )                               # Asigna el color del borde del ObjetoCanvas

# Pasa a la siguiente hoja
ObjetoCanvas.showPage( )                                                    # Termina de escribir en la hoja actual y pasa a la siguiente

# --------------------------------------------------------------------------#
#                       Escribir texto plano                                #
# --------------------------------------------------------------------------#

# Método 1 : Texto sencillo
ObjetoCanvas.setFont( "Helvetica", 10 )                                     # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 0, 0, 0 )                                     # Asigna el color "Negro" al ObjetoCanvas
ObjetoCanvas.drawString( x - 150, y, "¡Hola, mundo!")                       # Escribe el texto "¡Hola, Mundo!" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje")  

# Método 2: Texto que admite salto de línea
ObjetoTexto = ObjetoCanvas.beginText( x - 150, Alto_Pagina - 80 )           # Indica la posición del Texto en la página
ObjetoTexto.setFont( "Times-Roman", 14 )                                    # De esta manera actúa sólo sobre el Texto y no sobre toda la hoja
ObjetoTexto.textLine( "¡Hola, mundo!" )                                     # Las dos frases aparecen en dos líneas diferentes.
ObjetoTexto.textLine( "¡Desde ReportLab y Python!" )                        # Las dos frases aparecen en dos líneas diferentes.
ObjetoTexto.textLines( "¡Hola, mundo!\n¡Desde ReportLab y Python!" )        # Otra manera más limpia de realizar el mismo párrafo

# Aplica los campos del ObjetoTexto al ObjetoCanvas
ObjetoCanvas.drawText( ObjetoTexto )                                        # Una vez redactado el texto se aplica a la hoja con la función: drawText( "Texto" )

# --------------------------------------------------------------------------#
#                        Importar fuentes de texto                          #
# --------------------------------------------------------------------------#

from reportlab.pdfbase.ttfonts import TTFont                                # Importa el módulo para usar librerías personalizadas
from reportlab.pdfbase import pdfmetrics                                    # Importa el módulo para registrar fuentes de texto

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))                         # Registra la fuente Vera (Regular) con la función: registerFont( "Nombre del estilo", "ArchivoFuente.ttf" )
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))                     # Registra la fuente Vera (Bold) con la función: registerFont( "Nombre del estilo", "ArchivoFuente.ttf" )
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))                     # Registra la fuente Vera (Italic) con la función: registerFont( "Nombre del estilo", "ArchivoFuente.ttf" )
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))                     # Registra la fuente Vera (Bold-Italic) con la función: registerFont( "Nombre del estilo", "ArchivoFuente.ttf" )

ObjetoCanvas.setFont( 'VeraBI', 12 )                                        # Asigna la fuente al IbjetoCanvas con la función: setFont( "Nombre del estilo", Tamaño )
ObjetoCanvas.drawString( x - 150, Alto_Pagina - 200, "Primer parrafo" )

ObjetoCanvas.setFont( 'VeraBI', 14 )                                        # Asigna la fuente al IbjetoCanvas con la función: setFont( "Nombre del estilo", Tamaño )
ObjetoCanvas.drawString( x - 150, Alto_Pagina - 220, "Segundo parrafo" )

# --------------------------------------------------------------------------#
#                           Insertar imágenes                               #
# --------------------------------------------------------------------------#

ObjetoCanvas.drawImage( "NUEVO_LOGO.png", x - 150,                          # Inserta una imagen con la función: drawImage( "Imagen .png .jpg .gif", Posición_X, Posición_Y, Ancho_imagen, Alto_imagen)
                        Alto_Pagina - 300, 
                        width = 180,
                        height = 50 
                        )

# --------------------------------------------------------------------------#
#                           Insertar grillas                                #
# --------------------------------------------------------------------------#

xlist = [ 250,                                                              # Define las posiciones y cantidad de cuadros horizontales      
          300, 
          350, 
          400, 
          450,
          500
        ]

ylist = [ Alto_Pagina - 250,                                                # Define las posiciones y cantidad de cuadros verticales      
          Alto_Pagina - 300, 
          Alto_Pagina - 350, 
          Alto_Pagina - 400 
          ]
          
ObjetoCanvas.grid( xlist, ylist )                               

# --------------------------------------------------------------------------#
#                             Insertar footer                               #
# --------------------------------------------------------------------------#

ObjetoCanvas.save( )                                                        # 