import pygame
import os
from player import MusicPlayer

# Color for design
BG_COLOR = (18, 18, 18)        # Глубокий чёрный
ACCENT_COLOR = (0, 255, 127)   # Ярко-зелёный (неон)
TEXT_COLOR = (240, 240, 240)   # Почти белый
UI_PANEL = (33, 33, 33)        # Серые блоки

# Настройка путей
current_dir = os.path.dirname(os.path.abspath(__file__))
music_path = os.path.join(current_dir, "music")


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Premium Music Player")

# Шрифты 
title_font = pygame.font.SysFont("Segoe UI", 32, bold=True)
main_font = pygame.font.SysFont("Segoe UI", 24)
small_font = pygame.font.SysFont("Consolas", 18)

my_player = MusicPlayer(music_path)

running = True
while running:
    screen.fill(BG_COLOR)
    
    # 1. top panel for track name
    pygame.draw.rect(screen, UI_PANEL, (0, 0, 600, 100))
    pygame.draw.line(screen, ACCENT_COLOR, (0, 100), (600, 100), 3)

    # 2. text of the current track
    title_text = title_font.render("NOW PLAYING", True, ACCENT_COLOR)
    screen.blit(title_text, (30, 20))
    
    track_name = my_player.get_current_track_name()
    track_surf = main_font.render(track_name, True, TEXT_COLOR)
    screen.blit(track_surf, (30, 60))
    
    # 3. Player status(play or stop)
    status = "STATUS: PLAYING" if my_player.is_playing else "STATUS: STOPPED / PAUSED"
    status_color = ACCENT_COLOR if my_player.is_playing else (255, 80, 80)
    status_surf = small_font.render(status, True, status_color)
    screen.blit(status_surf, (30, 120))

    # 4.Control Panel
    pygame.draw.rect(screen, UI_PANEL, (30, 170, 540, 230), border_radius=10)
    
    controls = [
        ("P", "PLAY / PAUSE"),
        ("S", "STOP PLAYBACK"),
        ("N", "NEXT TRACK"),
        ("B", "PREVIOUS TRACK"),
        ("Q", "QUIT PLAYER")
    ]
    
    for i, (key, desc) in enumerate(controls):
        key_text = small_font.render(f"[{key}]", True, ACCENT_COLOR)
        desc_text = small_font.render(f" - {desc}", True, TEXT_COLOR)
        screen.blit(key_text, (50, 200 + i * 40))
        screen.blit(desc_text, (90, 200 + i * 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_p:
                if pygame.mixer.music.get_pos() == -1:
                    my_player.play()
                else:
                    my_player.pause_unpause()
            elif event.key == pygame.K_s:
                my_player.stop()
            elif event.key == pygame.K_n:
                my_player.next_track()
            elif event.key == pygame.K_b:
                my_player.prev_track()

    pygame.display.flip()

pygame.quit() 