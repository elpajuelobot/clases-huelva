from pygame import *
import variables

class Buttons:
    def __init__(self, x_button, y_button, width, height):
        self.x = x_button
        self.y = y_button
        self.width_button = width
        self.height_button = height
        self.form_button = Rect(self.x, self.y, self.width_button, self.height_button)

    def draw_button(self, wn, text):
        draw.rect(wn, variables.color, self.form_button)
        text_surface = variables.font_menu.render(text, True, variables.text_color)
        text_rect = text_surface.get_rect(center=self.form_button.center)
        wn.blit(text_surface, text_rect)

    def click(self, event):
        if event.type == MOUSEBUTTONDOWN and self.form_button.collidepoint(event.pos):
            return True
        return False
