from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout, QPushButton

#app
app = QApplication([])
# ventana principal:
mainwin = QWidget()
mainwin.resize(965, 476)

#######################################

texto = QLabel("Idioma oficial de Brasil")
main_layout = QVBoxLayout()
main_layout.addWidget(texto, alignment = Qt.AlignCenter)

button_answer = QPushButton("Elegir")

RadioGroupBox = QGroupBox("Opciones de respuesta")
button1 = QRadioButton("Italiano")
button2 = QRadioButton("Español")
button3 = QRadioButton("Portugués")
button4 = QRadioButton("Brasileño")

RadioAnswer = QGroupBox("Resultado de prueba")
true = QLabel("verdadero: Portugués")
false = QLabel("Falso: Portugués")

def respuesta():
    if button3.isChecked():
        RadioGroupBox.hide()
        button_answer.hide()
        RadioAnswer.show()

button_answer.clicked.connect(respuesta)
        

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(button1)
layout_ans2.addWidget(button2)
layout_ans3.addWidget(button3)
layout_ans3.addWidget(button4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
main_layout.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
main_layout.addWidget(button_answer, alignment=Qt.AlignCenter)
mainwin.setLayout(main_layout)

#######################################

#mostramos ventana principal
mainwin.show()
#mantiene app encendida
app.exec_()