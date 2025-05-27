import pygame

pygame.init()

# Ajustes de la pantalla de juego
WIDHT = 1024
HEIGHT = 768
bg_x = 0
bg_y = 0
speed_background = 5
x_relativa = bg_x % WIDHT


# Ajustes de jugador
widht_player = 35
height_player = 65
x_player = WIDHT // 2
y_player = 646
healt_player = 10
speed_player = 6
delta_x = 1
mouse_pressed = False

# Ajustes del villano
width_enemy = 43
height_enemy = 82
x_enemy = 612
y_enemy = 634
health_enemy = 2
ANIMATION_SPEED = 6

# Barra de vida
# Heroe
widht_healt = 200
height_healt = 25
# Villano
width_health_enemy = 43
height_health_enemy = 5
attack_range = 10

# texto
fuente = pygame.font.Font(None, 30)
text_color = (255, 255, 255)

# Mantener ventanas abiertas
game = False
menu_principal = True
menu_opciones = True
menu_niveles = True

# Configuración de fps
clock = pygame.time.Clock()
FPS = 60

# Ajustes de menú de inicio
font_menu = pygame.font.Font(None, 36)
backtext_x = 127
backtext_y = -135

# Ajustes menú opciones
fontMenuOpciones = pygame.font.Font(None, 39)

# Botones
colorButton = (0, 190, 0)

# Inventario
show_inventory = False
dragging = False
dragged_item = None
ROWS = 4
COLUMNS = 5
CELL_SIZE = 50
inv_x = WIDHT // 2
inv_y = HEIGHT // 2
GRAY = (169, 169, 169)
BLACK = (0, 0, 0)
font_inventary = pygame.font.Font(None, 19)

# Objetos
take_object = False
