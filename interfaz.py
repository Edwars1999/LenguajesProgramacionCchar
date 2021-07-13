'''import sys
from PyQt5.QtGui import QIcon 
from PyQt5.QtWidgets import  *


def mensaje():
    print('Hola desde Qt')

app = QApplication(sys.argv)#Inicia la aplicacion
w = QMainWindow()#Se crea la ventana principal

w.setWindowTitle("Interprete de c#")#Se cambia el titulo de la ventana 
w.setWindowIcon(QIcon('icono.jpg')) # agregar Icono a la ventana
w.setGeometry(100,100,300,300)#posicion izquierda derecha, arriba abajo, alto ancho

b = QPushButton('Boton1',w)#Se agrega un Botton

#Accion del boton
b.clicked.connect(mensaje)

statubar = w.statusBar()
statubar.showMessage('ready')
menubar = w.menuBar()
fileMenu = menubar.addMenu('&File')
edit  = menubar.addMenu('&Editar')

exitAct = QAction(QIcon('icono.jpg') , 'E&xit' , w)
exitAct.setShortcut('crtl+Q')
exitAct.setStatusTip('Exit Menu')##Cuando pase el mouse por encima
exitAct.triggered.connect(mensaje)#cuando se dispara la accion

fileMenu.addAction(exitAct)##Se agrega esa accion al menu

w.show()# se muestra la ventana 
app.exec_()#Ejecuta la aplicacion grafica
del(app)## borra la aplicacionde la memoria ram para que exista conflicto al vover a depuarar el programa y no cree una venta encima de la ya creada

#sys.exit(app.exec_())#trona la consola de python
'''
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(10, 60, 781, 231))
        self.textEdit_1.setObjectName("textEdit_1")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 310, 381, 251))
        self.textEdit_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(410, 310, 381, 251))
        self.textEdit_3.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_3.setObjectName("textEdit_3")
        #MainWindow.setCentralWidget(self.centralwidget)
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interprete C# "))
        self.pushButton.setText(_translate("MainWindow", "EJECUTAR"))
