import pygame

pygame.init()

class Variables:
    def __init__(self):
        # Ajustes de la pantalla de juego
        self.WIDHT = 1024
        self.HEIGHT = 768
        self.bg_x = 0
        self.bg_y = 0
        self.speed_background = 5
        self.x_relativa = self.bg_x % self.WIDHT


        # Ajustes de jugador
        self.widht_player = 35
        self.height_player = 65
        self.x_player = self.WIDHT // 2
        self.y_player = 646
        self.healt_player = 100
        self.speed_player = 6
        self.delta_x = 1
        self.mouse_pressed = False

        # Ajustes del villano
        self.width_enemy = 43
        self.height_enemy = 82
        self.x_enemy = 612
        self.y_enemy = 634
        self.health_enemy = 100
        self.ANIMATION_SPEED = 6

        # Barra de vida
        # Heroe
        self.widht_healt = 200
        self.height_healt = 25
        # Villano
        self.width_health_enemy = 43
        self.height_health_enemy = 5
        self.attack_range = 10

        # texto
        self.fuente = pygame.font.Font(None, 30)
        self.text_color = (255, 255, 255)

        # Mantener ventanas abiertas
        self.game = False
        self.menu_principal = True
        self.menu_opciones = True
        self.menu_niveles = True

        # Configuración de fps
        self.clock = pygame.time.Clock()
        self.FPS = 60

        # Ajustes de menú de inicio
        self.font_menu = pygame.font.Font(None, 36)
        self.backtext_x = 127
        self.backtext_y = -135

        # Ajustes menú opciones
        self.fontMenuOpciones = pygame.font.Font(None, 39)

        # Botones
        self.colorButton = (0, 190, 0)

        # Inventario
        self.show_inventory = False
        self.dragging = False
        self.dragged_item = None
        self.ROWS = 4
        self.COLUMNS = 5
        self.CELL_SIZE = 50
        self.inv_x = self.WIDHT // 2
        self.inv_y = self.HEIGHT // 2
        self.GRAY = (169, 169, 169)
        self.BLACK = (0, 0, 0)
        self.font_inventary = pygame.font.Font(None, 19)

        # Objetos
        self.take_object = False

config = Variables()
