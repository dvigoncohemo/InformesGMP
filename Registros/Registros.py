from reportlab.pdfbase.ttfonts import TTFont                        # Importa el módulo TTFont para utilizar fuentes de texto persnalizadas
from reportlab.pdfbase import pdfmetrics                            # Importa el módulo para registrar fuentes de texto personalizadas
from reportlab.lib.pagesizes import A4                              # Importa el formato de archivo A4
from reportlab.pdfgen import canvas                                 # Importa el módulo de canvas
from datetime import datetime                                       # Importa el módulo para obtener fechas
import reportlab                                                    # Importa la librería de ReportLab

# Obtiene la fecha actual
Fecha = datetime.now().strftime('%d/%m/%Y')

# Registra la fuente Calibri para utilizarla en el documento
pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))           # Calibri
pdfmetrics.registerFont(TTFont("Calibri-Bold", "Calibrib.ttf"))     # Calibri Bold
pdfmetrics.registerFont(TTFont("Calibri-Italic", "CalibriI.ttf"))     # Calibri Bold

# Crea el documento "Registros.pdf"
ObjetoCanvas = canvas.Canvas( "Registros.pdf", pagesize = A4 )

# Obtiene el Ancho y Alto de la página
Ancho_hoja, Alto_hoja = A4                                          # Altura: 841.8897637795277
                                                                    # Anchura: 595.2755905511812

# Asigna el color de background a Blanco
ObjetoCanvas.setFillColorRGB( 1, 1, 1 )                             # Asigna el color de relleno a Blanco
ObjetoCanvas.rect( 0, 0, Ancho_hoja, Alto_hoja, fill = 1 )          # Crea un rectangulo del tamaño de la hoja

# Inserta el logo de Cohemo en la esquina superior izquierda
ObjetoCanvas.drawImage( "Logo.png",                                 # Inserta una imagen con la función: drawImage( "Imagen .png .jpg .gif", Posición_X, Posición_Y, Ancho_imagen, Alto_imagen)
                        Ancho_hoja - 550,
                        Alto_hoja - 60, 
                        width = 180,
                        height = 22 
                        )

# Crea un rectangulo Azul metálico
ObjetoCanvas.setStrokeColorRGB( 51/255, 63/255, 80/255 )            # Asigna el color del borde del ObjetoCanvas
ObjetoCanvas.setFillColorRGB( 51/255, 63/255, 80/255 )              # Asigna el color de relleno
ObjetoCanvas.rect( 45, 
                   730,    
                   Ancho_hoja - 85, 
                   13, 
                   fill = 1 
                 )

# Añade el texto: "REGISTRO DE EDICIÓN"
ObjetoCanvas.setFont( "Calibri-Bold", 12 )                          # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 1, 1, 1 )                             # Asigna el color "Negro" al ObjetoCanvas
ObjetoCanvas.drawString( 244,                                       # Escribe el texto "¡Hola, Mundo!" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         733, 
                         "REGISTRO DE EDICIÓN"
                        )       

# Crea un rectangulo Gris con borde negro
ObjetoCanvas.setFillColorRGB( 166/255, 166/255, 166/255 )           # Color del relleno Gris
ObjetoCanvas.setStrokeColorRGB( 0, 0, 0 )                           # Color del borde Negro
ObjetoCanvas.setLineWidth(0.5)

# Recuadro de REALIZADO POR, REVISADO POR, APROBADO POR
ObjetoCanvas.rect( 65, 
                   700,    
                   160,
                   13,
                   fill = 1 
                 )
ObjetoCanvas.rect( 225, 
                   700,    
                   160,
                   13,
                   fill = 1 
                 )
ObjetoCanvas.rect( 385, 
                   700,    
                   160,
                   13,
                   fill = 1 
                 )

# Añade los títulos a los recuadros
ObjetoCanvas.setFont( "Calibri-Bold", 10 )                          # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 0, 0, 0 )                             # Asigna el color "Negro" al ObjetoCanvas

# Añade el texto: "REALIZADO POR:"
ObjetoCanvas.drawString( 110,                                       # Escribe el texto "¡Hola, Mundo!" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         703, 
                         "REALIZADO POR:"
                        )       

# Añade el texto: "REVISADO POR:"
ObjetoCanvas.drawString( 270,                                       # Escribe el texto "¡Hola, Mundo!" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         703, 
                         "REVISADO POR:"
                        )       

# Añade el texto: "APROBADO POR:"
ObjetoCanvas.drawString( 430,                                       # Escribe el texto "¡Hola, Mundo!" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         703, 
                         "APROBADO POR:"
                        )       

# Crea un rectangulo Blanco con borde negro
ObjetoCanvas.setFillColorRGB( 1, 1, 1 )                             # Color de relleno Blanco
ObjetoCanvas.setStrokeColorRGB( 0, 0, 0 )                           # Color del borde Negro

# Recuadro de firma
ObjetoCanvas.setLineWidth(0.5)
ObjetoCanvas.rect( 65, 
                   640,    
                   160,
                   60,
                   fill = 1 
                 )
ObjetoCanvas.rect( 225, 
                   640,    
                   160,
                   60,
                   fill = 1 
                 )
ObjetoCanvas.rect( 385, 
                   640,    
                   160,
                   60,
                   fill = 1 
                 )

# Recuadro de nombres
ObjetoCanvas.rect( 65, 
                   640,    
                   160,
                   15,
                   fill = 1 
                 )
ObjetoCanvas.rect( 225, 
                   640,    
                   160,
                   15,
                   fill = 1 
                 )
ObjetoCanvas.rect( 385, 
                   640,    
                   160,
                   15,
                   fill = 1 
                 )

# Añade los nombres a los recuadros
ObjetoCanvas.setFont( "Calibri-Bold", 10 )                          # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 0, 0, 0 )                             # Asigna el color "Negro" al ObjetoCanvas

# Añade el texto: "INGENIERÍA"
ObjetoCanvas.drawString( 120,                                       # Escribe el texto "INGENIERÍA" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         644, 
                         "INGENIERÍA"
                        )       

# Añade el texto: "ANTONIO CUESTA"
ObjetoCanvas.drawString( 266,                                       # Escribe el texto "ANTONIO CUESTA" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         644, 
                         "ANTONIO CUESTA"
                        )       

# Añade el texto: "MARIO CORPA"
ObjetoCanvas.drawString( 435,                                       # Escribe el texto "MARIO CORPA" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         644, 
                         "MARIO CORPA"
                        )       

# Crea un rectangulo Gris con borde negro
ObjetoCanvas.setFillColorRGB( 166/255, 166/255, 166/255 )           # Color del relleno Gris
ObjetoCanvas.setStrokeColorRGB( 0, 0, 0 )                           # Color del borde Negro
ObjetoCanvas.setLineWidth(0.5)

# Recuadro Gris de "Fecha:"
ObjetoCanvas.rect( 65, 
                   625,    
                   80,
                   15,
                   fill = 1 
                 )
ObjetoCanvas.rect( 225, 
                   625,    
                   80,
                   15,
                   fill = 1 
                 )
ObjetoCanvas.rect( 385, 
                   625,    
                   80,
                   15,
                   fill = 1 
                 )

# Crea un rectangulo Blanco con borde Negro
ObjetoCanvas.setFillColorRGB( 1, 1, 1 )                             # Color del relleno Blanco
ObjetoCanvas.setStrokeColorRGB( 0, 0, 0 )                           # Color del borde Negro
ObjetoCanvas.setLineWidth(0.5)

# Recuadro Blanco con la Fecha
ObjetoCanvas.rect( 145, 
                   625,    
                   80,
                   15,
                   fill = 1 
                 )
ObjetoCanvas.rect( 305, 
                   625,    
                   80,
                   15,
                   fill = 1 
                 )
ObjetoCanvas.rect( 465, 
                   625,    
                   80,
                   15,
                   fill = 1 
                 )

# Añade la Fecha a los recuadros
ObjetoCanvas.setFont( "Calibri-Bold", 10 )                          # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 0, 0, 0 )                             # Asigna el color "Negro" al ObjetoCanvas

# Añade el texto "FECHA:"
ObjetoCanvas.drawString( 93,                                        # Escribe el texto "FECHA:" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         629, 
                         "FECHA"
                        )       
ObjetoCanvas.drawString( 250,                                       # Escribe el texto "FECHA:" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         629, 
                         "FECHA"
                        )  
ObjetoCanvas.drawString( 411,                                       # Escribe el texto "FECHA:" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje")
                         629, 
                         "FECHA"
                        )  


# Añade la Fecha a los recuadros
ObjetoCanvas.setFont( "Calibri", 10 )                               # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 0, 0, 0 )                             # Asigna el color "Negro" al ObjetoCanvas

# Añade la fecha 1: "00/00/0000"
ObjetoCanvas.drawString( 160,                                       # Escribe el la Fecha con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         629, 
                         Fecha
                        )       
# Añade la fecha 2: "00/00/0000"
ObjetoCanvas.drawString( 320,                                       # Escribe el la Fecha con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         629, 
                         Fecha
                        ) 
# Añade la fecha 3: "00/00/0000"
ObjetoCanvas.drawString( 480,                                       # Escribe el la Fecha con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         629, 
                         Fecha
                        ) 


####################################################################################################################

# Crea un rectangulo Azul metálico
ObjetoCanvas.setStrokeColorRGB( 51/255, 63/255, 80/255 )            # Asigna el color del borde del ObjetoCanvas
ObjetoCanvas.setFillColorRGB( 51/255, 63/255, 80/255 )              # Forma de asignar un color RGB
ObjetoCanvas.rect( 45, 
                   580,    
                   Ancho_hoja - 85, 
                   13, 
                   fill = 1 
                 )

# Añade el texto: "REGISTRO DE MODIFICACIONES"
ObjetoCanvas.setFont( "Calibri-Bold", 12 )                          # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 1, 1, 1 )                             # Asigna el color "Negro" al ObjetoCanvas
ObjetoCanvas.drawString( 220,                                       # Escribe el texto "REGISTRO DE MODIFICACIONES" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         583, 
                         "REGISTRO DE MODIFICACIONES"
                        ) 

# Crea un rectangulo Gris
ObjetoCanvas.setFillColorRGB( 166/255, 166/255, 166/255 )           # Forma de asignar un color RGB
ObjetoCanvas.setStrokeColorRGB( 166/255, 166/255, 166/255 )         # Asigna el color del borde del ObjetoCanvas
ObjetoCanvas.rect( 65, 
                   550,    
                   Ancho_hoja - 120,
                   13, 
                   fill = 1 
                 )

# Añade el texto: "MOD. Nº"
ObjetoCanvas.setFont( "Calibri-Bold", 10 )                          # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 0, 0, 0 )                             # Asigna el color "Negro" al ObjetoCanvas
ObjetoCanvas.drawString( 90,                                        # Escribe el texto "MOD. Nº" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         553, 
                         "MOD. Nº"
                        )

# Añade el texto: "FECHA MOD."
ObjetoCanvas.drawString( 170,                                       # Escribe el texto "FECHA MOD." con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         553, 
                         "FECHA MOD."
                        )

# Añade el texto: "DESCRIPCIÓN MODIFICACIÓN"
ObjetoCanvas.drawString( 350,                                       # Escribe el texto "DESCRIPCIÓN MODIFICACIÓN" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         553, 
                         "DESCRIPCIÓN MODIFICACIÓN"
                        )

# Dibujar una línea
ObjetoCanvas.setStrokeColorRGB( 0, 0, 0 )                           # Asigna el color del borde del ObjetoCanvas
ObjetoCanvas.setLineWidth(0.5)
ObjetoCanvas.line( 64.5,                                            # Crea una línea con la función: line( Posicion_X1, Posicion_Y1, Posicion_X2, Posicion_Y2 )
                   548,    
                   Ancho_hoja - 54.5,
                   548 )                        

# Añade el texto: "0"
ObjetoCanvas.setFont( "Calibri", 10 )                               # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 0, 0, 0 )                             # Asigna el color "Negro" al ObjetoCanvas
ObjetoCanvas.drawString( 103,                                       # Escribe el texto "0" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         538, 
                         "0"
                        )

# Añade la fecha: "00/00/0000"
ObjetoCanvas.drawString( 173,                                       # Escribe el la fecha con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         538, 
                         Fecha
                        )
                        
# Añade el texto: ""
ObjetoCanvas.drawString( 352,                                       # Escribe el texto "" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         538, 
                         ""
                        )

# Dibujar una línea
ObjetoCanvas.setStrokeColorRGB( 0, 0, 0 )                           # Asigna el color del borde del ObjetoCanvas
ObjetoCanvas.setLineWidth(0.5)
ObjetoCanvas.line( 64.5,                                            # Crea una línea con la función: line( Posicion_X1, Posicion_Y1, Posicion_X2, Posicion_Y2 )
                   534,    
                   Ancho_hoja - 54.5,
                   534 )                        


########################################################################################################################

ObjetoCanvas.setFont( "Calibri", 8 )                                # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 166/255, 166/255, 166/255 )           # Asigna el color "Negro" al ObjetoCanvas

# Añade el texto: ""
ObjetoCanvas.drawString( 260,                                       # Escribe el texto "" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         60,
                         "Página 1 de X - Ed. 0"
                        )

ObjetoCanvas.setFont( "Calibri-Italic", 8 )                                # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 1, 0, 0 )                             # Asigna el color "Negro" al ObjetoCanvas

# Añade el texto: ""
ObjetoTexto = ObjetoCanvas.beginText( 80, 45 )                     # Indica la posición del Texto en la página
ObjetoTexto.textLines( "La información incluida en este documento es CONFIDENCIAL. Está totalmente prohibida cualquier utilización, divulgación, distribución y/o" )
ObjetoCanvas.drawText( ObjetoTexto )                                        # Una vez redactado el texto se aplica a la hoja con la función: drawText( "Texto" )

ObjetoTexto = ObjetoCanvas.beginText( 125, 35 )                     # Indica la posición del Texto en la página
ObjetoTexto.textLines( "reproducción de esta documentación, total o parcial, sin autorización expresa en virtud de la legislación vigente." )
ObjetoCanvas.drawText( ObjetoTexto )                                        # Una vez redactado el texto se aplica a la hoja con la función: drawText( "Texto" )

ObjetoCanvas.setFont( "Calibri", 8 )                                # Cambia el tipo de fuente de texto y el tamaño con la función: setFont( "Nombre de la fuente-Estilo", Tamaño )
ObjetoCanvas.setFillColorRGB( 166/255, 166/255, 166/255 )           # Asigna el color "Negro" al ObjetoCanvas

# Añade el texto: ""
ObjetoCanvas.drawString( 100,                                       # Escribe el texto "" con la función: drawString( Posicion_X, Posicion_Y, "Mensaje") 
                         18, 
                         "COHEMO, S.L.U.  - C/Camino de las Pajarillas 8, 28935 MÓSTOLES (MADRID) - Telf. +34 91 616 52 20 -  www.cohemo.com"
                        )

ObjetoCanvas.showPage( )
ObjetoCanvas.save( )