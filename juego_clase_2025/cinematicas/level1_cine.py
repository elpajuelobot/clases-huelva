import pygame
import sys
from variables import config

# --- Mensajes de la Cinemática ---
message1 = "Buenas caballero, estás a punto de embarcarte en una gran historia. Pero primero debes demostrarme lo que vales."
message2 = "En primer lugar, tendrás que derrotar a este monstruo. Una vez derrotado pasaremos al siguiente entrenamiento."
message3 = "Bien hecho, lo has derrotado. Pasemos al siguiente nivel."
message3_1 = "Vaya, ese monstruo ha podido contigo, pero no te rindas, inténtalo de nuevo." 


# --- Fuente ---
pygame.font.init()
font = pygame.font.Font(None, 35)

def render_multiline_text(text, font, color, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())

    surfaces = [font.render(line, True, color) for line in lines]
    return surfaces

def cinematic_level1(screen):
    # --- Recursos ---
    background = pygame.transform.scale(pygame.image.load("assets/img/background/area juego/background.png").convert(), (config.WIDHT, config.HEIGHT))
    original_hero_image = pygame.image.load("assets/img/players/hero/_idle_0.png").convert_alpha()

    cinematic_data = [
        (message1, 5),
        (message2, 5)
    ]

    current_scene_index = 0
    start_time = pygame.time.get_ticks()
    cinematic_running = True

    while cinematic_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_SPACE, pygame.K_RETURN]:
                    current_scene_index += 1
                    start_time = pygame.time.get_ticks()
                    if current_scene_index >= len(cinematic_data):
                        cinematic_running = False

        if not cinematic_running:
            break

        current_message, duration_seconds = cinematic_data[current_scene_index]
        if pygame.time.get_ticks() - start_time > duration_seconds * 1000:
            current_scene_index += 1
            start_time = pygame.time.get_ticks()
            if current_scene_index >= len(cinematic_data):
                cinematic_running = False

        # Dibujado
        screen.blit(background, (0, 0))

        # Mostrar personaje
        target_size = (800, 800)
        scaled_hero = pygame.transform.scale(original_hero_image, target_size)
        crop_height = int(scaled_hero.get_height() * 0.7)
        hero_display_surface = scaled_hero.subsurface(0, 0, scaled_hero.get_width(), crop_height)
        hero_x_pos = -200
        hero_y_pos = config.HEIGHT - hero_display_surface.get_height()
        screen.blit(hero_display_surface, (hero_x_pos, hero_y_pos))

        # Mostrar texto multilinea
        text_x_pos = hero_x_pos + hero_display_surface.get_width() - 50
        text_y_pos = config.HEIGHT // 4
        max_text_width = config.WIDHT - text_x_pos - 60

        text_surfaces = render_multiline_text(current_message, font, (255, 255, 255), max_text_width)

        text_bg_height = sum(s.get_height() + 10 for s in text_surfaces) + 20
        text_bg_surface = pygame.Surface((max_text_width + 40, text_bg_height), pygame.SRCALPHA)
        text_bg_surface.fill((0, 0, 0, 180))
        screen.blit(text_bg_surface, (text_x_pos - 20, text_y_pos - 20))

        y_offset = text_y_pos
        for surface in text_surfaces:
            screen.blit(surface, (text_x_pos, y_offset))
            y_offset += surface.get_height() + 10

        pygame.display.flip()
        config.clock.tick(config.FPS)

def finalCinematic_level1(screen):
    # --- Recursos ---
    background = pygame.transform.scale(pygame.image.load("assets/img/background/area juego/background.png").convert(), (config.WIDHT, config.HEIGHT))
    original_hero_image = pygame.image.load("assets/img/players/hero/_idle_0.png").convert_alpha()

    cinematic_data = [
        (message3, 5),
        (message3_1, 5)
    ]

    current_scene_index = 0
    start_time = pygame.time.get_ticks()
    cinematic_running = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_SPACE, pygame.K_RETURN]:
                    current_scene_index += 1
                    start_time = pygame.time.get_ticks()
                    if current_scene_index >= len(cinematic_data):
                        cinematic_running = False

        if not cinematic_running:
            break

        current_message, duration_seconds = cinematic_data[current_scene_index]
        if pygame.time.get_ticks() - start_time > duration_seconds * 1000:
            current_scene_index += 1
            start_time = pygame.time.get_ticks()
            if current_scene_index >= len(cinematic_data):
                cinematic_running = False
        # Dibujado
        screen.blit(background, (0, 0))

        # Mostrar personaje
        target_size = (800, 800)
        scaled_hero = pygame.transform.scale(original_hero_image, target_size)
        crop_height = int(scaled_hero.get_height() * 0.7)
        hero_display_surface = scaled_hero.subsurface(0, 0, scaled_hero.get_width(), crop_height)
        hero_x_pos = -200
        hero_y_pos = config.HEIGHT - hero_display_surface.get_height()
        screen.blit(hero_display_surface, (hero_x_pos, hero_y_pos))

        # Mostrar texto multilinea
        text_x_pos = hero_x_pos + hero_display_surface.get_width() - 50
        text_y_pos = config.HEIGHT // 4
        max_text_width = config.WIDHT - text_x_pos - 60

        text_surfaces = render_multiline_text(current_message, font, (255, 255, 255), max_text_width)

        text_bg_height = sum(s.get_height() + 10 for s in text_surfaces) + 20
        text_bg_surface = pygame.Surface((max_text_width + 40, text_bg_height), pygame.SRCALPHA)
        text_bg_surface.fill((0, 0, 0, 180))
        screen.blit(text_bg_surface, (text_x_pos - 20, text_y_pos - 20))

        y_offset = text_y_pos
        for surface in text_surfaces:
            screen.blit(surface, (text_x_pos, y_offset))
            y_offset += surface.get_height() + 10

        pygame.display.flip()
        config.clock.tick(config.FPS)


