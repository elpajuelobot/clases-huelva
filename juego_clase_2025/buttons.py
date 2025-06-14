from pygame import *
from variables import config


class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class RectButton(Shape):
    def __init__(self, x_button, y_button, width, height, color):
        super().__init__(x_button, y_button, color)
        self.color = color
        self.x = x_button
        self.y = y_button
        self.width_button = width
        self.height_button = height
        self.form_button = Rect(self.x, self.y, self.width_button, self.height_button)

    def draw_button(self, wn, text):
        draw.rect(wn, self.color, self.form_button)
        text_surface = config.font_menu.render(text, True, config.text_color)
        text_rect = text_surface.get_rect(center=self.form_button.center)
        wn.blit(text_surface, text_rect)

    def click(self, event):
        if event.type == MOUSEBUTTONDOWN and self.form_button.collidepoint(event.pos):
            return True
        return False

class CircleButton(Shape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.color = color
        self.radio = radius
        self.center_button = (self.x + self.radio, self.y + self.radio)

    def draw(self, wn, text):
        draw.circle(wn, self.color, self.center_button, self.radio)
        text_surface = config.font_menu.render(text, True, config.text_color)
        text_rect = text_surface.get_rect(center=self.center_button)
        wn.blit(text_surface, text_rect)

    def click(self, event):
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                distance = ((mouse_x - self.center_button[0])**2 + (mouse_y - self.center_button[1])**2)**0.5
                if distance <= self.radio:
                    return True
            return False
