import pygame
import random
import sys
import os

pygame.init()
pygame.mixer.init()

BASE_DIR = os.path.dirname(__file__)

# --- SOUNDS ---
coin_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "coin-sound.wav"))
crash_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "car-crash.wav"))

pygame.mixer.music.load(os.path.join(BASE_DIR, "chill-music.wav"))
pygame.mixer.music.play(-1)
 
# --- SCREEN ---
SCREEN_W, SCREEN_H = 400, 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()

ROAD_LEFT = 60
ROAD_RIGHT = 340

WHITE = (255,255,255)
GRAY = (90,90,90)
RED = (220,40,40)
BLUE = (40,90,220)
YELLOW = (255,215,0)
GRASS = (40,120,40)

font = pygame.font.SysFont("Arial", 22, True)
big = pygame.font.SysFont("Arial", 48, True)


# =========================
#CAR DESIGN
# =========================
def draw_car(surface, x, y, color):
    # shadow
    pygame.draw.ellipse(surface, (0,0,0,60), (x+5, y+60, 30, 10))

    # body
    pygame.draw.rect(surface, color, (x, y, 40, 70), border_radius=10)

    # windshield
    pygame.draw.polygon(surface, (180,220,255), [
        (x+6, y+10),
        (x+34, y+10),
        (x+30, y+30),
        (x+10, y+30)
    ])

    # roof highlight
    pygame.draw.rect(surface, (255,255,255), (x+10, y+12, 20, 6), border_radius=3)

    # headlights
    pygame.draw.circle(surface, (255,255,180), (x+10, y+5), 4)
    pygame.draw.circle(surface, (255,255,180), (x+30, y+5), 4)

    # wheels
    pygame.draw.rect(surface, (20,20,20), (x-3, y+12, 6, 18), border_radius=2)
    pygame.draw.rect(surface, (20,20,20), (x+37, y+12, 6, 18), border_radius=2)
    pygame.draw.rect(surface, (20,20,20), (x-3, y+45, 6, 18), border_radius=2)
    pygame.draw.rect(surface, (20,20,20), (x+37, y+45, 6, 18), border_radius=2)


# =========================
# PLAYER
# =========================
class Player:
    def __init__(self):
        self.x = SCREEN_W//2 - 20
        self.y = SCREEN_H - 110
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > ROAD_LEFT:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + 40 < ROAD_RIGHT:
            self.x += self.speed

    def draw(self):
        draw_car(screen, self.x, self.y, BLUE)

    def rect(self):
        return pygame.Rect(self.x, self.y, 40, 70)


# =========================
# ENEMY
# =========================
class Enemy:
    def __init__(self, speed):
        self.x = random.randint(ROAD_LEFT, ROAD_RIGHT - 40)
        self.y = -80
        self.speed = speed

    def update(self):
        self.y += self.speed

    def draw(self):
        draw_car(screen, self.x, self.y, RED)

    def rect(self):
        return pygame.Rect(self.x, self.y, 40, 70)


# =========================
# COIN
# =========================
class Coin:
    def __init__(self, speed):
        self.x = random.randint(ROAD_LEFT+10, ROAD_RIGHT-10)
        self.y = -20
        self.speed = speed

    def update(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), 10)

    def rect(self):
        return pygame.Rect(self.x-10, self.y-10, 20, 20)


# =========================
# ROAD
# =========================
offset = 0
def draw_road():
    global offset
    screen.fill(GRASS)
    pygame.draw.rect(screen, GRAY, (ROAD_LEFT,0,ROAD_RIGHT-ROAD_LEFT,SCREEN_H))

    offset = (offset + 6) % 80
    for i in range(-1, SCREEN_H//80 + 2):
        y = i*80 + offset
        pygame.draw.rect(screen, WHITE, (SCREEN_W//2-2, y, 4, 40))


# =========================
# GAME
# =========================
def main():
    player = Player()
    enemies = []
    coins = []

    score = 0
    money = 0
    base_speed = 4

    game_over = False
    spawn_timer = 0

    while True:
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN and game_over:
                if e.key == pygame.K_r:
                    main()
                    return
                if e.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()

        if not game_over:
            player.move(keys)

            speed = base_speed + score * 0.15

            spawn_timer += 1
            if spawn_timer > 50:
                if len(enemies) < 6:
                    enemies.append(Enemy(speed))
                if random.random() < 0.5:
                    coins.append(Coin(speed))
                spawn_timer = 0

            # ENEMY COLLISION
            for en in enemies[:]:
                en.update()

                if en.y > SCREEN_H:
                    enemies.remove(en)
                    score += 1

                elif en.rect().colliderect(player.rect()):
                    #STOP MUSIC + CRASH SOUND
                    pygame.mixer.music.stop()
                    crash_sound.play()
                    game_over = True

            # COINS
            for c in coins[:]:
                c.update()

                if c.y > SCREEN_H:
                    coins.remove(c)

                elif c.rect().colliderect(player.rect()):
                    coin_sound.play()
                    coins.remove(c)
                    money += 1

        draw_road()

        for en in enemies:
            en.draw()
        for c in coins:
            c.draw()
        player.draw()

        screen.blit(font.render(f"Score: {score}", True, WHITE), (10,10))
        screen.blit(font.render(f"Coins: {money}", True, YELLOW), (250,10))

        if game_over:
            screen.blit(big.render("GAME OVER", True, RED), (80,250))
            screen.blit(font.render("R - restart | Q - quit", True, WHITE), (70,320))

        pygame.display.flip()


if __name__ == "__main__":
    main()