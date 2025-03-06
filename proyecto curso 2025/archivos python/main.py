from pygame import *
import variables
from personajes import Player, Villain
from menu_inicio import menu_inicio

# Configuración ventana de juego
wn = display.set_mode((variables.WIDHT, variables.HEIGHT))
display.set_caption("El caballero")
background = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))


# Personajes
hero = Player()
enemy = Villain()

# Llamar al menú de inicio
menu_inicio()

# Ciclo del juego
while variables.game:

    # Evento de teclas
    keys_pressed = key.get_pressed()

    # Apagar videojuego cuando es presionada la X
    for e in event.get():
        if e.type == QUIT:
            variables.game = False
            variables.bg_x = 0
            variables.bg_y = 0

    # Controlador de FPS
    variables.clock.tick(variables.FPS)

    # Actualización de x_relativa
    variables.x_relativa = variables.bg_x % variables.WIDHT

    wn.blit(background, (variables.x_relativa - variables.WIDHT, variables.bg_y))
    wn.blit(background, (variables.x_relativa, variables.bg_y))

    # Personajes
    # Heroe
    # Movimiento del heroe
    hero.move_player(keys_pressed)
    # Dibujar al heroe
    hero.draw(wn, enemy)
    # Barra de vida del heroe
    hero.barra_healt(wn, 3, 4)

    # Villano
    # Dibujar al villano
    enemy.draw(wn, hero)
    # movimientos villano
    enemy.move_towards_player(hero)
    # Barra de vida
    enemy.draw_health_bar(wn)

    display.update()
