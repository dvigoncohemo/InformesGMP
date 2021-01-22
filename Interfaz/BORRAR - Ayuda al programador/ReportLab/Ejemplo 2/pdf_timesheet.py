from reportlab.lib.pagesizes import A4             # Importa el tamaño y formato del documento
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

# Importa fuentes de texto personalizadas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak, Image, Spacer, Table, TableStyle)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

from reportlab.graphics.shapes import Line, LineShape, Drawing
from reportlab.lib.colors import Color

class FooterCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.Paginas = []
        self.width, self.height = A4

    def showPage(self):
        self.Paginas.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        Contador_paginas = len(self.Paginas)
        for Pagina_actual in self.Paginas:
            self.__dict__.update(Pagina_actual)
            if (self._pageNumber > 1):
                self.draw_canvas(Contador_paginas)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas( self, Contador_paginas ):

        Pagina_actual = "Página %s de %s - Ed. 0" % ( self._pageNumber, Contador_paginas )
        x = 315

        self.saveState()                                    # Guarda el estado actual de los gráficos para ser restaurados más adelante con la función:   restoreState()
        self.setStrokeColorRGB( 0, 0, 0 )                   # Modifica el color de la línea del footer
        self.setLineWidth(0.5)
        
        self.drawImage( "NUEVO_LOGO.PNG", 
                        self.width - mm * 190, 
                        self.height - 50, 
                        width = 100, 
                        height = 20, 
                        preserveAspectRatio = True 
                    )

        self.drawImage( "Bandera.jpg", 
                        self.width - mm * 45, 
                        self.height - 50, 
                        width = 100, 
                        height = 30, 
                        preserveAspectRatio = True, 
                        mask = 'auto'
                    )

        self.line( 30, 740, A4[0] - 50, 740)                # Crea una línea a partir de coordenadas:   line( x1, y1, x2, y2 )
        self.line( 66, 78, A4[0] - 66, 78)                  # Crea una línea a partir de coordenadas:   line( x1, y1, x2, y2 )
        self.setFont('Times-Roman', 8)
        self.drawString(A4[0]-x, 65, Pagina_actual)

        Nuevo_Texto = """La información incluida en este documento es CONFIDENCIAL. Está totalmente prohibida cualquier utilización, divulgación, distribución y/o reproducción de esta documentación, total o parcial, sin autorización expresa en virtud de la legislación vigente."""
        self.setFillColor( "Red" )
        self.setFontSize( size = 7 ); 
        self.drawString( A4[0] - 500, 50, Nuevo_Texto )

        self.restoreState()

class PDFPSReporte:

    def __init__( self, path ):
        self.path = path
        self.styleSheet = getSampleStyleSheet()
        self.elements = []

        self.colorOhkaGreen0 = Color((45.0/255), (166.0/255), (153.0/255), 1)
        self.colorOhkaGreen1 = Color((182.0/255), (227.0/255), (166.0/255), 1)
        self.colorOhkaGreen2 = Color((140.0/255), (222.0/255), (192.0/255), 1)
        self.colorOhkaBlue0 = Color((54.0/255), (122.0/255), (179.0/255), 1)
        self.colorOhkaBlue1 = Color((122.0/255), (180.0/255), (225.0/255), 1)
        self.colorOhkaGreenLineas = Color((50.0/255), (140.0/255), (140.0/255), 1)

        self.firstPage()
        self.nextPagesHeader(True)
        self.remoteSessionTableMaker()
        self.nextPagesHeader(False)
        self.inSiteSessionTableMaker()
        self.nextPagesHeader(False)
        self.extraActivitiesTableMaker()
        self.nextPagesHeader(False)
        self.summaryTableMaker()
        # Build
        self.doc = SimpleDocTemplate(path, pagesize=A4)
        self.doc.multiBuild(self.elements, canvasmaker=FooterCanvas)

    def firstPage( self ):

        img = Image( 'ejercito_tierra_logo.png', kind = 'proportional' )
        img.drawHeight = 1 * mm * 25.4
        img.drawWidth = 2.4 * mm * 25.4
        img.hAlign = 'LEFT'
        self.elements.append( img )

        spacer = Spacer( 30, 100 )
        self.elements.append( spacer )

        img = Image( 'Portada.png' )
        img.drawHeight = 2.5 * mm * 25.4
        img.drawWidth = 4.5 * mm * 25.4
        self.elements.append( img )

        spacer = Spacer( 10, 250 )
        self.elements.append( spacer )

        psDetalle = ParagraphStyle( 'Resumen', 
                                    fontSize = 10, 
                                    leading = 14, 
                                    justifyBreaks = 1, 
                                    alignment = TA_LEFT, 
                                    justifyLastLine = 1
                                )

        text = """REPORTE DE SERVICIOS PROFESIONALES    <br/><br/>
                  Empresa: Nombre del Cliente           <br/>
                  Fecha de Inicio: 23-Oct-2019          <br/>
                  Fecha de actualización: 01-Abril-2020 <br/>
               """
        paragraphReportSummary = Paragraph( text, psDetalle )

        self.elements.append( paragraphReportSummary )
        self.elements.append( PageBreak( ) )

    def nextPagesHeader( self, isSecondPage ):

        if isSecondPage:

            psHeaderText = ParagraphStyle('Hed0', fontSize=16, alignment=TA_LEFT, borderWidth=3, textColor=self.colorOhkaGreen0)
            text = 'REPORTE DE SESIONES'
            paragraphReportHeader = Paragraph(text, psHeaderText)
            self.elements.append(paragraphReportHeader)

            spacer = Spacer(10, 10)
            self.elements.append(spacer)

            d = Drawing(500, 1)
            line = Line(-15, 0, 483, 0)
            line.strokeColor = self.colorOhkaGreenLineas
            line.strokeWidth = 2
            d.add(line)
            self.elements.append(d)

            spacer = Spacer(10, 1)
            self.elements.append(spacer)

            d = Drawing(500, 1)
            line = Line(-15, 0, 483, 0)
            line.strokeColor = self.colorOhkaGreenLineas
            line.strokeWidth = 0.5
            d.add(line)
            self.elements.append(d)

            spacer = Spacer(10, 22)
            self.elements.append(spacer)

    def remoteSessionTableMaker( self ):    

        psHeaderText = ParagraphStyle('Hed0', fontSize=12, alignment=TA_LEFT, borderWidth=3, textColor=self.colorOhkaBlue0)
        text = 'SESIONES REMOTAS'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)
        """
        Create the line items
        """
        d = []
        textData = ["No.", "Fecha", "Hora Inicio", "Hora Fin", "Tiempo Total"]
                
        fontSize = 8
        centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
        for text in textData:
            ptext = "<font size='%s'><b>%s</b></font>" % (fontSize, text)
            titlesTable = Paragraph(ptext, centered)
            d.append(titlesTable)        

        data = [d]
        lineNum = 1
        formattedLineData = []

        alignStyle = [ ParagraphStyle( name = "01", alignment = TA_CENTER ),
                       ParagraphStyle( name = "02", alignment = TA_LEFT ),
                       ParagraphStyle( name = "03", alignment = TA_CENTER ),
                       ParagraphStyle( name = "04", alignment = TA_CENTER ),
                       ParagraphStyle( name = "05", alignment = TA_CENTER )
                    ]

        for row in range(10):
            lineData = [ str( lineNum ), 
                         "Miércoles, 11 de diciembre de 2019", 
                         "17:30", 
                         "19:24", 
                         "1:54"
                        ]
            #data.append(lineData)
            columnNumber = 0

            for item in lineData:
                ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
                p = Paragraph(ptext, alignStyle[columnNumber])
                formattedLineData.append(p)
                columnNumber = columnNumber + 1
            data.append(formattedLineData)
            formattedLineData = []
            
        # Row for total
        totalRow = ["Total de Horas", 
                    "", 
                    "", 
                    "", 
                    "30:15"
                    ]

        for item in totalRow:
            ptext = "<font size='%s'>%s</font>" % ( fontSize - 1, item )
            p = Paragraph( ptext, alignStyle[ 1 ] )
            formattedLineData.append( p )
        data.append( formattedLineData )
        
        #print(data)
        table = Table(data, colWidths=[50, 200, 80, 80, 80])
        tStyle = TableStyle([ 
                                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                                ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
                                ('LINEABOVE', (0, 0), (-1, -1), 1, self.colorOhkaBlue1),
                                ('BACKGROUND',(0, 0), (-1, 0), self.colorOhkaGreenLineas),
                                ('BACKGROUND',(0, -1),(-1, -1), self.colorOhkaBlue1),
                                ('SPAN',(0,-1),(-2,-1))
                            ])
        table.setStyle( tStyle )
        self.elements.append( table )

    def inSiteSessionTableMaker( self ):

        self.elements.append(PageBreak())
        psHeaderText = ParagraphStyle('Hed0', fontSize=12, alignment=TA_LEFT, borderWidth=3, textColor=self.colorOhkaBlue0)
        text = 'SESIONES EN SITIO'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)
        """
        Create the line items
        """
        d = []
        textData = ["No.", "Fecha", "Hora Inicio", "Hora Fin", "Tiempo Total"]
                
        fontSize = 8
        centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
        for text in textData:
            ptext = "<font size='%s'><b>%s</b></font>" % (fontSize, text)
            titlesTable = Paragraph(ptext, centered)
            d.append(titlesTable)        

        data = [d]
        lineNum = 1
        formattedLineData = []

        alignStyle = [ParagraphStyle(name="01", alignment=TA_CENTER),
                      ParagraphStyle(name="02", alignment=TA_LEFT),
                      ParagraphStyle(name="03", alignment=TA_CENTER),
                      ParagraphStyle(name="04", alignment=TA_CENTER),
                      ParagraphStyle(name="05", alignment=TA_CENTER)]

        for row in range(10):
            lineData = [str(lineNum), "Miércoles, 11 de diciembre de 2019", "17:30", "19:24", "1:54"]
           
            columnNumber = 0
            for item in lineData:
                ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
                p = Paragraph(ptext, alignStyle[columnNumber])
                formattedLineData.append(p)
                columnNumber = columnNumber + 1
            data.append(formattedLineData)
            formattedLineData = []
            
        # Row for total
        totalRow = ["Total de Horas", "", "", "", "30:15"]
        for item in totalRow:
            ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
            p = Paragraph(ptext, alignStyle[1])
            formattedLineData.append(p)
        data.append(formattedLineData)
        
        #print(data)
        table = Table(data, colWidths=[50, 200, 80, 80, 80])
        tStyle = TableStyle([ #('GRID',(0, 0), (-1, -1), 0.5, grey),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                #('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
                ('LINEABOVE', (0, 0), (-1, -1), 1, self.colorOhkaBlue1),
                ('BACKGROUND',(0, 0), (-1, 0), self.colorOhkaGreenLineas),
                ('BACKGROUND',(0, -1),(-1, -1), self.colorOhkaBlue1),
                ('SPAN',(0,-1),(-2,-1))
                ])
        table.setStyle(tStyle)
        self.elements.append(table)

    def extraActivitiesTableMaker( self ):

        self.elements.append(PageBreak())
        psHeaderText = ParagraphStyle('Hed0', fontSize=12, alignment=TA_LEFT, borderWidth=3, textColor=self.colorOhkaBlue0)
        text = 'OTRAS ACTIVIDADES Y DOCUMENTACIÓN'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)
        """
        Create the line items
        """
        d = []
        textData = ["No.", "Fecha", "Hora Inicio", "Hora Fin", "Tiempo Total"]
                
        fontSize = 8
        centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
        for text in textData:
            ptext = "<font size='%s'><b>%s</b></font>" % (fontSize, text)
            titlesTable = Paragraph(ptext, centered)
            d.append(titlesTable)        

        data = [d]
        lineNum = 1
        formattedLineData = []

        alignStyle = [ParagraphStyle(name="01", alignment=TA_CENTER),
                      ParagraphStyle(name="02", alignment=TA_LEFT),
                      ParagraphStyle(name="03", alignment=TA_CENTER),
                      ParagraphStyle(name="04", alignment=TA_CENTER),
                      ParagraphStyle(name="05", alignment=TA_CENTER)]

        for row in range(10):
            lineData = [str(lineNum), "Miércoles, 11 de diciembre de 2019", 
                                            "17:30", "19:24", "1:54"]
            #data.append(lineData)
            columnNumber = 0
            for item in lineData:
                ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
                p = Paragraph(ptext, alignStyle[columnNumber])
                formattedLineData.append(p)
                columnNumber = columnNumber + 1
            data.append(formattedLineData)
            formattedLineData = []
            
        # Row for total
        totalRow = ["Total de Horas", "", "", "", "30:15"]
        for item in totalRow:
            ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
            p = Paragraph(ptext, alignStyle[1])
            formattedLineData.append(p)
        data.append(formattedLineData)
        
        #print(data)
        table = Table(data, colWidths=[50, 200, 80, 80, 80])
        tStyle = TableStyle([ #('GRID',(0, 0), (-1, -1), 0.5, grey),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                #('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
                ('LINEABOVE', (0, 0), (-1, -1), 1, self.colorOhkaBlue1),
                ('BACKGROUND',(0, 0), (-1, 0), self.colorOhkaGreenLineas),
                ('BACKGROUND',(0, -1),(-1, -1), self.colorOhkaBlue1),
                ('SPAN',(0,-1),(-2,-1))
                ])
        table.setStyle(tStyle)
        self.elements.append(table)

    def summaryTableMaker( self ):

        self.elements.append(PageBreak())
        psHeaderText = ParagraphStyle('Hed0', fontSize=12, alignment=TA_LEFT, borderWidth=3, textColor=self.colorOhkaBlue0)
        text = 'REGISTRO TOTAL DE HORAS'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)
        """
        Create the line items
        """

        tStyle = TableStyle([
                   ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                   #('VALIGN', (0, 0), (-1, -1), 'TOP'),
                   ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
                   ('LINEABOVE', (0, 0), (-1, -1), 1, self.colorOhkaBlue1),
                   ('BACKGROUND',(-2, -1),(-1, -1), self.colorOhkaGreen2)
                   ])

        lineData = [["Sesiones remotas", "30:15"],
                    ["Sesiones en sitio", "00:00"],
                    ["Otras actividades", "00:00"],
                    ["Total de horas consumidas", "30:15"]]

        # for row in lineData:
        #     for item in row:
        #         ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
        #         p = Paragraph(ptext, centered)
        #         formattedLineData.append(p)
        #     data.append(formattedLineData)
        #     formattedLineData = []

        table = Table(lineData, colWidths=[400, 100])
        table.setStyle(tStyle)
        self.elements.append(table)

        # Total de horas contradas vs horas consumidas
        
        lineData = [["Total de horas contratadas", "120:00"],
                    ["Horas restantes por consumir", "00:00"]]

        # for row in lineData:
        #     for item in row:
        #         ptext = "<b>{}</b>".format(item)
        #         p = Paragraph(ptext, self.styleSheet["BodyText"])
        #         formattedLineData.append(p)
        #     data.append(formattedLineData)
        #     formattedLineData = []

        table = Table(lineData, colWidths=[400, 100])
        tStyle = TableStyle([
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
                ('BACKGROUND', (0, 0), (1, 0), self.colorOhkaBlue1),
                ('BACKGROUND', (0, 1), (1, 1), self.colorOhkaGreen1),
                ])
        table.setStyle(tStyle)

        spacer = Spacer(10, 50)
        self.elements.append(spacer)
        self.elements.append(table)

if __name__ == '__main__':
    report = PDFPSReporte('psreport2.pdf')
