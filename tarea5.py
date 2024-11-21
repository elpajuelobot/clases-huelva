from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QMessageBox

#app
app = QApplication([])
# ventana principal:
mainwin = QWidget()
mainwin.resize(965, 476)

#######################################

text = QLabel("opciones de impresión")
main_layout = QVBoxLayout()
main_layout.addWidget(text, alignment = Qt.AlignLeft)

button_answer = QPushButton("Elegir")

RadioGroupBox = QGroupBox("Opciones de impresión")
rbtn_1 = QRadioButton('Color')
rbtn_2 = QRadioButton ('Blanco & negro')

def option():
    if rbtn_1.isChecked() or rbtn_2.isChecked():
        QMessageBox.information(mainwin, " ", "Se ha añadido correctamente")

button_answer.clicked.connect(option)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

main_layout.addWidget(RadioGroupBox, alignment=Qt.AlignLeft)
main_layout.addWidget(button_answer, alignment=Qt.AlignLeft, stretch=1)
mainwin.setLayout(main_layout)

#######################################

#mostramos ventana principal
mainwin.show()
#mantiene app encendida
app.exec_()