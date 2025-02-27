from pygame import *

# Configuración ventana de juego
wn = display.set_mode((1024, 768))
display.set_caption("El caballero")

# Configuración de fps
clock = time.Clock()
FPS = 60    

run = True

while run:

    # Controlador de FPS
    clock.tick(FPS)

    # Cerrar el programa cuando se pulsa la X
    for event in event.get():
        if event.type == QUIT:
            run = False

    display.update()