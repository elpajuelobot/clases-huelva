from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

# App
app = QApplication([])
# Ventana principal:
mainwin = QWidget()
mainwin.resize(965, 476)

#######################################

class Widgets():
    def __init__(self, etiqueta_text: str, coord_x: float, coord_y: float):
        self.etiqueta = etiqueta_text
        self.x = coord_x
        self.y = coord_y
    def print_info(self):
        print(self.etiqueta, self.x, self.y)

class Button(Widgets):
    def __init__(self, etiqueta_text, coord_x, coord_y, button_click: bool):
        super().__init__(etiqueta_text, coord_x, coord_y)
        self.is_clicked = button_click
    def click(is_clicked):
        if is_clicked == True:
            print("Estás registrado")

button = Button(False)
button.print_info()

question = input("¿Quieres registrarte? (sí/no)")

#if question == "sí":
    



#######################################

# Mostramos ventana principal
mainwin.show()
# Mantiene app encendida
app.exec_()