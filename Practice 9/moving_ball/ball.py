import pygame

class Ball:
    RADIUS = 25
    STEP = 20
    COLOR = (255, 0, 0) # red color

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        # initial position- center
        self.x = screen_width // 2
        self.y = screen_height // 2

    def move(self, direction):
        if direction == "up":
            if self.y - self.STEP >= self.RADIUS:
                self.y -= self.STEP
        elif direction == "down":
            if self.y + self.STEP <= self.screen_height - self.RADIUS:
                self.y += self.STEP
        elif direction == "left":
            if self.x - self.STEP >= self.RADIUS:
                self.x -= self.STEP
        elif direction == "right":
            if self.x + self.STEP <= self.screen_width - self.RADIUS:
                self.x += self.STEP

    def draw(self, screen):
        pygame.draw.circle(screen, self.COLOR, (self.x, self.y), self.RADIUS)

    def get_position(self):
        return (self.x, self.y)