"""from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog

#app
app = QApplication([])
# ventana principal:
mainwin = QWidget()
mainwin.resize(965, 476)

#######################################

# Botones
carpeta = QPushButton("carpeta")
left = QPushButton("izquierda")
right = QPushButton("derecha")
reflejo = QPushButton("reflejo")
nitidez = QPushButton("nitidez")
ByN = QPushButton("B/N")




#######################################

#mostramos ventana principal
mainwin.show()
#mantiene app encendida
app.exec_()"""

import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QListWidget,
                            QLabel, QHBoxLayout, QPushButton,
                            QVBoxLayout, QFileDialog)


"""APLICACION"""
app = QApplication([])


"""VENTANA PRINCIAL"""
ventana_principal = QWidget()
# tamanio
ventana_principal.resize(800, 600)
# posicion
ventana_principal.move(20, 20)
# titulo
ventana_principal.setWindowTitle("aplicación")


##################################
"""ELEMENTOS"""

# titulo de notas
lista_notas_label = QLabel('Lista de notas')
# area de lista de notas
lista_notas = QListWidget()


# boton crear nota
boton_crear_nota = QPushButton('Crear nota')

# Botones
carpeta = QPushButton("carpeta")
left = QPushButton("izquierda")
right = QPushButton("derecha")
reflejo = QPushButton("reflejo")
nitidez = QPushButton("nitidez")
ByN = QPushButton("B/N")


# Abrir el directorio
def open_directory():
    workdir = QFileDialog.getExistingDirectory()
    filenames = os.listdir(workdir)

carpeta.clicked.connect(open_directory)


####################################
"""COLOCACION"""
colunna_principal = QHBoxLayout()
ventana_principal.setLayout(colunna_principal)


colunna2 = QVBoxLayout()
colunna2.addWidget(carpeta, alignment=Qt.AlignLeft)
colunna2.addWidget(lista_notas_label)
colunna2.addWidget(lista_notas, alignment=Qt.AlignLeft)
colunna_principal.addLayout(colunna2)


fila1 = QHBoxLayout()
fila1.addWidget(left)
fila1.addWidget(right)
fila1.addWidget(reflejo)
fila1.addWidget(nitidez)
fila1.addWidget(ByN)
colunna2.addLayout(fila1)

####################################
# mostrar ventana
ventana_principal.show()
# ciclo de ejecucion
app.exec()
