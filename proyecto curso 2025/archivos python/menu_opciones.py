from pygame import *
from buttons import Buttons
import variables

def menu_opciones():
    # Configuración de ventana
    wn_menu_option = display.set_mode((variables.WIDHT, variables.HEIGHT))
    display.set_caption("El caballero")
    background_image = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))

    # Botones
    bttnBack = Buttons(0, 0, 100, 50)
    bttnMoreSpeed = Buttons(100, 300, 100, 50)
    bttnLessSpeed = Buttons(300, 300, 100, 50)

    # Ciclo de la ventana
    while variables.menu_opciones:
        # FPS
        variables.clock.tick(variables.FPS)

        # Imagen de fondo
        wn_menu_option.blit(background_image, (variables.bg_x, variables.bg_y))

        # Botones
        bttnBack.draw_button(wn_menu_option, "<--")
        bttnMoreSpeed.draw_button(wn_menu_option, "+")
        bttnLessSpeed.draw_button(wn_menu_option, "-")

        # Cerrar al presionar la X
        for e in event.get():
            if e.type == QUIT:
                variables.menu_opciones = False
                variables.menu_principal = False
                variables.game = False

            if bttnBack.click(e):
                variables.menu_opciones = False
                variables.menu_principal = True

            if bttnMoreSpeed.click(e):
                variables.speed_player = min(variables.speed_player + 1, 16)

            if bttnLessSpeed.click(e):
                variables.speed_player = max(variables.speed_player - 1, 1)

        # Texto para velocidad
        speedText = variables.fontMenuOpciones.render("Velocidad", True, variables.text_color)
        wn_menu_option.blit(speedText, (190, 260))

        speedText_num = variables.fontMenuOpciones.render(f"{variables.speed_player}", True, variables.text_color)
        wn_menu_option.blit(speedText_num, (246, 320))

        display.update()
