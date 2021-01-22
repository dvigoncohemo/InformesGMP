import os

#Cargamos los módulos que necesitamos.

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from reportlab.platypus import Image
from reportlab.platypus import Spacer

#Creamos objeto Canvas.
c = Canvas('Ejemplo7.pdf')

#Estilo de la hoja.
estiloHoja = getSampleStyleSheet()

#Demás estilos.
estiloN = estiloHoja['Normal']
estiloH = estiloHoja['BodyText']

#Inicializamos platypus story.
story = []

#Añadimos algunos flowables.
imagen_logo = Image("Imagen.png", width=100, height=100)
story.append(imagen_logo)

#Dejamos espacio.
story.append(Spacer(0,20))

#Añadimos un párrafo.
story.append(Paragraph("Esto es un ejemplo de frame 01",estiloN))

#Definimos un frame.
frame = Frame(3, 3, 200, 260, showBoundary=1)
frame.addFromList(story, c)

#Inicializamos platypus story.
story2 = []

#Añadimos algunos flowables.
story2.append(Paragraph("Este es el párrafo del segundo Frame",estiloH))

#Dejamos espacio.
story2.append(Spacer(0,40))

#~ #Una imagen.
imagen_logo = Image("Imagen.png", width=100, height=100)
story2.append(imagen_logo)

#Definimos otro frame.
frame2 = Frame(250, 3, 250, 250, 6, showBoundary=1)
frame2.addFromList(story2, c)

#Salvamos el PDF.
c.save()

os.system("Ejemplo7.pdf")