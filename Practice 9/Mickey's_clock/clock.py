import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, screen_width, screen_height):
        self.screen_size = (screen_width, screen_height)
        self.center = pygame.math.Vector2(screen_width // 2, screen_height // 2)
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, "images")

        # Фон(Background)
        self.bg = pygame.image.load(os.path.join(img_dir, "clock.png")).convert()
        self.bg = pygame.transform.scale(self.bg, self.screen_size)
        
        # Mikkey
        self.mickey_body = pygame.image.load(os.path.join(img_dir, "mikkey.png")).convert_alpha()
        self.mickey_body = pygame.transform.scale(self.mickey_body, (380, 500)) 
        self.mickey_rect = self.mickey_body.get_rect(center=self.center)
        
        # Right Hand
        self.hand_right = pygame.image.load(os.path.join(img_dir, "hand_right_centered.png")).convert_alpha()
        self.hand_right = pygame.transform.scale(self.hand_right, (200, 300))
        
        # Left hand
        self.hand_left = pygame.image.load(os.path.join(img_dir, "hand_left_centered.png")).convert_alpha()
        self.hand_left = pygame.transform.scale(self.hand_left, (190, 280))

    def blit_rotate_pivot(self, surface, image, pos, originPos, angle):
        image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        offset = pygame.math.Vector2(pos) - image_rect.center
        rotated_offset = offset.rotate(-angle)
        rotated_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
        
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=rotated_center)
        surface.blit(rotated_image, new_rect)

    def render(self, surface):
        surface.blit(self.bg, (0, 0))
        surface.blit(self.mickey_body, self.mickey_rect.topleft)
        
        now = datetime.datetime.now()

        # angles
        sec_angle = -((now.second + now.microsecond / 1_000_000) * 6)
        min_angle = -((now.minute + now.second / 60) * 6)

        
        right_pivot = (100, 220)

       
        left_pivot = (95, 240)

        
        self.blit_rotate_pivot(
            surface,
            self.hand_right,
            self.center,
            right_pivot,
            sec_angle
        )

        
        self.blit_rotate_pivot(
            surface,
            self.hand_left,
            self.center,
            left_pivot,
            min_angle
        )