from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QLineEdit, QRadioButton

# App
app = QApplication([])
# Ventana principal:
mainwin = QWidget()
mainwin.resize(965, 476)
mainwin.setWindowTitle("principal")

# Segunda ventana
mainwin2 = QWidget()
mainwin2.resize(965, 476)
mainwin2.setWindowTitle("inicio sesión")

# Tercera ventana
mainwin3 = QWidget()
mainwin3.resize(965, 476)
mainwin3.setWindowTitle("registrarse")

#######################################

''' VENTANA PRINCIPAL '''
# Texto
text = QLabel("Resgístrate o inicia sesión")
main_layout = QVBoxLayout()
main_layout.addWidget(text, alignment = Qt.AlignCenter)

# Grupo de opciones
RadioGroupBox = QGroupBox("Opciones de respuesta")

# Funciones botones
def iniciar_sesion():
    mainwin.hide()
    mainwin2.show()

def registrarte():
    mainwin.hide()
    mainwin3.show()

# Botones radio
rbtn_1 = QPushButton('Regístrate')
rbtn_2 = QPushButton ('Inicia sesión')

rbtn_2.clicked.connect(iniciar_sesion)
rbtn_1.clicked.connect(registrarte)

# Vertical horizontal
layoutHorizontal =  QHBoxLayout()
layoutVertical = QVBoxLayout()
layoutVertical2 = QVBoxLayout()

# Unir los botones con las líneas horizontales y verticales
layoutVertical.addWidget(rbtn_1)
layoutVertical2.addWidget(rbtn_2)
layoutHorizontal.addLayout(layoutVertical)
layoutHorizontal.addLayout(layoutVertical2)

# Meter los botones en la caja
RadioGroupBox.setLayout(layoutHorizontal)

main_layout.addWidget(RadioGroupBox)
mainwin.setLayout(main_layout)

''' VENTANA DE INICO DE SESIÓN '''
# Función para procesar la entrada
def cerrar_ventana():
    mainwin2.hide()
    mainwin.show()

# Función para procesar la entrada
def process_input():
    password2 = password.text()
    output_label.setText(f"Contraseña ingresada: {password2}")


# Layout principal
layout = QVBoxLayout()

# Entrada de texto
user = QLineEdit()
user.setPlaceholderText("Nombre de usuario")
layout.addWidget(user)

# Entrada de texto como contraseña
password = QLineEdit()
password.setEchoMode(QLineEdit.Password)  # Oculta el texto ingresado
password.setPlaceholderText("Escribe tu contraseña...")
layout.addWidget(password)

# Botón para procesar entrada
submit_button2 = QPushButton("Ver contraseña")
submit_button2.clicked.connect(process_input)
layout.addWidget(submit_button2)

# Etiqueta para mostrar la entrada procesada
output_label = QLabel("Tu contraseña aparecerá aquí.")
layout.addWidget(output_label)


# Botón para procesar entrada
submit_button = QPushButton("Enviar")
submit_button.clicked.connect(cerrar_ventana)
layout.addWidget(submit_button)

# Configurar layout y mostrar ventana
mainwin2.setLayout(layout)

''' VENTANA DE REGISTRO '''
# Función para procesar la entrada
def cerrar_ventana():
    mainwin3.hide()
    mainwin.show()

# Función para procesar la entrada
def process_input():
    password2 = password.text()
    output_label.setText(f"Contraseña ingresada: {password2}")


# Layout principal
layout = QVBoxLayout()
layout2 = QHBoxLayout()

# Entrada de texto
user = QLineEdit()
user.setPlaceholderText("Nombre de usuario")
layout.addWidget(user)

# Entrada de texto como contraseña
password = QLineEdit()
password.setEchoMode(QLineEdit.Password)  # Oculta el texto ingresado
password.setPlaceholderText("Escribe tu contraseña...")
layout.addWidget(password)

# Botón para procesar entrada
submit_button2 = QPushButton("Ver contraseña")
submit_button2.clicked.connect(process_input)
layout.addWidget(submit_button2)

# Etiqueta para mostrar la entrada procesada
output_label = QLabel("Tu contraseña aparecerá aquí.")
layout.addWidget(output_label)

# Género
man = QRadioButton("Hombre")
woman = QRadioButton("Mujer")
layout.addWidget(man)
layout.addWidget(woman)

# Botón para procesar entrada
submit_button = QPushButton("Enviar")
submit_button.clicked.connect(cerrar_ventana)
layout.addWidget(submit_button)

# Configurar layout y mostrar ventana
mainwin3.setLayout(layout)

#######################################

# Mostramos ventana principal
mainwin.show()
# Mantiene app encendida
app.exec_()