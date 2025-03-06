import pygame
import random

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
healt_player = 100
speed_player = 6
delta_x = 1

# Ajustes del villano
width_enemy = 43
height_enemy = 82
x_enemy = 612
y_enemy = 634
health_enemy = 120
speed_enemy = random.randint(1, 3)
ANIMATION_SPEED = 6
num_enemies = 1

# Barra de vida
# Heroe
widht_healt = 200
height_healt = 25
# Villano
width_health_enemy = 43
height_health_enemy = 5

# Fuente texto
fuente = pygame.font.Font(None, 30)
text_color = (255, 255, 255)

# Mantener ventanas abiertas
game = False
menu_principal = True
menu_opciones = True

# Configuración de fps
clock = pygame.time.Clock()
FPS = 60

# Ajustes de menú de inicio
font_menu = pygame.font.Font(None, 36)
backtext_x = 127
backtext_y = -135

# Ajustes menú opciones


# Botones
color = 0, 190, 0