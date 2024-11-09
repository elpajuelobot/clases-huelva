from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

#app
app = QApplication([])
# ventana principal:
mainwin = QWidget()
mainwin.resize(965, 476)

#######################################



#######################################

#mostramos ventana principal
mainwin.show()
#mantiene app encendida
app.exec_()