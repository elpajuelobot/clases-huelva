from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QListWidget, QLineEdit

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
PushBoxGroup1 = QLabel("Lista de notas")
createButton = QPushButton("Crear nota")
deletButton = QPushButton("eliminar nota")
saveButton = QPushButton("guardar nota")


# Etiquetas
# Lista de etiquetas
label_list = QListWidget() 

# Entrada de texto
user = QLineEdit()
user.setPlaceholderText("Nombre de usuario")

# Botones
PushBoxGroup2 = QLabel("Lista de etiquetas")
addButton = QPushButton("Añadir nota")
removeButton = QPushButton("Remover etiqueta de nota")
searchButton = QPushButton("Buscar notas por etiqueta")


# Layouts
# Columnas
columV1 = QVBoxLayout()
columV2 = QVBoxLayout()
columH1 = QHBoxLayout()
columH2 = QHBoxLayout()
columH3 = QHBoxLayout()
columH4 = QHBoxLayout()
columH5 = QHBoxLayout()



'''                                                                   En proceso   
                                                                      Solo falta organizarlo todo


# Unir layouts y botones
columV1.addWidget(note_list)
columV1.addWidget(createButton)
columV1.addWidget(deletButton)
columV1.addWidget(saveButton)

columH1.addLayout(columV1)
columH1.addLayout(columV1)

# Meter los botones en la caja
PushBoxGroup1.setLayout(columH1)
PushBoxGroup2.setLayout(columH1)

mainwin.setLayout(columH1)
'''

#######################################

# Mostramos ventana principal
mainwin.show()
# Mantiene app encendida
app.exec_()
