import pygame
import db
import config
import game
import os

# Предварительная настройка микшера для стабильного звука
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Snake - PostgreSQL & JSON")
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)

def draw_button(text, rect, color, hover_color, mouse_pos):
    is_hover = rect.collidepoint(mouse_pos)
    pygame.draw.rect(screen, hover_color if is_hover else color, rect)
    text_surf = font.render(text, True, (255, 255, 255))
    screen.blit(text_surf, (rect.x + (rect.width - text_surf.get_width())//2, rect.y + 10))
    return is_hover

def main():
    db.setup_database()
    settings = config.load_settings()
    
    # Автоматическое определение пути к файлу музыки
    base_path = os.path.dirname(os.path.abspath(__file__))
    music_path = os.path.join(base_path, "video-game.wav")
    
    music_loaded = False
    try:
        if os.path.exists(music_path):
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.set_volume(0.5)
            music_loaded = True
            print(f"Music loaded: {music_path}")
        else:
            print(f"Music file NOT FOUND at: {music_path}")
    except pygame.error as e:
        print(f"Pygame error loading music: {e}")

    state = "MENU"
    username = ""
    player_id = None
    last_score, last_level = 0, 0
    personal_best = 0
    music_playing = False

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
            
            if state == "MENU" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif event.key != pygame.K_RETURN and len(username) < 15:
                    username += event.unicode

        screen.fill((20, 20, 20))

        if state == "MENU":
            # Управление музыкой
            if music_loaded and settings.get("sound"):
                if not music_playing:
                    pygame.mixer.music.play(-1)
                    music_playing = True
            else:
                if music_playing:
                    pygame.mixer.music.stop()
                    music_playing = False

            title = font.render("SNAKE GAME", True, (0, 255, 0))
            screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))
            
            prompt = small_font.render("Username: " + username + ("_" if pygame.time.get_ticks() % 1000 < 500 else ""), True, (200, 200, 200))
            screen.blit(prompt, (WIDTH//2 - prompt.get_width()//2, 150))

            btn_play = pygame.Rect(WIDTH//2 - 100, 230, 200, 50)
            btn_lead = pygame.Rect(WIDTH//2 - 125, 300, 250, 50)
            btn_sett = pygame.Rect(WIDTH//2 - 100, 370, 200, 50)
            btn_quit = pygame.Rect(WIDTH//2 - 100, 440, 200, 50)

            if draw_button("Play", btn_play, (50, 150, 50), (80, 200, 80), mouse_pos) and click and username != "":
                if music_playing:
                    pygame.mixer.music.stop()
                    music_playing = False
                player_id = db.get_or_create_player(username)
                personal_best = db.get_personal_best(player_id)
                state = "PLAYING"
            
            if draw_button("Leaderboard", btn_lead, (50, 50, 150), (80, 80, 200), mouse_pos) and click:
                state = "LEADERBOARD"
            
            if draw_button("Settings", btn_sett, (150, 150, 50), (200, 200, 80), mouse_pos) and click:
                state = "SETTINGS"
            
            if draw_button("Quit", btn_quit, (150, 50, 50), (200, 80, 80), mouse_pos) and click:
                running = False

        elif state == "PLAYING":
            last_score, last_level = game.run_game(screen, settings, personal_best)
            if last_score is None:
                running = False
            else:
                db.save_score(player_id, last_score, last_level)
                state = "GAME_OVER"

        elif state == "GAME_OVER":
            go_text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(go_text, (WIDTH//2 - go_text.get_width()//2, 100))
            
            s_text = small_font.render(f"Final Score: {last_score} | Level: {last_level}", True, (255, 255, 255))
            screen.blit(s_text, (WIDTH//2 - s_text.get_width()//2, 200))

            btn_retry = pygame.Rect(WIDTH//2 - 100, 300, 200, 50)
            btn_menu = pygame.Rect(WIDTH//2 - 100, 370, 200, 50)

            if draw_button("REPLAY", btn_retry, (0, 150, 0), (0, 200, 0), mouse_pos) and click:
                personal_best = db.get_personal_best(player_id)
                state = "PLAYING"
            
            if draw_button("MAIN MENU", btn_menu, (100, 100, 100), (150, 150, 150), mouse_pos) and click:
                state = "MENU"

        elif state == "LEADERBOARD":
            title = font.render("TOP 10 SCORES", True, (255, 215, 0))
            screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))
            
            y_offset = 100
            top_scores = db.get_top_10()
            for rank, row in enumerate(top_scores, 1):
                txt = small_font.render(f"{rank}. {row[0]} - Score: {row[1]}", True, (200, 200, 200))
                screen.blit(txt, (WIDTH//2 - txt.get_width()//2, y_offset))
                y_offset += 35
                
            btn_back = pygame.Rect(WIDTH//2 - 100, 500, 200, 50)
            if draw_button("Back", btn_back, (100, 100, 100), (150, 150, 150), mouse_pos) and click:
                state = "MENU"

        elif state == "SETTINGS":
            title = font.render("SETTINGS", True, (255, 255, 255))
            screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))

            current_color = settings.get("snake_color", [0, 255, 0])
            if current_color == [200, 0, 0]: color_name = "Red"
            elif current_color == [0, 255, 0]: color_name = "Green"
            elif current_color == [0, 0, 255]: color_name = "Blue"
            else: color_name = "Custom"
            
            btn_grid = pygame.Rect(WIDTH//2 - 150, 150, 300, 50)
            btn_sound = pygame.Rect(WIDTH//2 - 150, 220, 300, 50)
            btn_color = pygame.Rect(WIDTH//2 - 150, 290, 300, 50)
            btn_back = pygame.Rect(WIDTH//2 - 100, 450, 200, 50)

            if draw_button(f"Grid: {'ON' if settings['grid_overlay'] else 'OFF'}", btn_grid, (70, 70, 70), (100, 100, 100), mouse_pos) and click:
                settings["grid_overlay"] = not settings["grid_overlay"]
                config.save_settings(settings)
            
            if draw_button(f"Sound: {'ON' if settings['sound'] else 'OFF'}", btn_sound, (70, 70, 70), (100, 100, 100), mouse_pos) and click:
                settings["sound"] = not settings["sound"]
                config.save_settings(settings)

            if draw_button(f"Snake Color: {color_name}", btn_color, tuple(current_color), (150, 150, 150), mouse_pos) and click:
                if current_color == [0, 255, 0]: settings["snake_color"] = [0, 0, 255] # Green -> Blue
                elif current_color == [0, 0, 255]: settings["snake_color"] = [200, 0, 0] # Blue -> Red
                else: settings["snake_color"] = [0, 255, 0] # Red -> Green
                config.save_settings(settings)

            if draw_button("Back", btn_back, (100, 100, 100), (150, 150, 150), mouse_pos) and click:
                state = "MENU"

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main() 