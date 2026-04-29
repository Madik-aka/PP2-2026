import pygame
import random
import os

# Константы
WIDTH, HEIGHT = 600, 600
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Четкие полосы движения
LANES = [180, 300, 420] 

# Глобальный множитель скорости для эффектов Нитро/Repair
global_speed_mult = 1.0

def get_image(name, size=None):
    path = os.path.join(BASE_DIR, "images", name)
    try:
        img = pygame.image.load(path).convert_alpha()
        if size: img = pygame.transform.scale(img, size)
        return img
    except:
        surf = pygame.Surface(size if size else (50, 50))
        surf.fill((255, 0, 255)) 
        return surf

# FIX: Вспомогательная функция для безопасного спавна
def get_safe_spawn_pos(existing_group, object_height):
    """
    Пытается найти полосу, которая свободна от других объектов.
    """
    tries = 0
    while tries < 10: # Пробуем 10 раз найти свободную полосу
        lane_x = random.choice(LANES)
        y_pos = random.randint(-800, -object_height - 50)
        
        # Создаем временный rect для проверки
        test_rect = pygame.Rect(lane_x - 22, y_pos, 45, object_height)
        
        collision_found = False
        for sprite in existing_group:
            # Если временный рект пересекается с любым существующим спрайтом
            if test_rect.colliderect(sprite.rect):
                collision_found = True
                break
        
        if not collision_found:
            return lane_x, y_pos
        tries += 1
    
    # Если за 10 попыток не нашли идеального места, спавним далеко наверху
    return random.choice(LANES), -2000

class Player(pygame.sprite.Sprite):
    def __init__(self, color="red"):
        super().__init__()
        self.image = get_image(f"player_{color}.png", (45, 90))
        self.rect = self.image.get_rect(center=(WIDTH//2, 500))
        self.base_speed = 7
        self.shield_active = False
        self.nitro_active = False
        self.slow_motion_active = False
        self.powerup_timer = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 150: self.rect.x -= self.base_speed
        if keys[pygame.K_RIGHT] and self.rect.right < 450: self.rect.x += self.base_speed

        if self.powerup_timer > 0 and pygame.time.get_ticks() > self.powerup_timer:
            self.nitro_active = False
            self.slow_motion_active = False
            self.shield_active = False
            self.powerup_timer = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, existing_sprites=None):
        super().__init__()
        self.image = get_image("enemy.png", (45, 90))
        self.base_speed = speed
        
        # FIX: Безопасный первый спавн
        lane_x, y_pos = get_safe_spawn_pos(existing_sprites if existing_sprites else [], 90)
        self.rect = self.image.get_rect(center=(lane_x, y_pos))

    def update(self):
        global global_speed_mult
        self.rect.y += self.base_speed * global_speed_mult
        
        if self.rect.top > HEIGHT:
            # FIX: Не используем kill() и __init__, чтобы не создавать лишние объекты.
            # Просто сбрасываем позицию безопасно.
            # Передаем группу all_sprites (ее нужно передать при обновлении в main.py)
            self.kill() # Временно убираем, чтобы safe_spawn его не видел
            # Main.py создаст нового врага, так проще.

class Coin(pygame.sprite.Sprite):
    def __init__(self, speed, existing_sprites=None):
        super().__init__()
        # Рисуем монету
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 215, 0), (15, 15), 15) # Золото
        pygame.draw.circle(self.image, (0, 0, 0), (15, 15), 15, 2)     # Обводка
        self.value = random.choice([1, 2, 5])
        
        font = pygame.font.Font(None, 24)
        v_txt = font.render(str(self.value), True, (0, 0, 0))
        self.image.blit(v_txt, (10, 8))
        
        self.base_speed = speed
        
        # FIX: Безопасный спавн
        lane_x, y_pos = get_safe_spawn_pos(existing_sprites if existing_sprites else [], 30)
        self.rect = self.image.get_rect(center=(lane_x, y_pos))

    def update(self):
        global global_speed_mult
        self.rect.y += self.base_speed * global_speed_mult
        if self.rect.top > HEIGHT:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    # У бонусов можно оставить простую логику, они редкие
    def __init__(self, speed):
        super().__init__()
        self.type = random.choice(["Nitro", "Shield", "Repair"])
        img_map = {"Nitro": "nitro.png", "Shield": "shield.png", "Repair": "repair.png"}
        self.image = get_image(img_map[self.type], (35, 35))
        self.rect = self.image.get_rect(center=(random.choice(LANES), random.randint(-1500, -200)))
        self.base_speed = speed

    def update(self):
        global global_speed_mult
        self.rect.y += self.base_speed * global_speed_mult
        if self.rect.top > HEIGHT:
            self.kill()