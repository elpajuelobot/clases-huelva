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
note_list_label = QLabel("Lista de notas")
createButton = QPushButton("Crear nota")
deletButton = QPushButton("Eliminar nota")
saveButton = QPushButton("Guardar nota")

# Etiquetas
# Lista de etiquetas
label_list = QListWidget() 

# Entrada de texto
user = QLineEdit()
user.setPlaceholderText("Nombre de usuario")

# Botones
label_list_text = QLabel("Lista de etiquetas")
addButton = QPushButton("Añadir nota")
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

# Añadimos los botones en un QHBoxLayout
botonesNotasLayout = QHBoxLayout()
botonesNotasLayout.addWidget(createButton)
botonesNotasLayout.addWidget(deletButton)
colum2.addLayout(botonesNotasLayout)  # Agregamos el layout horizontal a la columna

# Etiquetas
colum2.addWidget(label_list_text)
colum2.addWidget(label_list)
fila1.addLayout(colum2)

#######################################

# Mostramos ventana principal
mainwin.show()
# Mantiene app encendida
app.exec_()
