# imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                            QLabel, QListWidget, QLineEdit, 
                            QTextEdit, QHBoxLayout, QVBoxLayout,)

# app
app = QApplication([])

'''Interfaz de la aplicación'''
# parámetros de la ventana de la aplicación
notes_win = QWidget()
notes_win.setWindowTitle('Notas inteligentes')
notes_win.resize(900, 600)

# widgets de la ventana de la aplicación

# una ventana aparece con el campo “Ingresar nombre de nota”

# organizando los widgets por diseño

# ejecutar la aplicación
notes_win.show()
app.exec_()