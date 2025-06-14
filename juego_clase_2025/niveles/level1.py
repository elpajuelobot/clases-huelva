from pygame import *
from variables import config
from personajes import Player, Villain
from random import randint
from objetos import Item, get_cell_from_mouse, draw_inventory, add_to_inventory, inventory
from animaciones import healt_potion, coin
from cinematicas.level1_cine import cinematic_level1, finalCinematic_level1


def level1():
    # Configuración ventana de juego
    wn = display.set_mode((config.WIDHT, config.HEIGHT))
    display.set_caption("El caballero")
    background = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))

    cinematic_level1(wn)

    # Personajes
    hero = Player()
    enemy = Villain(randint(2, 4))

    # Ajustes de variables
    config.health_enemy = 10

    # Ciclo del juego
    while config.game:
        # Evento de teclas
        keys_pressed = key.get_pressed()

        # Controlador de FPS
        config.clock.tick(config.FPS)

        # Actualización de x_relativa
        config.x_relativa = config.bg_x % config.WIDHT

        # Fondo pantalla
        wn.blit(background, (config.x_relativa - config.WIDHT, config.bg_y))
        wn.blit(background, (config.x_relativa, config.bg_y))

        # Heroe
        # Movimiento del heroe
        hero.move_player(keys_pressed, config.mouse_pressed)
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

        # Apagar videojuego cuando es presionada la X
        for e in event.get():
            if e.type == QUIT:
                config.game = False
                config.bg_x = 0
                config.bg_y = 0

            # Manejar click de ratón
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    config.mouse_pressed = True  # Detectar clic izquierdo del ratón

            elif e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    config.mouse_pressed = False  # Liberar clic izquierdo del ratón

            elif hero.health > 0:
                if e.type == KEYDOWN:
                    if e.key == K_e:
                        config.show_inventory = not config.show_inventory  # Abrir/cerrar inventario
                        config.dragging = False
                        config.dragged_item = None

            if config.show_inventory:
                if e.type == MOUSEBUTTONDOWN:
                    cell = get_cell_from_mouse(e.pos)
                    if cell:
                        row, col = cell
                        if inventory[row][col]:  # Si hay un ítem en la celda
                            config.dragging = True
                            # Asegúrate de clonar el ítem, para que no se modifique accidentalmente al arrastrarlo
                            config.dragged_item = inventory[row][col].copy()  # Suponiendo que 'Item' tiene un método .copy()
                            inventory[row][col] = None  # Remueve el ítem del inventario

                elif e.type == MOUSEBUTTONUP:
                    if config.dragging:
                        cell = get_cell_from_mouse(e.pos)
                        if cell:
                            row, col = cell
                            if inventory[row][col] is None:
                                inventory[row][col] = config.dragged_item  # Soltar el ítem
                            else:
                                # Apilamiento de ítems solo si son del mismo nombre
                                if inventory[row][col]["name"] == config.dragged_item["name"]:
                                    inventory[row][col]["quantity"] += config.dragged_item["quantity"]
                                else:
                                    # No deberíamos sobreponer el ítem, simplemente intercambiar
                                    if inventory[row][col] != config.dragged_item:  
                                        inventory[row][col], config.dragged_item = config.dragged_item, inventory[row][col]
                                    else:
                                        # Si son iguales, no hacer nada
                                        pass

                        config.dragging = False
                        config.dragged_item = None

        if config.show_inventory:
            draw_inventory(wn)
            if config.dragging and config.dragged_item:
                wn.blit(healt_potion, mouse.get_pos())

        if config.health_enemy == 0:
            break

        display.update()

    finalCinematic_level1(wn)
