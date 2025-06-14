from pygame import *
from variables import config

class Item:
    def __init__(self, image, x, y, name, quantity, width, height):
        self.x = x
        self.y = y
        self.image = image  # Imagen del objeto
        self.rect = Rect(self.x, self.y, width, height)
        self.name = name
        self.quantity = quantity
        self.color = (255, 165, 0)  # Naranja

    def draw(self, wn):
        wn.blit(self.image, (self.x, self.y))

    def hitbox(self, wn):
        draw.rect(wn, (255, 0, 0), self.rect, 2)


# Inventario: Lista de listas con diccionarios de ítems
inventory = [[None for _ in range(config.COLUMNS)] for _ in range(config.ROWS)]

def draw_inventory(wn):
    """Dibuja el inventario en la pantalla y muestra el nombre y cantidad al pasar el ratón."""
    draw.rect(
        wn, (200, 200, 200),
        (config.inv_x - 10, config.inv_y - 10,
        config.COLUMNS * config.CELL_SIZE + 20, config.ROWS * config.CELL_SIZE + 20)
    )  # Fondo del inventario

    mouse_x, mouse_y = mouse.get_pos()
    hovered_item = None

    for row in range(config.ROWS):
        for col in range(config.COLUMNS):
            x = config.inv_x + col * config.CELL_SIZE
            y = config.inv_y + row * config.CELL_SIZE

            draw.rect(wn, config.GRAY, (x, y, config.CELL_SIZE, config.CELL_SIZE), 2)  # Cuadrícula

            item = inventory[row][col]
            if item:
                # Dibujar imagen centrada
                img_x = x + (config.CELL_SIZE - item["image"].get_width()) // 2
                img_y = y + (config.CELL_SIZE - item["image"].get_height()) // 2
                wn.blit(item["image"], (img_x, img_y))

                # Dibujar cantidad en la esquina inferior derecha
                quantity_text = config.font_inventary.render(str(item["quantity"]), True, config.BLACK)
                wn.blit(quantity_text, (x + config.CELL_SIZE - 10, y + config.CELL_SIZE - 15))

                # Comprobar si el cursor está sobre esta celda
                if x <= mouse_x < x + config.CELL_SIZE and y <= mouse_y < y + config.CELL_SIZE:
                    hovered_item = item  # Guardar el objeto sobre el que está el ratón

    # Dibujar el nombre y la cantidad si el cursor está sobre un objeto
    if hovered_item:
        item_name = f"{hovered_item['name']} x{hovered_item['quantity']}"
        text = config.font_inventary.render(item_name, True, (255, 255, 255))
        text_x, text_y = mouse_x + 10, mouse_y + 10  # Mostrar cerca del cursor

        # Medidas de la caja
        padding = 8
        bg_width = text.get_width() + padding * 2
        bg_height = text.get_height() + padding

        # Crear una superficie con canal alfa (para opacidad)
        tooltip_surf = Surface((bg_width, bg_height), SRCALPHA)
        tooltip_surf.fill((0, 0, 0, 180))  # Color negro con opacidad

        # Dibujar bordes redondeados
        draw.rect(tooltip_surf, (0, 0, 0, 180), (0, 0, bg_width, bg_height), border_radius=10)

        # Renderizar la caja y el texto en la pantalla
        wn.blit(tooltip_surf, (text_x, text_y))
        wn.blit(text, (text_x + padding - 2, text_y + padding - 4))  # Ajuste fino del texto

def get_cell_from_mouse(pos):
    """Obtiene la celda del inventario según la posición del mouse"""
    x, y = pos
    # Verifica si el cursor está dentro de los límites del inventario
    if config.inv_x <= x < config.inv_x + config.COLUMNS * config.CELL_SIZE and config.inv_y <= y < config.inv_y + config.ROWS * config.CELL_SIZE:
        col = (x - config.inv_x) // config.CELL_SIZE
        row = (y - config.inv_y) // config.CELL_SIZE
        return row, col

    return None

def add_to_inventory(item):
    """Agrega un ítem al inventario, ya sea un objeto Item o un diccionario."""
    item_name = item.name if isinstance(item, Item) else item["name"]
    item_quantity = item.quantity if isinstance(item, Item) else item["quantity"]
    item_image = item.image if isinstance(item, Item) else item["image"]

    # Primero intenta apilar si ya existe el mismo objeto
    for row in range(config.ROWS):
        for col in range(config.COLUMNS):
            if inventory[row][col] and inventory[row][col]["name"] == item_name:
                inventory[row][col]["quantity"] += item_quantity
                return True

    # Si no existe, intenta colocar en una celda vacía
    for row in range(config.ROWS):
        for col in range(config.COLUMNS):
            if inventory[row][col] is None:
                inventory[row][col] = {"name": item_name, "quantity": item_quantity, "image": item_image}
                return True

    return False  # Inventario lleno
