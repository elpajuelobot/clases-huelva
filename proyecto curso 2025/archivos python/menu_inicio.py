from pygame import *
import variables

# Configuración de ventana
wn_menu = display.set_mode((variables.WIDHT, variables.HEIGHT))
display.set_caption("El caballero")
# Imagen de fondo
background_image = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))

# Texto de bienvenida
text_welcome = image.load("assets/img/background/menu principal/welcome.jpg")

while variables.menu_principal:
    # FPS
    variables.clock.tick(variables.FPS)

    # Cerrar al presionar la X
    for e in event.get():
        if e.type == QUIT:
            variables.menu_principal = False
            variables.game = False

    # Imagen de fondo
    wn_menu.blit(background_image, (variables.bg_x, variables.bg_y))

    display.update()