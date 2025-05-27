from pygame import *
from buttons import RectButton, CircleButton
from menu_opciones import menu_opciones
import variables
from menu_niveles import levels

def menu_inicio():
    # Configuración de ventana
    wn_menu = display.set_mode((variables.WIDHT, variables.HEIGHT))
    display.set_caption("El caballero")
    background_image = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))

    # Texto de bienvenida
    text_welcome = image.load("assets/img/background/menu principal/welcome.jpg")

    # Botones
    bttnPlay = RectButton(430, 560, 200, 100, variables.colorButton)
    bttnOptions = RectButton(130, 560, 200, 100, variables.colorButton)

    while variables.menu_principal:
        # FPS
        variables.clock.tick(variables.FPS)

        # Imagen de fondo
        wn_menu.blit(background_image, (variables.bg_x, variables.bg_y))
        wn_menu.blit(text_welcome, (variables.backtext_x, variables.backtext_y))

        # Botones
        bttnPlay.draw_button(wn_menu, "Levels")
        bttnOptions.draw_button(wn_menu, "Options")

        # Cerrar al presionar la X
        for e in event.get():
            if e.type == QUIT:
                variables.menu_principal = False
                variables.game = False

            # Función de cada botón
            if bttnPlay.click(e):
                variables.menu_principal = False
                variables.menu_niveles = True
                levels()

            if bttnOptions.click(e):
                variables.menu_principal = False
                variables.menu_opciones = True
                menu_opciones()

        display.update()
