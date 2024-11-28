from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QRadioButton, QGroupBox

# App
app = QApplication([])

# Ventana principal:
mainwin = QWidget()
mainwin.resize(965, 476)
mainwin.setWindowTitle("memory card")

#######################################

# Texto
text = QLabel("Opciones")
main_layout = QVBoxLayout()
main_layout.addWidget(text, alignment = Qt.AlignCenter)

# Grupo de opciones
RadioGroupBox = QGroupBox("Opciones de respuesta")

# Botones radio
rbtn_1 = QRadioButton('Opcion1')
rbtn_2 = QRadioButton ('Opcion2')
rbtn_3 = QRadioButton ('Opcion3')
rbtn_4 = QRadioButton('Opcion4')

# Botón respuesta
ansButton = QPushButton("Respuesta")

# Vertical horizontal
layoutHorizontal =  QHBoxLayout()
layoutVertical = QVBoxLayout()
layoutVertical2 = QVBoxLayout()

# Unir los botones con las líneas horizontales y verticales
layoutVertical.addWidget(rbtn_1)
layoutVertical.addWidget(rbtn_2)
layoutVertical2.addWidget(rbtn_3)
layoutVertical2.addWidget(rbtn_4)
layoutHorizontal.addLayout(layoutVertical)
layoutHorizontal.addLayout(layoutVertical2)

# Meter los botones en la caja
RadioGroupBox.setLayout(layoutHorizontal)

main_layout.addWidget(RadioGroupBox)
main_layout.addWidget(ansButton)
mainwin.setLayout(main_layout)

#######################################

# Mostramos ventana principal
mainwin.show()
app.exec_()
# Mantiene app encendida