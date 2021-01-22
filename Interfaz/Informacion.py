from PyQt5 import QtCore, QtGui, QtWidgets
import Recursos.Python.Logo

class Ui_informacion_version(object):

    def setupUi(self, informacion_version):

        informacion_version.setObjectName("informacion_version")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Recursos\ICO\icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        informacion_version.setWindowIcon(icon)

        informacion_version.resize(450, 200)
        informacion_version.setMinimumSize(QtCore.QSize(450, 200))
        informacion_version.setMaximumSize(QtCore.QSize(450, 200))
        informacion_version.setStyleSheet("background-color: rgb(240, 240, 240);")

        self.label = QtWidgets.QLabel(informacion_version)
        self.label.setGeometry(QtCore.QRect(30, 40, 90, 90))
        self.label.setStyleSheet("image: url(:/Logo/PNG/Logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(informacion_version)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 121, 21))
        self.label_2.setStyleSheet("font: 85 11pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(informacion_version)
        self.label_3.setGeometry(QtCore.QRect(150, 40, 291, 111))
        self.label_3.setStyleSheet("font: 9pt \"Arial\";")
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(informacion_version)
        self.pushButton.setGeometry(QtCore.QRect(350, 160, 80, 25))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())

        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton.setStyleSheet(  "QPushButton {\n"
                                        "    background-color: rgb(225, 225, 225);\n"
                                        "    border: 1px solid #8f8f91;\n"
                                        "    min-width: 80px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:flat {\n"
                                        "    border: none; /* no border for a flat push button */\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:default {\n"
                                        "    border: 2px solid;\n"
                                        "    border-color: rgb(0, 120, 215);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    border: 1px solid;\n"
                                        "    border-color: rgb(0, 120, 215);\n"
                                        "    background-color: rgb(229, 241, 251);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:focus{\n"
                                        "    border-color: rgb(0, 120, 215);\n"
                                        "}"
                                    )
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(informacion_version)
        self.pushButton.clicked.connect(informacion_version.close)
        QtCore.QMetaObject.connectSlotsByName(informacion_version)

    def retranslateUi(self, informacion_version):
        _translate = QtCore.QCoreApplication.translate
        informacion_version.setWindowTitle(_translate("informacion_version", "Sobre Cohemo GMP"))
        self.label_2.setText(_translate("informacion_version", "Cohemo GMP"))
        self.label_3.setText(_translate("informacion_version", "Version 1.0\n"
                                        "Cohemo GMP es un generador de informes \n"
                                        "PDF de ensayos de grupos motopropulsores.\n"
                                        "\n"
                                        "Copyright (C) 2021 Cohemo SL."))
        self.pushButton.setText(_translate("informacion_version", "Cerrar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    informacion_version = QtWidgets.QDialog()
    ui = Ui_informacion_version()
    ui.setupUi(informacion_version)
    informacion_version.show()
    sys.exit(app.exec_())
