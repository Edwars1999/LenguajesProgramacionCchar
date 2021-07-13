import sys
#from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from interfaz import Ui_MainWindow
import lexcomp 
import sintax

class Principal(QWidget):
    def __init__(self):
       QWidget.__init__(self)
       self.ventana = Ui_MainWindow()
       self.ventana.setupUi(self)

       self.ventana.pushButton.clicked.connect(self.obtenerTexto)

    def obtenerTexto(self):
        self.texto = self.ventana.textEdit_1.toPlainText()
        self.salidaLex = '------------------------ANALISIS LEXICO------------------------------\n ' + lexcomp.pruebaInt(self.texto)
        self.ventana.textEdit_2.setText(self.salidaLex)
        self.salidaSin = '------------------------ANALISIS SINTAXIS--------------------------------\n' + sintax.pruebaInt(self.texto)
        self.ventana.textEdit_3.setText(self.salidaSin)


app = QApplication(sys.argv)
ventana = Principal()
ventana.show()
app.exec_()
del(app)
sys.exit(app.exec_())