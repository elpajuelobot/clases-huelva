import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movimiento con Cámara")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Definir la clase Potion
class Potion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)

# Definir la clase Enemy
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.speed = 2  # Velocidad de persecución

    def move_towards(self, target_x, target_y):
        """Haz que el enemigo se mueva hacia las coordenadas del jugador"""
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        # Normalizamos el vector de dirección
        if distance != 0:
            dx /= distance
            dy /= distance
        
        # Movemos al enemigo hacia el jugador
        self.x += dx * self.speed
        self.y += dy * self.speed

# Definir la clase Game
class Game:
    def __init__(self):
        self.player_x = 100
        self.player_y = 100
        self.camera_x = 0
        self.camera_y = 0
        self.camera_speed = 5
        self.player_image = pygame.Surface((50, 50))
        self.player_image.fill((0, 0, 255))

        # Crear pociones y enemigos de ejemplo
        self.potions = [Potion(random.randint(200, 600), random.randint(100, 500)) for _ in range(5)]
        self.enemies = [Enemy(random.randint(200, 600), random.randint(100, 500)) for _ in range(3)]

    def move_camera(self):
        """Mover la cámara con el jugador"""
        self.camera_x = self.player_x - SCREEN_WIDTH // 2
        self.camera_y = self.player_y - SCREEN_HEIGHT // 2

    def update_player_position(self, dx, dy):
        """Actualizar la posición del jugador"""
        self.player_x += dx
        self.player_y += dy
        self.move_camera()  # Mover la cámara con el jugador

    def update_enemies(self):
        """Hacer que los enemigos persigan al jugador"""
        for enemy in self.enemies:
            enemy.move_towards(self.player_x, self.player_y)

    def draw(self):
        """Dibuja los objetos y el jugador con el movimiento de la cámara"""
        # Fondo blanco para simular el mundo
        screen.fill(WHITE)
        
        # Dibujar las pociones (ajustar la posición con la cámara)
        for potion in self.potions:
            screen.blit(potion.image, (potion.x - self.camera_x, potion.y - self.camera_y))
        
        # Dibujar los enemigos (ajustar la posición con la cámara)
        for enemy in self.enemies:
            screen.blit(enemy.image, (enemy.x - self.camera_x, enemy.y - self.camera_y))
        
        # Dibujar al jugador (ajustar la posición con la cámara)
        screen.blit(self.player_image, (self.player_x - self.camera_x, self.player_y - self.camera_y))

# Función principal del juego
def main():
    clock = pygame.time.Clock()
    game = Game()

    running = True
    while running:
        clock.tick(60)  # 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Controlar el movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            game.update_player_position(-game.camera_speed, 0)
        if keys[pygame.K_RIGHT]:
            game.update_player_position(game.camera_speed, 0)
        if keys[pygame.K_UP]:
            game.update_player_position(0, -game.camera_speed)
        if keys[pygame.K_DOWN]:
            game.update_player_position(0, game.camera_speed)

        # Actualizar la posición de los enemigos
        game.update_enemies()

        # Dibujar todo en la pantalla
        game.draw()

        # Actualizar la pantalla
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
