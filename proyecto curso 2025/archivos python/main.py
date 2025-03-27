from pygame import *
import variables
from personajes import Player, Villain
from menu_inicio import menu_inicio
from random import randint
from objetos import Item, get_cell_from_mouse, draw_inventory, add_to_inventory, inventory
from animaciones import healt_potion, coin

# Configuración ventana de juego
wn = display.set_mode((variables.WIDHT, variables.HEIGHT))
display.set_caption("El caballero")
background = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))


# Personajes
hero = Player()
enemy = Villain(randint(2, 4))

# Objetos
items_on_ground = [
    Item(healt_potion, 400, 650, "Potion", 1, 30, 32),
    Item(healt_potion, 200, 650, "Potion", 1, 30, 32)
]

# Llamar al menú de inicio
menu_inicio()

# Ciclo del juego
while variables.game:

    # Evento de teclas
    keys_pressed = key.get_pressed()

    # Controlador de FPS
    variables.clock.tick(variables.FPS)

    # Actualización de x_relativa
    variables.x_relativa = variables.bg_x % variables.WIDHT

    # Fondo pantalla
    wn.blit(background, (variables.x_relativa - variables.WIDHT, variables.bg_y))
    wn.blit(background, (variables.x_relativa, variables.bg_y))

    # Heroe
    # Movimiento del heroe
    hero.move_player(keys_pressed, variables.mouse_pressed)
    # Dibujar al heroe
    hero.draw(wn, enemy)
    # Barra de vida del heroe
    hero.barra_healt(wn, 3, 4)

    # Objetos
    if enemy.health == 0:
        for item in items_on_ground:
            item.draw(wn)
        # Verificar colisiones y recoger ítems
        for item in items_on_ground[:]:  # [:] para iterar sobre una copia
            if hero.hitbox_player.colliderect(item.rect):
                if add_to_inventory(item):  # Si hay espacio en el inventario
                    items_on_ground.remove(item)  # Eliminar el objeto del suelo

    for item in items_on_ground[:]:
        item.hitbox(wn)

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
            variables.game = False
            variables.bg_x = 0
            variables.bg_y = 0

        # Manejar click de ratón
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                variables.mouse_pressed = True  # Detectar clic izquierdo del ratón

        elif e.type == MOUSEBUTTONUP:
            if e.button == 1:
                variables.mouse_pressed = False  # Liberar clic izquierdo del ratón

        elif hero.health > 0:
            if e.type == KEYDOWN:
                if e.key == K_e:
                    variables.show_inventory = not variables.show_inventory  # Abrir/cerrar inventario
                    variables.dragging = False
                    variables.dragged_item = None

        if variables.show_inventory:
            if e.type == MOUSEBUTTONDOWN:
                cell = get_cell_from_mouse(e.pos)
                if cell:
                    row, col = cell
                    if inventory[row][col]:  # Si hay un ítem en la celda
                        variables.dragging = True
                        # Asegúrate de clonar el ítem, para que no se modifique accidentalmente al arrastrarlo
                        variables.dragged_item = inventory[row][col].copy()  # Suponiendo que 'Item' tiene un método .copy()
                        inventory[row][col] = None  # Remueve el ítem del inventario

            elif e.type == MOUSEBUTTONUP:
                if variables.dragging:
                    cell = get_cell_from_mouse(e.pos)
                    if cell:
                        row, col = cell
                        if inventory[row][col] is None:
                            inventory[row][col] = variables.dragged_item  # Soltar el ítem
                        else:
                            # Apilamiento de ítems solo si son del mismo nombre
                            if inventory[row][col]["name"] == variables.dragged_item["name"]:
                                inventory[row][col]["quantity"] += variables.dragged_item["quantity"]
                            else:
                                # No deberíamos sobreponer el ítem, simplemente intercambiar
                                if inventory[row][col] != variables.dragged_item:  
                                    inventory[row][col], variables.dragged_item = variables.dragged_item, inventory[row][col]
                                else:
                                    # Si son iguales, no hacer nada
                                    pass

                    variables.dragging = False
                    variables.dragged_item = None

    if variables.show_inventory:
        draw_inventory(wn)
        if variables.dragging and variables.dragged_item:
            wn.blit(healt_potion, mouse.get_pos())

    display.update()
