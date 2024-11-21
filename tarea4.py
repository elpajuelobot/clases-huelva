from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QMessageBox

# App
app = QApplication([])
# Ventana principal:
mainwin = QWidget()
mainwin.resize(400, 200)
mainwin.windowTitle("Memory Card")

#######################################

text = QLabel("¿Qué nacionalidad no existe?")
main_layout = QVBoxLayout()
main_layout.addWidget(text, alignment = Qt.AlignCenter)

button_answer = QPushButton("Respuesta")

RadioGroupBox = QGroupBox("Opciones de respuesta")
rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton ('Pitufos')
rbtn_3 = QRadioButton ('Chulyms')
rbtn_4 = QRadioButton('Aleutas')

def respuesta():
    if rbtn_2.isChecked():
        QMessageBox.information(mainwin, "Correcto", "Correcto")
    else:
        QMessageBox.warning(mainwin, "Incorrecto", "Incorrecto")

button_answer.clicked.connect(respuesta)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

main_layout.addWidget(RadioGroupBox)
main_layout.addWidget(button_answer)
mainwin.setLayout(main_layout)
#######################################

# Mostramos ventana principal
mainwin.show()
# Mantiene app encendida
app.exec_()