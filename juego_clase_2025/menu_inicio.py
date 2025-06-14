from pygame import *
from buttons import RectButton, CircleButton
from menu_opciones import menu_opciones
from variables import config
from menu_niveles import levels

def menu_inicio():
    # Configuración de ventana
    wn_menu = display.set_mode((config.WIDHT, config.HEIGHT))
    display.set_caption("El caballero")
    background_image = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))

    # Texto de bienvenida
    text_welcome = image.load("assets/img/background/menu principal/welcome.jpg")

    # Botones
    bttnPlay = RectButton(430, 560, 200, 100, config.colorButton)
    bttnOptions = RectButton(130, 560, 200, 100, config.colorButton)

    while config.menu_principal:
        # FPS
        config.clock.tick(config.FPS)

        # Imagen de fondo
        wn_menu.blit(background_image, (config.bg_x, config.bg_y))
        wn_menu.blit(text_welcome, (config.backtext_x, config.backtext_y))

        # Botones
        bttnPlay.draw_button(wn_menu, "Levels")
        bttnOptions.draw_button(wn_menu, "Options")

        # Cerrar al presionar la X
        for e in event.get():
            if e.type == QUIT:
                config.menu_principal = False
                config.game = False

            # Función de cada botón
            if bttnPlay.click(e):
                config.menu_principal = False
                config.menu_niveles = True
                levels()

            if bttnOptions.click(e):
                config.menu_principal = False
                config.menu_opciones = True
                menu_opciones()

        display.update()
