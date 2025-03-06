from pygame import *
import variables

# Cargar imágenes de animación del jugador
walk_right_path = [transform.scale(image.load(f'assets/img/players/hero/RunR_{i}.png'), (variables.widht_player, variables.height_player)) for i in range(0, 9)]
walk_left_path = [transform.scale(image.load(f'assets/img/players/hero/RunL_{i}.png'), (variables.widht_player, variables.height_player)) for i in range(0, 9)]
stand_right = [transform.scale(image.load(f'assets/img/players/hero/_idle_{i}.png'), (variables.widht_player, variables.height_player)) for i in range(0, 9)]
stand_left = [transform.scale(image.load(f'assets/img/players/hero/_idleL_{i}.png'), (variables.widht_player, variables.height_player)) for i in range(0, 9)]
jump_right_path = [transform.scale(image.load(f'assets/img/players/hero/_Jump_{i}.png'), (variables.widht_player, variables.height_player)) for i in range(0, 2)]
jump_left_path = [transform.scale(image.load(f'assets/img/players/hero/_JumpL_{i}.png'), (variables.widht_player, variables.height_player)) for i in range(0, 2)]
attack_right_path = [transform.scale(image.load(f'assets/img/players/hero/_Attack_{i}.png'), (variables.widht_player, variables.height_player)) for i in range(0, 9)]
attack_left_path = [transform.scale(image.load(f'assets/img/players/hero/_AttackL_{i}.png'), (variables.widht_player, variables.height_player)) for i in range(0, 9)]
dead_path = [transform.scale(image.load(f'assets/img/players/hero/_Death_{i}.png'), (65, 35)) for i in range(0, 9)]
dead_left_path = [transform.scale(image.load(f'assets/img/players/hero/_DeathL_{i}.png'), (65, 35)) for i in range(0, 9)]

# Cargar imágenes del villano
stand_right_villain = [transform.scale(image.load(f'assets/img/players/villian/NightBorne_Idle_{i}.png'), (variables.width_enemy, variables.height_enemy)) for i in range(0, 8)]
dead_right_villain = [transform.scale(image.load(f'assets/img/players/villian/NightBorne_Death_{i}.png'), (variables.width_enemy, variables.height_enemy)) for i in range(0, 22)]
run_right_villain = [transform.scale(image.load(f'assets/img/players/villian/NightBorne_Run_{i}.png'), (variables.width_enemy, variables.height_enemy)) for i in range(0, 5)]
run_left_villain = [transform.scale(image.load(f'assets/img/players/villian/NightBorne_RunL_{i}.png'), (variables.width_enemy, variables.height_enemy)) for i in range(0, 5)]
attack_right_villain = [transform.scale(image.load(f'assets/img/players/villian/NightBorne_Attack_{i}.png') ,(variables.width_enemy, variables.height_enemy)) for i in range(0, 11)]




class Player:
    def __init__(self):
        self.x = variables.x_player
        self.y = variables.y_player
        self.hitbox_player = Rect(self.x, self.y, variables.widht_player, variables.height_player)
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
        self.health = variables.healt_player
        self.is_hurt = False
        self.num_hurt = 4
        self.attack_damage = False

    def move_player(self, keys_pressed):
        """Mueve el jugador según las teclas presionadas"""
        if not self.is_death:
            if keys_pressed[K_d] and self.x < 990:
                self.x += variables.speed_player
                self.moving_right = True
                self.moving_left = False
                variables.delta_x = 1
                # Movimiento del fondo derecha
                variables.bg_x -= variables.speed_background

            elif keys_pressed[K_a] and self.x > 3:
                self.x -= variables.speed_player
                self.moving_left = True
                self.moving_right = False
                variables.delta_x = 0
                # Movimiento del fondo izquierda
                variables.bg_x += variables.speed_background

            else:
                self.moving_left = False
                self.moving_right = False

            if variables.delta_x == 1:
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

            if keys_pressed[K_1] and not self.is_attack:
                self.is_attack = True
                self.attack_damage = False

    def draw(self, wn, enemy):
        # Hitbox del jugador
        self.hitbox_player = Rect(self.x, self.y, variables.widht_player, variables.height_player)
        draw.rect(wn, (255, 0, 0), self.hitbox_player, 2)

        # Animación de salto
        if self.is_jumping:
            if variables.delta_x == 1:
                wn.blit(jump_right_path[self.jump_anim_count // 3 % len(jump_right_path)], (self.x, self.y))
            elif variables.delta_x == 0:
                wn.blit(jump_left_path[self.jump_anim_count // 3 % len(jump_left_path)], (self.x, self.y))
            else:
                wn.blit(jump_right_path[self.jump_anim_count // 3 % len(jump_right_path)], (self.x, self.y))

            self.jump_anim_count += 1 # Avanza la animación de salto

        # Animación de ataque
        elif self.is_attack:
            if variables.delta_x == 1:
                variables.widht_player = 42
                wn.blit(attack_right_path[self.attack_anim_count // 5 % len(attack_right_path)], (self.x, self.y))
            elif variables.delta_x == 0:
                wn.blit(attack_left_path[self.attack_anim_count // 5 % len(attack_left_path)], (self.x, self.y))
            else:
                wn.blit(attack_right_path[self.attack_anim_count // 5 % len(attack_right_path)], (self.x, self.y))

            self.attack_anim_count += 1 # Avanza la animación de ataque

            # Mantener la animación de ataque hasta que acabe
            if self.attack_anim_count >= len(attack_right_path) * 5:
                self.is_attack = False
                self.attack_anim_count = 0
                variables.widht_player = 35

                if not self.attack_damage:
                    self.attack_damage = True
                    self.check_collision_enemy(enemy)

        # Animación de muerte
        elif self.is_death:
            variables.height_player = 35
            variables.widht_player = 65
            self.y = 676
            if self.death_count < len(dead_path) * 5:
                if variables.delta_x == 1:
                    wn.blit(dead_path[self.death_count // 5 % len(dead_path)], (self.x, self.y))
                else:
                    wn.blit(dead_left_path[self.death_count // 5 % len(dead_left_path)], (self.x, self.y))

                self.death_count += 1

            else:
                if self.death_timer == 0:
                    self.death_timer = time.get_ticks()
                if variables.delta_x == 1:
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
        calculo_barra = int((self.health / 100) * variables.widht_healt)
        borde = Rect(x, y, variables.widht_healt, variables.height_healt)
        rectangulo = Rect(x, y, calculo_barra, variables.height_healt)
        draw.rect(wn, (255, 0, 255), rectangulo)
        draw.rect(wn, (0, 0, 255), borde, 3)
        text_healt = variables.fuente.render(f"Vida: {self.health}", True, variables.text_color)
        wn.blit(text_healt, (6, 7))
        if self.health <= 0:
            self.health = 0

    def check_dead(self):
        if self.health == 0:
            self.is_death = True

    def check_collision_enemy(self, enemy):
        if self.hitbox_player.colliderect(enemy.hitbox_enemy):
            enemy.health -= self.num_hurt

'''
class Villian:
    def __init__(self):
        self.x = variables.x_enemy
        self.y = variables.y_enemy
        self.hitbox_enemy = Rect(self.x, self.y, variables.widht_enemy, variables.height_enemy)
        self.standing = stand_right_villian  # Imagen de pie por defecto
        self.walk_count = 0
        self.moving_right = False
        self.moving_left = False
        self.is_attack = False
        self.attack_count = 0
        self.healt = variables.healt_enemy
        self.dead_count = 0
        self.visible = True
        self.delta_x = 1
        self.is_stand = False

    def move_enemy(self, player):
        if self.healt > 0:
            if self.visible:
                if player.x > self.x:
                    self.moving_right = True
                    self.moving_left = False
                    self.is_attack = False
                    self.x += variables.speed_enemy

                elif player.x < self.x:
                    self.moving_right = False
                    self.moving_left = True
                    self.is_attack = False
                    self.x -= variables.speed_enemy

                else:
                    self.is_attack = True

                    if player.healt == 0:
                        self.is_attack = False
                        self.moving_left = False
                        self.moving_right = False
                        self.is_stand = True
        else:
            self.moving_left = False
            self.moving_right = False
            self.is_attack = False

    def draw(self, wn):
        if self.visible:
            # Hitbox del enemigo
            self.hitbox_enemy = Rect(self.x, self.y, variables.widht_enemy, variables.height_enemy)
            #draw.rect(wn, (255, 0, 0), self.hitbox_enemy, 2)

            if self.healt == 0:
                # Animación de muerte
                wn.blit(dead_right_villian[self.dead_count // 6 % len(dead_right_villian)], (self.x, self.y))
                self.dead_count += 1

                if self.dead_count >= len(dead_right_villian) * 6:
                    self.visible = False
            if self.is_attack:
                # Animación de ataque
                wn.blit(attack_right_villian[self.attack_count // 6 % len(attack_right_villian)], (self.x, self.y))
                self.attack_count += 1

            else:
                if self.moving_left == True or self.moving_right == True:
                    if self.moving_right:
                        wn.blit(run_right_villian[self.walk_count // 6 % len(run_right_villian)], (self.x, self.y))

                    elif self.moving_left:
                        wn.blit(run_left_villian[self.walk_count // 6 % len(run_left_villian)], (self.x, self.y))

                    elif self.is_stand:
                        # Posición parada
                        wn.blit(stand_right_villian[self.walk_count // 6 % len(self.standing)], (self.x, self.y))

                    self.walk_count += 1

    def barra_healt(self, wn):
        if self.visible:
            calculo_barra = int((self.healt / 120) * variables.widht_healt_enemy)
            rectangulo = Rect(self.x + 15, self.y - 5, calculo_barra, variables.height_healt_enemy)
            draw.rect(wn, (255, 0, 255), rectangulo)
            text_healt = variables.fuente.render(f"Vida: {self.healt}", True, variables.text_color)
            wn.blit(text_healt, (self.x - 8, self.y - 25))
            if self.healt <= 0:
                self.healt = 0
'''

class Villain:
    def __init__(self):
        self.x = variables.x_enemy
        self.y = variables.y_enemy
        self.hitbox_enemy = Rect(self.x, self.y, variables.width_enemy, variables.height_enemy)
        self.standing = stand_right_villain  # Imagen de pie por defecto
        self.walk_count = 0
        self.moving_right = False
        self.moving_left = False
        self.is_attack = False
        self.attack_count = 0
        self.health = variables.health_enemy
        self.dead_count = 0
        self.visible = True
        self.is_stand = False
        self.num_hurt = 4
        self.attack_damage = False

    def move_towards_player(self, player):
        if player.health > 0 and self.health > 0:
            if player.x > self.x:
                self.moving_right = True
                self.moving_left = False
                self.is_attack = False
                self.x += variables.speed_enemy
            elif player.x < self.x:
                self.moving_right = False
                self.moving_left = True
                self.is_attack = False
                self.x -= variables.speed_enemy
            else:
                self.is_attack = True
                self.attack_damage = True
        else:
            self.moving_left = False
            self.moving_right = False
            self.is_attack = False
            self.is_stand = True

    def draw(self, wn, player):
        if not self.visible:
            return

        self.hitbox_enemy = Rect(self.x, self.y, variables.width_enemy, variables.height_enemy)
        draw.rect(wn, (255, 0, 0), self.hitbox_enemy, 2)

        if self.health == 0:
            wn.blit(dead_right_villain[self.dead_count // variables.ANIMATION_SPEED % len(dead_right_villain)], (self.x, self.y))
            self.dead_count += 1
            if self.dead_count >= len(dead_right_villain) * variables.ANIMATION_SPEED:
                self.visible = False
            return

        if self.is_attack:
            wn.blit(attack_right_villain[self.attack_count // variables.ANIMATION_SPEED % len(attack_right_villain)], (self.x, self.y))
            self.attack_count += 1

            if self.attack_count >= len(attack_right_villain) * 6:
                self.attack_count = 0
                if not self.attack_damage:
                        self.attack_damage = True
                        self.check_collision_hero(player)

        elif self.moving_right:
            wn.blit(run_right_villain[self.walk_count // variables.ANIMATION_SPEED % len(run_right_villain)], (self.x, self.y))

        elif self.moving_left:
            wn.blit(run_left_villain[self.walk_count // variables.ANIMATION_SPEED % len(run_left_villain)], (self.x, self.y))

        else:
            wn.blit(self.standing[self.walk_count // variables.ANIMATION_SPEED % len(self.standing)], (self.x, self.y))

        self.walk_count += 1

    def draw_health_bar(self, wn):
        if self.visible:
            health_ratio = max(self.health / 120, 0)  # Evitar valores negativos
            health_width = int(health_ratio * variables.width_health_enemy)
            health_bar = Rect(self.x + 15, self.y - 5, health_width, variables.height_health_enemy)
            draw.rect(wn, (255, 0, 255), health_bar)
            health_text = variables.fuente.render(f"Vida: {self.health}", True, variables.text_color)
            wn.blit(health_text, (self.x - 8, self.y - 25))

    def check_collision_hero(self, player):
        if self.hitbox_enemy.colliderect(player.hitbox_player):
            player.health -= self.num_hurt
