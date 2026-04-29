import pygame

class Button:
    def __init__(self, x, y, w, h, text, color=(200, 200, 200), hover_color=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover_color = hover_color or tuple(max(0, c - 50) for c in color)
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        col = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(surface, col, self.rect, border_radius=8)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2, border_radius=8)
        txt = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(txt, txt.get_rect(center=self.rect.center))

    def is_clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and
                event.button == 1 and
                self.rect.collidepoint(event.pos))


class TextInput:
    def __init__(self, x, y, w, h, placeholder=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = ""
        self.placeholder = placeholder
        self.font = pygame.font.Font(None, 36)
        self.active = True

    def handle_event(self, event):
        """Returns the entered text when Enter is pressed, else None."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.text.strip():
                return self.text.strip()
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isprintable() and len(self.text) < 15:
                self.text += event.unicode
        return None

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect, border_radius=6)
        pygame.draw.rect(surface, (0, 200, 255), self.rect, 2, border_radius=6)
        display = self.text if self.text else self.placeholder
        color = (0, 0, 0) if self.text else (150, 150, 150)
        txt = self.font.render(display, True, color)
        surface.blit(txt, (self.rect.x + 10, self.rect.y + 8))