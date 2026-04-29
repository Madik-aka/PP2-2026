import pygame, random, sys

# -------- Settings --------
W, H = 480, 700
ROAD = (80, 400)
SPD_STEP, SPD_INC = 5, 0.5

COLORS = {
    "BLUE": (30,120,255),
    "RED": (220,40,40),
    "GOLD": (255,220,0),
    "SILVER": (192,192,192)
}

COINS = [
    ("BRONZE", 1, (180,100,30), 60),
    ("SILVER", 2, COLORS["SILVER"], 30),      #Different coins 
    ("GOLD", 3, COLORS["GOLD"], 10)
]

pygame.init()
scr = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
fnt = pygame.font.SysFont("arial", 22, True)
big_fnt = pygame.font.SysFont("arial", 40, True)


class Car:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 40, 70)
        self.color = color

    def draw(self, surf):
        # Body of machine
        pygame.draw.rect(surf, self.color, self.rect, border_radius=8)

        # стекла
        pygame.draw.rect(surf, (180,220,255), (self.rect.x+6, self.rect.y+8, 28,16), border_radius=4)
        pygame.draw.rect(surf, (180,220,255), (self.rect.x+6, self.rect.y+46, 28,14), border_radius=4)

        # фары
        pygame.draw.circle(surf, (255,255,200), (self.rect.x+10, self.rect.y+5), 4)
        pygame.draw.circle(surf, (255,255,200), (self.rect.x+30, self.rect.y+5), 4)

        # stop signal
        pygame.draw.circle(surf, (255,50,50), (self.rect.x+10, self.rect.y+65), 4)
        pygame.draw.circle(surf, (255,50,50), (self.rect.x+30, self.rect.y+65), 4)

        # wheels
        for dx, dy in [(-5,10), (35,10), (-5,48), (35,48)]:
            pygame.draw.rect(surf, (20,20,20), (self.rect.x+dx, self.rect.y+dy, 10,14), border_radius=3)

class Player(Car):
    def move(self, keys, speed):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > ROAD[0]:
            self.rect.x -= speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < ROAD[1]:
            self.rect.x += speed

class Coin:
    def __init__(self, speed, x):
        self.type = random.choices(COINS, weights=[c[3] for c in COINS])[0]
        self.val, self.color = self.type[1], self.type[2]
        self.rect = pygame.Rect(x, -30, 24, 24)
        self.speed = speed

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, self.rect.center, 12)
        pygame.draw.circle(surf, (0,0,0), self.rect.center, 12, 2)
        txt = pygame.font.SysFont("arial", 12, True).render(str(self.val), True, (0,0,0))
        surf.blit(txt, txt.get_rect(center=self.rect.center))

# -------- checking the position --------
def is_position_free(x, objects, min_dist=60):
    for obj in objects:
        if abs(obj.rect.x - x) < min_dist:
            return False
    return True

# -------- reset --------
def reset_game():
    return Player(W//2-20, H-90, COLORS["BLUE"]), [], [], 0, 0, 3.0, 0, 0

player, enemies, coins, score, total_c, speed, frame, line_offset = reset_game()
game_over = False

# -------- main cycle--------
while True:
    scr.fill((50, 200, 80)) 

    # road 
    pygame.draw.rect(scr, (50,50,50), (ROAD[0], 0, ROAD[1]-ROAD[0], H))

    if not game_over:
        line_offset += speed
        if line_offset > 40:
            line_offset = 0

        for y in range(-40, H, 40):
            pygame.draw.rect(scr, (255,255,255),
                             ((ROAD[0]+ROAD[1])//2 - 5, y + line_offset, 10, 20))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over and ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_r:
                player, enemies, coins, score, total_c, speed, frame, line_offset = reset_game()
                game_over = False
            if ev.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    if not game_over:
        frame += 1
        keys = pygame.key.get_pressed()
        player.move(keys, 5)

        # ---- spawn of enemy ----
        if frame % 90 == 0:
            for _ in range(10):
                x = random.randint(ROAD[0], ROAD[1]-40)
                if is_position_free(x, enemies + coins):
                    enemies.append(Car(x, -70, COLORS["RED"]))
                    break

        # ---- spawn of coins----
        if frame % 60 == 0:
            for _ in range(10):
                x = random.randint(ROAD[0], ROAD[1]-24)
                if is_position_free(x, enemies + coins):
                    coins.append(Coin(speed, x))
                    break

        # ---- enemy ----
        for e in enemies[:]:
            e.rect.y += speed
            e.draw(scr)
            if e.rect.colliderect(player.rect):
                game_over = True
            if e.rect.top > H:
                enemies.remove(e)

        # ---- coins ----
        for c in coins[:]:
            c.rect.y += speed
            c.draw(scr)
            if c.rect.colliderect(player.rect):
                score += c.val
                total_c += 1
                coins.remove(c)
                if total_c % SPD_STEP == 0:
                    speed += SPD_INC
            elif c.rect.top > H:
                coins.remove(c)

        player.draw(scr)

        scr.blit(fnt.render(f"Score: {score}  Coins: {total_c}", True, COLORS["GOLD"]), (10, 10))

    else:
        scr.blit(big_fnt.render("GAME OVER", True, (255,0,0)), (110, 250))
        scr.blit(fnt.render("Press R to Restart", True, (255,255,255)), (130, 320))
        scr.blit(fnt.render("Press Q to Quit", True, (255,255,255)), (140, 360))

    pygame.display.flip()
    clock.tick(60) 