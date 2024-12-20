from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox

# App
app = QApplication([])
# Ventana principal:
mainwin = QWidget()
mainwin.resize(400, 200)
mainwin.setWindowTitle("Competición de Crazy People")

#######################################
# Funciones para los botones
def button_2005():
    # Crear un mensaje emergente
    msg = QMessageBox()
    msg.setWindowTitle("Correcto")
    msg.setText("¡Correcto! Ganaste un scooter gyro.")
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)  # Botón para cerrar el mensaje
    msg.exec_()  # Mostrar el mensaje

def other_buttons():
    # Crear un mensaje emergente
    msg = QMessageBox()
    msg.setWindowTitle("incorrecto")
    msg.setText("No, fue en el 2005. Ganaste un póster de la empresa.")
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)  # Botón para cerrar el mensaje
    msg.exec_()  # Mostrar el mensaje

question = QLabel("¿En qué año el canal recibió su “botón de reproducción dorado de YouTube?")

# Definir los botones
button_1 = QRadioButton("2005")
button_2 = QRadioButton("2010")
button_3 = QRadioButton("2015")
button_4 = QRadioButton("2020")

# Añadir funciones a los botones
button_1.clicked.connect(button_2005)
button_2.clicked.connect(other_buttons)
button_3.clicked.connect(other_buttons)
button_4.clicked.connect(other_buttons)

# Mostrar la información en la aplicación
layout_main = QVBoxLayout()

layout_main.addWidget(question, alignment = Qt.AlignCenter)
layout_main.addWidget(button_1, alignment = Qt.AlignCenter)
layout_main.addWidget(button_2, alignment = Qt.AlignCenter)
layout_main.addWidget(button_3, alignment = Qt.AlignCenter)
layout_main.addWidget(button_4, alignment = Qt.AlignCenter)

mainwin.setLayout(layout_main)
#######################################

# Mostramos ventana principal
mainwin.show()
# Mantiene app encendida
app.exec_()
