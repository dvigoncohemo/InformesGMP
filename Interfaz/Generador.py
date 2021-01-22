from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QColorDialog
from Fuentes_de_texto import *
from Informacion import *
from interfaz import *

import pandas as pd 
import time
import sys

class Fuente_de_texto( QtWidgets.QMainWindow, Ui_Fuentes_de_texto ):

    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        
        self.pushButton_Aceptar.clicked.connect(Fuente_de_texto.Funcion_Aceptar)
        self.pushButton_Cancelar.clicked.connect(Fuente_de_texto.Funcion_Cancelar)

    def Funcion_Aceptar( self ):
        print("Pulsado: Fuente de texto -> Aceptar")

    def Funcion_Cancelar( self ):
        print("Pulsado: Fuente de texto -> Cencelar")
        

class Espaciado_de_texto( QtWidgets.QMainWindow, Ui_informacion_version ):

    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

class Colores( QtWidgets.QMainWindow, Ui_informacion_version ):

    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

class Linea( QtWidgets.QMainWindow, Ui_informacion_version ):

    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

class Grilla( QtWidgets.QMainWindow, Ui_informacion_version ):

    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

class Ayuda( QtWidgets.QMainWindow, Ui_informacion_version ):

    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

class Sobre_Cohemo_GMP( QtWidgets.QMainWindow, Ui_informacion_version ):

    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

class Solucionar_Problemas( QtWidgets.QMainWindow, Ui_informacion_version ):

    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

class MainWindow( QtWidgets.QMainWindow, Ui_MainWindow ):

    # Variables para la barra de progreso
    Porcentaje_inicial = 0
    Porcentaje_actual = 0
    Porcentaje_final = 100

    # Variables para la entrada y salida de datos
    Archivo_de_entrada = ''
    Imagen_de_portada = ''
    Ruta_de_salida = ''

    # Método inicial de la clase
    def __init__( self, *args, **kwargs ):

        super().__init__(*args, **kwargs)        
        
        self.setupUi(self)
        self.show()   

        # QPushButton
        self.QPushButton_archivo_de_entrada.clicked.connect(self.Funcion_archivo_de_entrada)
        self.QPushButton_imagen_de_portada.clicked.connect(self.Funcion_imagen_de_portada)
        self.QPushButton_ruta_de_salida.clicked.connect(self.Funcion_ruta_de_salida)
        self.QPushbutton_generar_informe.clicked.connect(self.Funcion_generar_informe)

        # Estado inicial de la barra de progreso
        self.progressBar.setVisible(False)                                          # Oculta la barra de progreso
        self.progressBar.setValue(self.Porcentaje_inicial)                          # Barra de progreso al 0%
        
        # Menú Archivo: Enlaza las funciones con los botones
        self.action_Nuevo.triggered.connect(self.Funcion_Nuevo)
        self.action_Abrir.triggered.connect(self.Funcion_Abrir)
        self.action_Guardar.triggered.connect(self.Funcion_Guardar)
        self.action_Salir.triggered.connect(self.Funcion_Salir)
        
        # Menú Preferencias: Enlaza las funciones con los botones
        self.action_Fuente_de_texto.triggered.connect(self.Funcion_Fuente_de_texto)
        self.action_Espaciado_de_texto.triggered.connect(self.Funcion_Espaciado_de_texto)
        self.action_Colores.triggered.connect(self.Funcion_Colores)
        self.action_Linea.triggered.connect(self.Funcion_Linea)
        self.action_Grilla.triggered.connect(self.Funcion_Grilla)
        
        # Menú Ayuda: Enlaza las funciones con los botones
        self.action_Ayuda.triggered.connect(self.Funcion_Ayuda)
        self.action_Sobre_Cohemo_GMP.triggered.connect(self.Funcion_Sobre_Cohemo_GMP)
        self.action_Solucionar_problemas.triggered.connect(self.Funcion_Solucion_Problemas)

    #################################################################################################################
    #   MENÚ ARCHIVO
    #################################################################################################################

    # Función que realiza la acción de reiniciar los campos del programa mediante la ruta Archivo -> Nuevo
    def Funcion_Nuevo( self ):

        Archivo_de_entrada = ''                                             # Vacía la variable
        Imagen_de_portada = ''                                              # Vacía la variable
        Ruta_de_salida = ''                                                 # Vacía la variable

        self.Porcentaje_actual = 0                                          # Asigna el valor 0 al Porcentaje_actual de la barra de progreso
        self.progressBar.setVisible(False)                                  # Oculta la barra de progreso
    
    # Función que realiza la acción de reiniciar los campos del programa mediante la ruta Archivo -> Abrir
    def Funcion_Abrir( self ):
        app
    
    # Función que realiza la acción de reiniciar los campos del programa mediante la ruta Archivo -> Guardar
    def Funcion_Guardar( self ):
        app
    
    # Función que realiza la acción de salir del programa mediante la ruta Archivo -> Salir
    def Funcion_Salir( self ):
        window.close()
  
    #################################################################################################################
    #   MENÚ PREFERENCIAS
    #################################################################################################################

    # Función que realiza la acción de reiniciar los campos del programa mediante la ruta Archivo -> Guardar
    def Funcion_Fuente_de_texto( self ):
        Fuente_de_texto( self )
    
    # Función que realiza la acción de reiniciar los campos del programa mediante la ruta Archivo -> Guardar
    def Funcion_Espaciado_de_texto( self ):
        print("Seleccionado: Espaciado de texto")
    
    # Función que realiza la acción de reiniciar los campos del programa mediante la ruta Archivo -> Guardar
    def Funcion_Colores( self ):
        print("Seleccionado: Colores")

        color = QColorDialog.getColor()
        if color.isValid():
            print(color.name())
    
    # Función que realiza la acción de reiniciar los campos del programa mediante la ruta Archivo -> Guardar
    def Funcion_Linea( self ):
        print("Seleccionado: Línea")

    # Función que realiza la acción de reiniciar los campos del programa mediante la ruta Archivo -> Guardar
    def Funcion_Grilla( self ):
        print("Seleccionado: Grilla")
    
    #################################################################################################################
    #   MENÚ AYUDA
    #################################################################################################################

    # Función que realiza la acción de mostrar la ventana de información del programa mediante la ruta Ayuda -> Ayuda
    def Funcion_Ayuda( self ):
        Ayuda( self )                                          # Abre la ventana de información de versión del programa

    # Función que realiza la acción de mostrar la ventana de información del programa mediante la ruta Ayuda -> Ayuda
    def Funcion_Sobre_Cohemo_GMP( self ):
        Ayuda(self)                                          # Abre la ventana de información de versión del programa

    # Función que realiza la acción de mostrar la ventana de Solución de problemas
    def Funcion_Solucion_Problemas( self ):
        Solucionar_Problemas( self )

    #################################################################################################################
    #   FUNCIONES
    #################################################################################################################

    # Función que muestra y actualiza la barra de progreso
    def Funcion_barra_progreso( self ):

        self.progressBar.setVisible(True)                           # 

        while self.Porcentaje_actual < self.Porcentaje_final:       # 
            self.Porcentaje_actual += 1                             # 
            time.sleep(0.01)                                        # 
            self.progressBar.setValue(self.Porcentaje_actual)       # 

    # Función que realiza la acción de realizar las llamadas a las demás funciones encargadas de formar el informe de salida
    def Funcion_generar_informe( self ):

        self.QLineEdit_archivo_de_entrada.setText("Generando informe...") 
        self.QLineEdit_imagen_de_portada.setText("Generando informe...") 
        self.QLineEdit_ruta_de_salida.setText("Generando informe...")
        self.Funcion_barra_progreso()
    
    # Función que realiza la acción de pedir al usuario un archivo de entrada en formato .txt
    def Funcion_archivo_de_entrada( self ):

        self.Archivo_de_entrada, _ = QFileDialog.getOpenFileName( self, "Abrir...", "", "Archivos de texto (*.txt)" )
        self.QLineEdit_archivo_de_entrada.setText( self.Archivo_de_entrada ) 
            
    # Función que realiza la acción de pedir al usuario un archivo de imagen para la portada del documento en formato .jpg / .png
    def Funcion_imagen_de_portada( self ):

        self.QLineEdit_archivo_de_entrada.setText("Funcion_imagen_de_portada") 
        self.QLineEdit_imagen_de_portada.setText("Funcion_imagen_de_portada") 
        self.QLineEdit_ruta_de_salida.setText("Funcion_imagen_de_portada") 
    
    # Función que realiza la acción de pedir al usuario un directorio de salida donde se creará el informe en PDF
    def Funcion_ruta_de_salida( self ):

        self.Ruta_de_salida = QFileDialog.getExistingDirectory( self, "Guardar en..." )
        self.QLineEdit_ruta_de_salida.setText( self.Ruta_de_salida )

if __name__ == "__main__":

    app = QApplication( sys.argv )
    window = MainWindow()
    app.exec_()

