# From PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                        QHBoxLayout, QTextEdit, QListWidget, QLineEdit, QLabel)
import json

# App
app = QApplication([])
# Ventana principal:
mainwin = QWidget()
mainwin.setWindowTitle('Notas inteligentes')
mainwin.resize(965, 476)

#######################################




# QtextEdit
text_list = QTextEdit()

# Notas
# Lista de las notas
note_list = QListWidget()

# Botones
note_list_label = QLabel("Lista de notas")
createButton = QPushButton("Crear nota")
deletButton = QPushButton("eliminar nota")
saveButton = QPushButton("guardar nota")

# Etiquetas
# Lista de etiquetas
label_list = QListWidget()

# Entrada de texto
tag = QLineEdit()
tag.setPlaceholderText("Introducir etiqueta...")

# Botones
label_list_text = QLabel("Lista de etiquetas")
addButton = QPushButton("añadir a la nota")
removeButton = QPushButton("Remover etiqueta de nota")
searchButton = QPushButton("Buscar notas por etiqueta")



# Layouts
fila1 = QHBoxLayout()
mainwin.setLayout(fila1)

colum1 = QVBoxLayout()
colum1.addWidget(text_list)
fila1.addLayout(colum1)

colum2 = QVBoxLayout()
# Notas
colum2.addWidget(note_list_label)
colum2.addWidget(note_list)

# Botones de notas
botones_note = QHBoxLayout()
botones_note.addWidget(createButton)
botones_note.addWidget(deletButton)
colum2.addLayout(botones_note)
colum2.addWidget(saveButton)

# Etiqueta
colum2.addWidget(label_list_text)
colum2.addWidget(label_list)
colum2.addWidget(tag)
fila1.addLayout(colum2)

# Botones de etiquetas
botones_label = QHBoxLayout()
botones_label.addWidget(addButton)
botones_label.addWidget(removeButton)
colum2.addLayout(botones_label)
colum2.addWidget(searchButton)

fila2 = QHBoxLayout()
colum2.addLayout(fila1)

#######################################

# Mostramos ventana principal
mainwin.show()
# Mantiene app encendida
app.exec_()