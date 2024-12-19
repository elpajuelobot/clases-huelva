from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                            QVBoxLayout, QGroupBox, QRadioButton,
                            QPushButton, QLabel, QButtonGroup)
from random import shuffle




#########################################################
app = QApplication([])


ventana_principal = QWidget()
ventana_principal.setWindowTitle('Tarjeta de memoria')


'''Interfaz para la aplicación de Tarjeta de memoria'''
btn_OK = QPushButton('Responder') # botón de responder
lb_pregunta = QLabel('¡La pregunta más difícil del mundo!') # texto de pregunta


# GRUPO DE BOTONES RADIO #################################################


RadioGroupBox = QGroupBox("Opciones de respuesta")
# grupo en la pantalla para botones de radio con respuestas
rbtn_1 = QRadioButton('Opción 1')
rbtn_2 = QRadioButton('Opción 2')
rbtn_3 = QRadioButton('Opción 3')
rbtn_4 = QRadioButton('Opción 4')


# asignacion de los botenes a un mismo grupo
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


# lineas del interior del grupbox boton
linea_h_grop1 = QHBoxLayout() # linea main horizontal grupo
linea_v_grop2 = QVBoxLayout() # lineas verticales grupo
linea_v_grop3 = QVBoxLayout()


# colocando los botones en las lines
linea_v_grop2.addWidget(rbtn_1) # dos respuestas en la primera columna
linea_v_grop2.addWidget(rbtn_2)
linea_v_grop3.addWidget(rbtn_3) # dos respuestas en la segunda columna
linea_v_grop3.addWidget(rbtn_4)


linea_h_grop1.addLayout(linea_v_grop2)
linea_h_grop1.addLayout(linea_v_grop3) # las columnas están en la misma línea


RadioGroupBox.setLayout(linea_h_grop1) # el “panel” con opciones de respuesta está listo


# GRUPO DE LA RESPUESTA #################################################


AnsGroupBox = QGroupBox("Resultado de prueba")
lb_Result = QLabel('¿Es correcto o no?')
lb_Correct = QLabel('¡Aquí estará la respuesta!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


# LINEAS  #################################
linea_h_1 = QHBoxLayout() # pregunta
linea_v_2 = QHBoxLayout() # opciones de respuesta o resultados de prueba
linea_v_3 = QHBoxLayout() # botón de “Responder”


linea_h_1 .addWidget(lb_pregunta, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
linea_v_2.addWidget(RadioGroupBox)
linea_v_2.addWidget(AnsGroupBox)
# ocultamos el grupo de la respuesta
AnsGroupBox.hide()


linea_v_3.addStretch(1)
linea_v_3.addWidget(btn_OK, stretch=2) # el botón debería ser grande
linea_v_3.addStretch(1)


# FUNCIONES #############################################################


# oculta los botones de radio y muestra la respuesta
def show_result():
    ''' mostrar panel de respuesta '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Siguiente pregunta')


# resetea los botones
def show_question():
    ''' mostrar panel de pregunta '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Responder')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


# asigna valores a la pregunta y a la respueta barajadas
def ask(question, right_answer, wrong1, wrong2, wrong3):
    ''' la función escribe el valor de la pregunta y responde en los widgets correspondientes mientras distribuye las opciones de respuesta de forma aleatoria'''
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_pregunta.setText(question)
    lb_Correct.setText(right_answer)
    show_question()




# funcion de botones
def show_correct(res):
    ''' mostrar resultado - coloca el texto escrito en “resultado” y muestra el panel correspondiente '''
    lb_Result.setText(res)
    show_result()




# funcion de validacion de la respuesta
def check_answer():
    ''' si se seleccionó una opción de respuesta, revisa y muestra el panel de respuesta '''
    if answers[0].isChecked():
        show_correct('¡Correcto!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('¡Incorrecto!')


# #################################################




# Ahora vamos a colocar las líneas que hemos creado una debajo de la otra:
linea_principal_vertical = QVBoxLayout()




linea_principal_vertical.addLayout(linea_h_1, stretch=2)
linea_principal_vertical.addLayout(linea_v_2, stretch=8)
linea_principal_vertical.addStretch(1)
linea_principal_vertical.addLayout(linea_v_3, stretch=1)
linea_principal_vertical.addStretch(1)
linea_principal_vertical.setSpacing(5) # los espacios entre el contenido


# llamamos a ask y le pasamos los argumentos
ask('El idioma nacional de Brasil', 'Portugués', 'Brasilero', 'Español', 'Italiano')
# connect llama a la funcion check_answer
btn_OK.clicked.connect(check_answer)


ventana_principal.setLayout(linea_principal_vertical)
ventana_principal.show()
app.exec()