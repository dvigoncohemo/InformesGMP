from reportlab.pdfbase.ttfonts import TTFont        # Importa el módulo TTFont para utilizar fuentes de texto persnalizadas
from reportlab.pdfbase import pdfmetrics            # Importa el módulo para registrar fuentes de texto personalizadas
from reportlab.lib.pagesizes import A4              # Importa el formato de archivo A4
from reportlab.pdfgen import canvas                 # Importa el módulo de canvas
from datetime import datetime                       # Importa el módulo para obtener fechas
import reportlab                                    # Importa la librería de ReportLab

pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))
pdfmetrics.registerFont(TTFont("Calibri-Bold", "Calibrib.ttf"))

ObjetoCanvas = canvas.Canvas( "Portada.pdf", pagesize = A4 )
Ancho_hoja, Alto_hoja = A4

# Crea un rectangulo del tamaño de la hoja
ObjetoCanvas.setFillColorRGB( 51/255, 63/255, 80/255 )                              # Forma de asignar un color RGB
ObjetoCanvas.rect( 0, 0, Ancho_hoja, Alto_hoja, fill = 1 )

# Inserta el logo de Cohemo
ObjetoCanvas.drawImage( "Cohemo.png", Ancho_hoja - 440,                 # Inserta una imagen con la función: drawImage( "Imagen .png .jpg .gif", Posición_X, Posición_Y, Ancho_imagen, Alto_imagen)
                        Alto_hoja - 350, 
                        width = 280,
                        height = 42 
                        )

# Método 1 : Texto sencillo
ObjetoCanvas.setFont( "Calibri-Bold", 28 )                                          # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 1, 1, 1 )                                             # Asigna el color "Negro" al ObjetoCanvas
ObjetoCanvas.drawString( Ancho_hoja - 470,                                          # Escribe el texto "¡Hola, Mundo!" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         Alto_hoja - 430, 
                         "GMP – Generador de informes")       

Fecha = datetime.now().strftime('%d/%m/%Y')

ObjetoCanvas.setFont( "Calibri", 18 )                                               # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.drawString( Ancho_hoja - 170, Alto_hoja - 730, str(Fecha))             # Escribe la fecha con la función: drawString( Posicion_X, Posicion_Y, "Mensaje")  
ObjetoCanvas.showPage( )
ObjetoCanvas.save( )