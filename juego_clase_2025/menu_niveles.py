from pygame import *
from buttons import RectButton, CircleButton
from menu_opciones import menu_opciones
from variables import config
from niveles.level1 import level1

def levels():
    wn_menu_levels = display.set_mode((config.WIDHT, config.HEIGHT))
    display.set_caption("El caballero")
    background_image = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))

    # Botones
    bttnLevel1 = CircleButton(200, config.HEIGHT//2, 50, config.colorButton)
    bttnBack = RectButton(0, 0, 100, 50, config.colorButton)

    while config.menu_niveles:
        # FPS
        config.clock.tick(config.FPS)

        # Imagen de fondo
        wn_menu_levels.blit(background_image, (config.bg_x, config.bg_y))

        for e in event.get():
            if e.type == QUIT:
                config.menu_niveles = False
                config.menu_opciones = False
                config.menu_principal = False
                config.game = False

            if bttnLevel1.click(e):
                config.menu_niveles = False
                config.menu_opciones = False
                config.menu_principal = False
                config.game = True
                level1()

            if bttnBack.click(e):
                config.menu_niveles = False
                config.menu_principal = True
                config.menu_opciones = False
                config.game = False

        bttnLevel1.draw(wn_menu_levels, "Nivel1")
        bttnBack.draw_button(wn_menu_levels, "<--")

        display.update()

