from pygame import *
from buttons import RectButton, CircleButton
from menu_opciones import menu_opciones
import variables
from niveles.level1 import level1

def levels():
    wn_menu_levels = display.set_mode((variables.WIDHT, variables.HEIGHT))
    display.set_caption("El caballero")
    background_image = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))

    # Botones
    bttnLevel1 = CircleButton(200, variables.HEIGHT//2, 50, variables.colorButton)
    bttnBack = RectButton(0, 0, 100, 50, variables.colorButton)

    while variables.menu_niveles:
        # FPS
        variables.clock.tick(variables.FPS)

        # Imagen de fondo
        wn_menu_levels.blit(background_image, (variables.bg_x, variables.bg_y))

        for e in event.get():
            if e.type == QUIT:
                variables.menu_niveles = False
                variables.menu_opciones = False
                variables.menu_principal = False
                variables.game = False

            if bttnLevel1.click(e):
                variables.menu_niveles = False
                variables.menu_opciones = False
                variables.menu_principal = False
                variables.game = True
                level1()

            if bttnBack.click(e):
                variables.menu_niveles = False
                variables.menu_principal = True
                variables.menu_opciones = False
                variables.game = False

        bttnLevel1.draw(wn_menu_levels, "Nivel1")
        bttnBack.draw_button(wn_menu_levels, "<--")

        display.update()

