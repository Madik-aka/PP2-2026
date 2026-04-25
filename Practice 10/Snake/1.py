import pygame
import random
import sys
import os

#Настройка звука 
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

try:
    pygame.mixer.init()
    print("Звук работает")
except Exception as e:
    print("Ошибка звука:", e)

# путь к файлу
base_dir = os.path.dirname(os.path.abspath(__file__))

def get_sound(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        print(f"Файл не найден: {path}")
        return None
    try:
        sound = pygame.mixer.Sound(path)
        sound.set_volume(1.0)
        print(f"Загружен звук: {filename}")
        return sound
    except Exception as e:
        print(f"Ошибка загрузки {filename}: {e}")
        return None

eat_sound = get_sound("snake-game-food.wav")
death_sound = get_sound("snake-death-scream.wav")

# --- ОКНО ---
CELL_SIZE = 20 
COLS, ROWS = 30, 20
HUD_HEIGHT = 60
WIDTH = CELL_SIZE * COLS
HEIGHT = CELL_SIZE * ROWS + HUD_HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake (Fixed Sound)")
clock = pygame.time.Clock()

# --- ЦВЕТА ---
BLACK = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (255, 60, 60)
GREEN = (40, 255, 40)
DARK_GREEN = (0, 150, 0)
GRAY = (50, 50, 50)
GOLD = (255, 215, 0)

# --- ШРИФТЫ ---
font_small = pygame.font.SysFont("Arial", 22, bold=True)
font_big = pygame.font.SysFont("Arial", 40, bold=True)

# --- КЛАССЫ ---
class Snake:
    def __init__(self):
        self.body = [(COLS // 2, ROWS // 2)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.grow = False

    def move(self):
        self.direction = self.next_direction
        x, y = self.body[0]
        new_head = (x + self.direction[0], y + self.direction[1])
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self):
        for i, (x, y) in enumerate(self.body):
            color = DARK_GREEN if i == 0 else GREEN
            rect = (x * CELL_SIZE + 1, y * CELL_SIZE + HUD_HEIGHT + 1, CELL_SIZE - 2, CELL_SIZE - 2)
            pygame.draw.rect(screen, color, rect)

class Food:
    def __init__(self, snake_body):
        self.pos = self.spawn(snake_body)

    def spawn(self, snake_body):
        while True:
            p = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
            if p not in snake_body:
                return p

    def draw(self):
        x, y = self.pos
        center = (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + HUD_HEIGHT + CELL_SIZE // 2)
        pygame.draw.circle(screen, RED, center, CELL_SIZE // 2 - 2)

# --- game ---
def run_game():
    snake = Snake()
    food = Food(snake.body)
    score = 0
    level = 1
    active = True
    death_played = False

    while True:
        clock.tick(7 + level * 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_UP and snake.direction != (0, 1):
                        snake.next_direction = (0, -1)
                    elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                        snake.next_direction = (0, 1)
                    elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                        snake.next_direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                        snake.next_direction = (1, 0)
                else:
                    if event.key == pygame.K_r:
                        run_game()
                        return
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

        if active:
            snake.move()
            x, y = snake.body[0]

            # Столкновение
            if x < 0 or x >= COLS or y < 0 or y >= ROWS or (x, y) in snake.body[1:]:
                active = False
                if death_sound and not death_played:
                    death_sound.play()
                    death_played = True

            # Еда
            if active and snake.body[0] == food.pos:
                snake.grow = True
                score += 10
                if eat_sound:
                    eat_sound.play()
                food = Food(snake.body)

                if score % 30 == 0:
                    level += 1

        # --- РЕНДЕР ---
        screen.fill(BLACK)
        pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, HUD_HEIGHT))

        score_text = font_small.render(f"SCORE: {score}", True, WHITE)
        level_text = font_small.render(f"LEVEL: {level}", True, GOLD)

        screen.blit(score_text, (20, 15))
        screen.blit(level_text, (WIDTH - 140, 15))

        food.draw()
        snake.draw()

        if not active:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            msg = font_big.render("GAME OVER", True, RED)
            hint = font_small.render("R - Restart | Q - Quit", True, WHITE)

            screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 40))
            screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT // 2 + 20))

        pygame.display.flip()

if __name__ == "__main__":
    run_game()                  










