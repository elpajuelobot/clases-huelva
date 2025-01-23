import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPolygon, QPainter, QBrush, QRegion
from PyQt5.QtCore import Qt, QPoint

class TriangleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Establecer el título de la ventana y su tamaño
        self.setWindowTitle('Ventana Triangular')
        self.setGeometry(100, 100, 400, 400)

        # Eliminar el marco de la ventana
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Hacer la ventana triangular
        self.setMask(self.create_triangle_mask())

        # Crear el botón de cierre (X)
        self.close_button = QPushButton('X', self)
        self.close_button.setGeometry(350, 10, 40, 40)  # Posición de la X en la ventana
        self.close_button.setStyleSheet("background-color: red; color: white; font-size: 20px; border-radius: 20px;")
        self.close_button.clicked.connect(self.close)

    def create_triangle_mask(self):
        # Crear un triángulo con tres vértices
        triangle = QPolygon([
            QPoint(200, 50),  # Vértice superior
            QPoint(50, 350),  # Vértice inferior izquierdo
            QPoint(350, 350)  # Vértice inferior derecho
        ])

        # Crear una máscara a partir del triángulo
        mask = QRegion(triangle)
        return mask

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.green))

        # Dibujar el triángulo dentro de la ventana
        painter.drawPolygon(QPolygon([
            QPoint(200, 50),
            QPoint(50, 350),
            QPoint(350, 350)
        ]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TriangleWindow()
    window.show()
    sys.exit(app.exec_())

