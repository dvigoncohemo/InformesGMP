import os
import reportlab
from reportlab.lib.pagesizes import A4                                      # Importa el formato de página A4 ( 595.2755905511812, 841.8897637795277 ) puntos

from reportlab.pdfgen import canvas                                         # Importa el módulo de canvas para generar archivos en .PDF
canvas = canvas.Canvas("Ejemplo12.pdf", pagesize = A4)                 # Crea el archivo "InformeGMP.pdf" en formato .PDF con las dimensiones de una hoja A4


folder = os.path.dirname(reportlab.__file__) + os.sep + 'fonts'
afmFile = os.path.join(folder, 'DarkGardenMK.afm')
pfbFile = os.path.join(folder, 'DarkGardenMK.pfb')
from reportlab.pdfbase import pdfmetrics
justFace = pdfmetrics.EmbeddedType1Face(afmFile, pfbFile)
faceName = 'DarkGardenMK' # pulled from AFM file
pdfmetrics.registerTypeFace(justFace)
justFont = pdfmetrics.Font('DarkGardenMK', faceName, 'WinAnsiEncoding')
pdfmetrics.registerFont(justFont)
canvas.setFont('DarkGardenMK', 32)
canvas.drawString(10, 150, 'This should be in')
canvas.drawString(10, 100, 'DarkGardenMK')
canvas.save( )                                                        # 