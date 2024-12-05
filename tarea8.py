from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox

# App
app = QApplication([])
# Ventana principal:
mainwin = QWidget()
mainwin.resize(965, 476)
mainwin.setWindowTitle("memory card")

#######################################

# Texto
text = QLabel("Resgístrate o inicia sesión")
main_layout = QVBoxLayout()
main_layout.addWidget(text, alignment = Qt.AlignCenter)

# Grupo de opciones
RadioGroupBox = QGroupBox("Opciones de respuesta")

# Botones radio
rbtn_1 = QPushButton('Regístrate')
rbtn_2 = QPushButton ('Inicia sesión')

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
#######################################

# Mostramos ventana principal
mainwin.show()
# Mantiene app encendida
app.exec_()