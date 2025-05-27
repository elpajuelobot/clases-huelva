import pygame

# 1. Inicializar Pygame
pygame.init()

# 2. Configurar la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dibujar Círculos en Pygame")

# Colores (en formato RGB)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Rellenar el fondo de la pantalla (opcional, pero buena práctica)
    screen.fill(WHITE) # Fondo blanco

    # 4. Dibujar un círculo rojo relleno
    center_x_red = 200
    center_y_red = 300
    radius_red = 70
    pygame.draw.circle(screen, RED, (center_x_red, center_y_red), radius_red)

    # 5. Dibujar un círculo azul con solo el contorno
    center_x_blue = 500
    center_y_blue = 300
    radius_blue = 100
    border_width_blue = 5 # Ancho del contorno de 5 píxeles
    pygame.draw.circle(screen, BLUE, (center_x_blue, center_y_blue), radius_blue, border_width_blue)

    # 6. Actualizar la pantalla para mostrar lo dibujado
    pygame.display.flip()

# 7. Salir de Pygame
pygame.quit()