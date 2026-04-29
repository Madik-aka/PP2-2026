import pygame
import sys
import os
import random
from persistence import load_settings, save_settings, load_leaderboard, save_score
from ui import Button, TextInput
import racer # Импортируем модуль целиком для доступа к global_speed_mult

# Инициализация
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Extreme Racer PRO 2026")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)

# Загрузка настроек
settings = load_settings()

# ================= ЗВУКИ =================
def load_sound(name):
    path = os.path.join(BASE_DIR, "sounds", name)
    try:
        return pygame.mixer.Sound(path)
    except:
        return None

snd_crash = load_sound("crash.wav")
snd_coin = load_sound("coin.wav")
snd_nitro = load_sound("nitro.wav")

# ================= ГРАФИКА МЕНЮ =================
try:
    menu_bg = pygame.image.load(os.path.join(BASE_DIR, "images", "menu_bg.png")).convert()
    menu_bg = pygame.transform.scale(menu_bg, (WIDTH, HEIGHT))
except:
    menu_bg = None

# ================= ФУНКЦИИ ОТРИСОВКИ =================
def draw_enviroment():
    """Отрисовка дороги с анимацией скорости"""
    screen.fill((45, 45, 45)) # Асфальт
    pygame.draw.rect(screen, (34, 139, 34), (0, 0, 150, HEIGHT)) # Трава слева
    pygame.draw.rect(screen, (34, 139, 34), (450, 0, 150, HEIGHT)) # Трава справа
    
    # Белые линии обочины
    pygame.draw.line(screen, (255, 255, 255), (150, 0), (150, HEIGHT), 5)
    pygame.draw.line(screen, (255, 255, 255), (450, 0), (450, HEIGHT), 5)
    
    # Анимированная разметка
    speed_factor = 10 * racer.global_speed_mult
    offset = (pygame.time.get_ticks() * (speed_factor / 10)) % 40
    for y in range(-40, HEIGHT, 40):
        pygame.draw.line(screen, (200, 200, 200), (300, y + offset), (300, y + 20 + offset), 3)

def draw_hud(player, score, distance):
    """Интерфейс во время гонки"""
    s_txt = font.render(f"SCORE: {score}", True, (255, 255, 0))
    d_txt = font.render(f"DIST: {int(distance)}m", True, (255, 255, 255))
    screen.blit(s_txt, (165, 20))
    screen.blit(d_txt, (320, 20))
    
    if player.nitro_active:
        screen.blit(font.render("NITRO BOOST!", True, (255, 100, 0)), (WIDTH//2 - 80, 70))
    if player.slow_motion_active:
        screen.blit(font.render("SLOW-MO REPAIR", True, (0, 255, 255)), (WIDTH//2 - 100, 70))
    if player.shield_active:
        pygame.draw.circle(screen, (0, 200, 255), player.rect.center, 55, 3)

# ================= ОБЪЕКТЫ =================
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
powerups = pygame.sprite.Group()

def reset_game():
    global all_sprites, enemies, coins, powerups, player, score, distance
    score = 0
    distance = 0
    racer.global_speed_mult = 1.0
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    
    player = racer.Player(color=settings.get("car_color", "red"))
    all_sprites.add(player)
    
    # Первые враги без коллизий при спавне
    for _ in range(2):
        e = racer.Enemy(random.randint(4, 6), existing_sprites=all_sprites)
        all_sprites.add(e); enemies.add(e)

# Кнопки интерфейса
btn_play = Button(200, 220, 200, 50, "START", (0, 150, 0))
btn_garage = Button(200, 300, 200, 50, "GARAGE", (100, 100, 100))
btn_board = Button(200, 380, 200, 50, "SCORES", (0, 100, 150))
btn_quit = Button(200, 460, 200, 50, "EXIT", (150, 0, 0))
btn_back = Button(200, 500, 200, 50, "BACK", (60, 60, 60))

# Кнопки гаража
btn_red = Button(150, 250, 80, 40, "RED", (200, 0, 0))
btn_green = Button(260, 250, 80, 40, "GREEN", (0, 180, 0))
btn_blue = Button(370, 250, 80, 40, "BLUE", (0, 0, 180))

name_input = TextInput(200, 250, 200, 45, "Name")
state = "MENU"
player_name = "Racer"

# ================= ГЛАВНЫЙ ЦИКЛ =================
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if state == "NAME_INPUT":
            res = name_input.handle_event(event)
            if res:
                player_name = res
                reset_game()
                state = "PLAY"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "MENU":
                if btn_play.is_clicked(event): state = "NAME_INPUT"
                if btn_garage.is_clicked(event): state = "GARAGE"
                if btn_board.is_clicked(event): state = "LEADERBOARD"
                if btn_quit.is_clicked(event): running = False
            elif state == "GARAGE":
                if btn_red.is_clicked(event): settings["car_color"] = "red"; save_settings(settings)
                if btn_green.is_clicked(event): settings["car_color"] = "green"; save_settings(settings)
                if btn_blue.is_clicked(event): settings["car_color"] = "blue"; save_settings(settings)
                if btn_back.is_clicked(event): state = "MENU"
            elif state == "LEADERBOARD":
                if btn_back.is_clicked(event): state = "MENU"

    # --- ЛОГИКА ИГРЫ ---
    if state == "PLAY":
        # Управление скоростью мира
        if player.nitro_active:
            racer.global_speed_mult = 3.0 
            distance += 0.5
        elif player.slow_motion_active:
            racer.global_speed_mult = 0.4 
            distance += 0.05
        else:
            racer.global_speed_mult = 1.0
            distance += 0.1

        draw_enviroment()
        all_sprites.update()
        
        # Спавн без "прилипания"
        if len(coins) < 3 and random.randint(1, 80) == 1:
            c = racer.Coin(5, existing_sprites=all_sprites)
            all_sprites.add(c); coins.add(c)
        
        if len(enemies) < 2 and random.randint(1, 100) == 1:
            e = racer.Enemy(random.randint(5, 7), existing_sprites=all_sprites)
            all_sprites.add(e); enemies.add(e)

        if len(powerups) < 1 and random.randint(1, 300) == 1:
            p = racer.PowerUp(5)
            all_sprites.add(p); powerups.add(p)

        # Коллизии
        if pygame.sprite.spritecollideany(player, enemies):
            if player.shield_active:
                player.shield_active = False
                for e in pygame.sprite.spritecollide(player, enemies, True):
                    new_e = racer.Enemy(random.randint(4, 7), existing_sprites=all_sprites)
                    all_sprites.add(new_e); enemies.add(new_e)
            else:
                if snd_crash: snd_crash.play()
                save_score(player_name, score, distance)
                state = "MENU"

        for c in pygame.sprite.spritecollide(player, coins, True):
            score += c.value
            if snd_coin: snd_coin.play()

        for p in pygame.sprite.spritecollide(player, powerups, True):
            if p.type == "Nitro":
                if snd_nitro: snd_nitro.play()
                player.nitro_active, player.slow_motion_active = True, False
                player.powerup_timer = pygame.time.get_ticks() + 3000
            elif p.type == "Repair":
                player.slow_motion_active, player.nitro_active = True, False
                player.powerup_timer = pygame.time.get_ticks() + 6000 
            elif p.type == "Shield":
                player.shield_active = True
                player.powerup_timer = pygame.time.get_ticks() + 5000

        all_sprites.draw(screen)
        draw_hud(player, score, distance)

    # --- РЕНДЕР МЕНЮ ---
    elif state == "MENU":
        if menu_bg: screen.blit(menu_bg, (0, 0))
        else: screen.fill((20, 20, 20))
        title = big_font.render("RACER PRO 2026", True, (255, 215, 0))
        screen.blit(title, (WIDTH//2 - 190, 100))
        btn_play.draw(screen)
        btn_garage.draw(screen)
        btn_board.draw(screen)
        btn_quit.draw(screen)

    elif state == "GARAGE":
        screen.fill((30, 30, 30))
        txt = font.render(f"CAR COLOR: {settings['car_color'].upper()}", True, (255, 255, 255))
        screen.blit(txt, (WIDTH//2 - 120, 180))
        btn_red.draw(screen); btn_green.draw(screen); btn_blue.draw(screen)
        btn_back.draw(screen)

    elif state == "NAME_INPUT":
        screen.fill((20, 20, 20))
        screen.blit(font.render("TYPE YOUR NAME:", True, (255, 255, 255)), (190, 200))
        name_input.draw(screen)

    elif state == "LEADERBOARD":
        screen.fill((10, 10, 10))
        board = load_leaderboard()
        for i, entry in enumerate(board[:10]):
            txt = font.render(f"{i+1}. {entry['name']} - {entry['score']} PTS", True, (200, 200, 200))
            screen.blit(txt, (160, 100 + i * 35))
        btn_back.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()