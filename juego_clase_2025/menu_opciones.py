from pygame import *
from buttons import RectButton, CircleButton
from variables import config

def menu_opciones():
    # Configuración de ventana
    wn_menu_option = display.set_mode((config.WIDHT, config.HEIGHT))
    display.set_caption("El caballero")
    background_image = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))

    # Botones
    bttnBack = RectButton(0, 0, 100, 50, config.colorButton)
    bttnMoreSpeed = RectButton(100, 300, 100, 50, config.colorButton)
    bttnLessSpeed = RectButton(300, 300, 100, 50, config.colorButton)

    # Ciclo de la ventana
    while config.menu_opciones:
        # FPS
        config.clock.tick(config.FPS)

        # Imagen de fondo
        wn_menu_option.blit(background_image, (config.bg_x, config.bg_y))

        # Botones
        bttnBack.draw_button(wn_menu_option, "<--")
        bttnMoreSpeed.draw_button(wn_menu_option, "+")
        bttnLessSpeed.draw_button(wn_menu_option, "-")

        # Cerrar al presionar la X
        for e in event.get():
            if e.type == QUIT:
                config.menu_opciones = False
                config.menu_principal = False
                config.game = False

            if bttnBack.click(e):
                config.menu_opciones = False
                config.menu_principal = True

            if bttnMoreSpeed.click(e):
                config.speed_player = min(config.speed_player + 1, 16)

            if bttnLessSpeed.click(e):
                config.speed_player = max(config.speed_player - 1, 1)

        # Texto para velocidad
        speedText = config.fontMenuOpciones.render("Velocidad", True, config.text_color)
        wn_menu_option.blit(speedText, (190, 260))

        speedText_num = config.fontMenuOpciones.render(f"{config.speed_player}", True, config.text_color)
        wn_menu_option.blit(speedText_num, (246, 320))

        display.update()
