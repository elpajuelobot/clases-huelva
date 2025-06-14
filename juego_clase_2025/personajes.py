from pygame import *
from variables import config
from animaciones import *

class Player:
    def __init__(self):
        self.x = config.x_player
        self.y = config.y_player
        self.hitbox_player = Rect(self.x, self.y, config.widht_player, config.height_player)
        self.is_jumping = False
        self.jump_count = 9
        self.is_attack = False
        self.is_death = False
        self.moving_left = False
        self.moving_right = False
        self.standing = stand_right  # Imagen de pie por defecto
        self.walk_count = 0
        self.jump_anim_count = 0 # Contador de animación de salto
        self.attack_anim_count = 0 # Contador de animación de ataque
        self.death_count = 0
        self.death_timer = 0
        self.health = config.healt_player
        self.is_hurt = False
        self.num_hurt = 4
        self.attack_damage = False

    def move_player(self, keys_pressed, mouse_pressed):
        """Mueve el jugador según las teclas presionadas"""
        if not self.is_death and config.show_inventory == False:
            if keys_pressed[K_d] and self.x < 990:
                self.x += config.speed_player
                self.moving_right = True
                self.moving_left = False
                config.delta_x = 1
                # Movimiento del fondo derecha
                config.bg_x -= config.speed_background

            elif keys_pressed[K_a] and self.x > 3:
                self.x -= config.speed_player
                self.moving_left = True
                self.moving_right = False
                config.delta_x = 0
                # Movimiento del fondo izquierda
                config.bg_x += config.speed_background

            else:
                self.moving_left = False
                self.moving_right = False

            if config.delta_x == 1:
                self.standing = stand_right

            else:
                self.standing = stand_left

            if not self.is_jumping:
                if keys_pressed[K_SPACE]:
                    self.is_jumping = True
            else:
                if self.jump_count >= -9:
                    neg = 1 if self.jump_count > 0 else -1
                    self.y -= (self.jump_count ** 2) * 0.4 * neg
                    self.jump_count -= 1
                else:
                    self.is_jumping = False
                    self.jump_count = 9

            if mouse_pressed and not self.is_attack:
                self.is_attack = True
                self.attack_damage = False

    def draw(self, wn, enemy):
        # Hitbox del jugador
        self.hitbox_player = Rect(self.x, self.y, config.widht_player, config.height_player)
        draw.rect(wn, (255, 0, 0), self.hitbox_player, 2)

        self.check_dead()

        # Animación de salto
        if self.is_jumping:
            if config.delta_x == 1:
                wn.blit(jump_right_path[self.jump_anim_count // 3 % len(jump_right_path)], (self.x, self.y))
            elif config.delta_x == 0:
                wn.blit(jump_left_path[self.jump_anim_count // 3 % len(jump_left_path)], (self.x, self.y))
            else:
                wn.blit(jump_right_path[self.jump_anim_count // 3 % len(jump_right_path)], (self.x, self.y))

            self.jump_anim_count += 1 # Avanza la animación de salto

        # Animación de ataque
        elif self.is_attack:
            if config.delta_x == 1:
                config.widht_player = 42
                wn.blit(attack_right_path[self.attack_anim_count // 5 % len(attack_right_path)], (self.x, self.y))
            elif config.delta_x == 0:
                wn.blit(attack_left_path[self.attack_anim_count // 5 % len(attack_left_path)], (self.x, self.y))
            else:
                wn.blit(attack_right_path[self.attack_anim_count // 5 % len(attack_right_path)], (self.x, self.y))

            self.attack_anim_count += 1 # Avanza la animación de ataque

            # Mantener la animación de ataque hasta que acabe
            if self.attack_anim_count >= len(attack_right_path) * 5:
                self.is_attack = False
                self.attack_anim_count = 0
                config.widht_player = 35

                if not self.attack_damage:
                    self.attack_damage = True
                    self.check_collision_enemy(enemy)

        # Animación de muerte
        elif self.is_death:
            config.height_player = 35
            config.widht_player = 65
            self.y = 676
            if self.death_count < len(dead_path) * 5:
                if config.delta_x == 1:
                    wn.blit(dead_path[self.death_count // 5 % len(dead_path)], (self.x, self.y))
                else:
                    wn.blit(dead_left_path[self.death_count // 5 % len(dead_left_path)], (self.x, self.y))

                self.death_count += 1

            else:
                if self.death_timer == 0:
                    self.death_timer = time.get_ticks()
                if config.delta_x == 1:
                    wn.blit(dead_path[-1], (self.x, self.y))
                else:
                    wn.blit(dead_left_path[-1], (self.x, self.y))

                if time.get_ticks() - self.death_timer > 3000:
                    pass

        # Animación de movimiento
        else:
            if self.moving_right:
                wn.blit(walk_right_path[self.walk_count // 2 % len(walk_right_path)], (self.x, self.y))
            elif self.moving_left:
                wn.blit(walk_left_path[self.walk_count // 2 % len(walk_left_path)], (self.x, self.y))
            else:
                wn.blit(self.standing[self.walk_count // 4 % len(self.standing)], (self.x, self.y))

            self.walk_count += 1
            self.jump_anim_count = 0

    def barra_healt(self, wn, x, y):
        calculo_barra = int((self.health / 100) * config.widht_healt)
        borde = Rect(x, y, config.widht_healt, config.height_healt)
        rectangulo = Rect(x, y, calculo_barra, config.height_healt)
        draw.rect(wn, (255, 0, 255), rectangulo)
        draw.rect(wn, (0, 0, 255), borde, 3)
        text_healt = config.fuente.render(f"Vida: {self.health}", True, config.text_color)
        wn.blit(text_healt, (6, 7))
        if self.health <= 0:
            self.health = 0

    def check_dead(self):
        if self.health == 0:
            self.is_death = True

    def check_collision_enemy(self, enemy):
        if self.hitbox_player.colliderect(enemy.hitbox_enemy):
            enemy.health -= self.num_hurt
            enemy.health = max(enemy.health, 0)


class Villain:
    def __init__(self, speed):
        self.x = config.x_enemy
        self.y = config.y_enemy
        self.hitbox_enemy = Rect(self.x, self.y, config.width_enemy, config.height_enemy)
        self.standing = stand_right_villain  # Imagen de pie por defecto
        self.walk_count = 0
        self.moving_right = False
        self.moving_left = False
        self.is_attack = False
        self.attack_count = 0
        self.health = config.health_enemy
        self.dead_count = 0
        self.is_dead = False
        self.visible = True
        self.is_stand = False
        self.num_hurt = 4
        self.speed = speed

    def move_towards_player(self, player):
        if player.health > 0 and self.health > 0 and config.show_inventory == False:
            if player.x > self.x:
                self.moving_right = True
                self.moving_left = False
                self.is_attack = False
                self.x += min(self.speed, player.x - self.x)
            elif player.x < self.x:
                self.moving_right = False
                self.moving_left = True
                self.is_attack = False
                self.x -= min(self.speed, self.x - player.x)
            else:
                self.is_attack = True
        else:
            self.moving_left = False
            self.moving_right = False
            self.is_attack = False
            self.is_stand = not self.is_attack

    def draw(self, wn, player):
        if not self.visible:
            return

        self.hitbox_enemy = Rect(self.x, self.y, config.width_enemy, config.height_enemy)
        draw.rect(wn, (255, 0, 0), self.hitbox_enemy, 2)

        if self.is_dead:
            wn.blit(dead_right_villain[self.dead_count // config.ANIMATION_SPEED % len(dead_right_villain)], (self.x, self.y))
            self.dead_count += 1
            if self.dead_count >= len(dead_right_villain) * config.ANIMATION_SPEED:
                self.visible = False
            return

        if self.is_attack:
            wn.blit(attack_right_villain[self.attack_count // config.ANIMATION_SPEED % len(attack_right_villain)], (self.x, self.y))
            self.attack_count += 1

            if self.attack_count >= len(attack_right_villain) * 6:
                self.attack_count = 0
                self.check_collision_hero(player)

        elif self.moving_right:
            wn.blit(run_right_villain[self.walk_count // config.ANIMATION_SPEED % len(run_right_villain)], (self.x, self.y))

        elif self.moving_left:
            wn.blit(run_left_villain[self.walk_count // config.ANIMATION_SPEED % len(run_left_villain)], (self.x, self.y))

        else:
            wn.blit(self.standing[self.walk_count // config.ANIMATION_SPEED % len(self.standing)], (self.x, self.y))

        self.walk_count += 1

    def draw_health_bar(self, wn):
        if self.visible:
            health_ratio = max(self.health / 120, 0)  # Evitar valores negativos
            health_width = int(health_ratio * config.width_health_enemy)
            health_bar = Rect(self.x + 15, self.y - 5, health_width, config.height_health_enemy)
            draw.rect(wn, (255, 0, 255), health_bar)
            health_text = config.fuente.render(f"Vida: {self.health}", True, config.text_color)
            wn.blit(health_text, (self.x - 8, self.y - 25))
            if self.health <= 0:
                self.health = 0
                self.is_dead = True

    def check_collision_hero(self, player):
        if self.hitbox_enemy.colliderect(player.hitbox_player):
            player.health -= self.num_hurt
