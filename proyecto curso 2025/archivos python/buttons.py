from pygame import *
import variables

class Buttons:
    def __init__(self, x_button, y_button):
        self.x = x_button
        self.y = y_button
        self.form_button = Rect(self.x, self.y, variables.width_button, variables.height_button)
        self.is_clicked = False

    def draw_button(self, wn, text):
        draw.rect(wn, variables.color, self.form_button, 5)
        text_button = variables.fuente.render(text, True, variables.text_color)
        wn.blit(text_button, self.x + 100, self.y)

    def click(self):
        pass

    def funcion_boton(self):
        pass