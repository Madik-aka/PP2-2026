import pygame
from collections import deque
 
 
# ─────────────────────────────────────────
#  PENCIL
# ─────────────────────────────────────────
class PencilTool:
    def __init__(self):
        self.last_pos = None
 
    def on_mouse_down(self, canvas, pos, color, size):
        self.last_pos = pos
        pygame.draw.circle(canvas, color, pos, size // 2)
 
    def on_mouse_move(self, canvas, pos, color, size):
        if self.last_pos:
            pygame.draw.line(canvas, color, self.last_pos, pos, size)
        self.last_pos = pos
 
    def on_mouse_up(self, canvas, pos, color, size):
        self.last_pos = None
 
 
# ─────────────────────────────────────────
#  STRAIGHT LINE
# ─────────────────────────────────────────
class LineTool:
    def __init__(self):
        self.start = None
        self.preview_surface = None
 
    def on_mouse_down(self, canvas, pos, color, size):
        self.start = pos
        self.preview_surface = canvas.copy()
 
    def on_mouse_move(self, canvas, pos, color, size):
        if self.start and self.preview_surface:
            canvas.blit(self.preview_surface, (0, 0))
            pygame.draw.line(canvas, color, self.start, pos, size)
 
    def on_mouse_up(self, canvas, pos, color, size):
        if self.start:
            pygame.draw.line(canvas, color, self.start, pos, size)
        self.start = None
        self.preview_surface = None
 
 
# ─────────────────────────────────────────
#  RECTANGLE
# ─────────────────────────────────────────
class RectTool:
    def __init__(self):
        self.start = None
        self.preview_surface = None
 
    def on_mouse_down(self, canvas, pos, color, size):
        self.start = pos
        self.preview_surface = canvas.copy()
 
    def on_mouse_move(self, canvas, pos, color, size):
        if self.start and self.preview_surface:
            canvas.blit(self.preview_surface, (0, 0))
            rect = _make_rect(self.start, pos)
            pygame.draw.rect(canvas, color, rect, size)
 
    def on_mouse_up(self, canvas, pos, color, size):
        if self.start:
            rect = _make_rect(self.start, pos)
            pygame.draw.rect(canvas, color, rect, size)
        self.start = None
        self.preview_surface = None
 
 
# ─────────────────────────────────────────
#  SQUARE
# ─────────────────────────────────────────
class SquareTool:
    def __init__(self):
        self.start = None
        self.preview_surface = None
 
    def on_mouse_down(self, canvas, pos, color, size):
        self.start = pos
        self.preview_surface = canvas.copy()
 
    def on_mouse_move(self, canvas, pos, color, size):
        if self.start and self.preview_surface:
            canvas.blit(self.preview_surface, (0, 0))
            rect = _make_square(self.start, pos)
            pygame.draw.rect(canvas, color, rect, size)
 
    def on_mouse_up(self, canvas, pos, color, size):
        if self.start:
            rect = _make_square(self.start, pos)
            pygame.draw.rect(canvas, color, rect, size)
        self.start = None
        self.preview_surface = None
 
 
# ─────────────────────────────────────────
#  CIRCLE
# ─────────────────────────────────────────
class CircleTool:
    def __init__(self):
        self.start = None
        self.preview_surface = None
 
    def on_mouse_down(self, canvas, pos, color, size):
        self.start = pos
        self.preview_surface = canvas.copy()
 
    def on_mouse_move(self, canvas, pos, color, size):
        if self.start and self.preview_surface:
            canvas.blit(self.preview_surface, (0, 0))
            cx = (self.start[0] + pos[0]) // 2
            cy = (self.start[1] + pos[1]) // 2
            r = max(abs(pos[0] - self.start[0]), abs(pos[1] - self.start[1])) // 2
            if r > 0:
                pygame.draw.circle(canvas, color, (cx, cy), r, size)
 
    def on_mouse_up(self, canvas, pos, color, size):
        if self.start:
            cx = (self.start[0] + pos[0]) // 2
            cy = (self.start[1] + pos[1]) // 2
            r = max(abs(pos[0] - self.start[0]), abs(pos[1] - self.start[1])) // 2
            if r > 0:
                pygame.draw.circle(canvas, color, (cx, cy), r, size)
        self.start = None
        self.preview_surface = None
 
 
# ─────────────────────────────────────────
#  RIGHT TRIANGLE
# ─────────────────────────────────────────
class RightTriangleTool:
    def __init__(self):
        self.start = None
        self.preview_surface = None
 
    def on_mouse_down(self, canvas, pos, color, size):
        self.start = pos
        self.preview_surface = canvas.copy()
 
    def _points(self, start, end):
        return [start, (start[0], end[1]), end]
 
    def on_mouse_move(self, canvas, pos, color, size):
        if self.start and self.preview_surface:
            canvas.blit(self.preview_surface, (0, 0))
            pygame.draw.polygon(canvas, color, self._points(self.start, pos), size)
 
    def on_mouse_up(self, canvas, pos, color, size):
        if self.start:
            pygame.draw.polygon(canvas, color, self._points(self.start, pos), size)
        self.start = None
        self.preview_surface = None
 
 
# ─────────────────────────────────────────
#  EQUILATERAL TRIANGLE
# ─────────────────────────────────────────
class EqTriangleTool:
    def __init__(self):
        self.start = None
        self.preview_surface = None
 
    def on_mouse_down(self, canvas, pos, color, size):
        self.start = pos
        self.preview_surface = canvas.copy()
 
    def _points(self, start, end):
        import math
        base = abs(end[0] - start[0]) or 1
        cx = (start[0] + end[0]) / 2
        h = base * (3 ** 0.5) / 2
        top_y = start[1] - h
        return [(start[0], start[1]), (end[0], start[1]), (int(cx), int(top_y))]
 
    def on_mouse_move(self, canvas, pos, color, size):
        if self.start and self.preview_surface:
            canvas.blit(self.preview_surface, (0, 0))
            pygame.draw.polygon(canvas, color, self._points(self.start, pos), size)
 
    def on_mouse_up(self, canvas, pos, color, size):
        if self.start:
            pygame.draw.polygon(canvas, color, self._points(self.start, pos), size)
        self.start = None
        self.preview_surface = None
 
 
# ─────────────────────────────────────────
#  RHOMBUS
# ─────────────────────────────────────────
class RhombusTool:
    def __init__(self):
        self.start = None
        self.preview_surface = None
 
    def on_mouse_down(self, canvas, pos, color, size):
        self.start = pos
        self.preview_surface = canvas.copy()
 
    def _points(self, start, end):
        cx = (start[0] + end[0]) // 2
        cy = (start[1] + end[1]) // 2
        return [(cx, start[1]), (end[0], cy), (cx, end[1]), (start[0], cy)]
 
    def on_mouse_move(self, canvas, pos, color, size):
        if self.start and self.preview_surface:
            canvas.blit(self.preview_surface, (0, 0))
            pygame.draw.polygon(canvas, color, self._points(self.start, pos), size)
 
    def on_mouse_up(self, canvas, pos, color, size):
        if self.start:
            pygame.draw.polygon(canvas, color, self._points(self.start, pos), size)
        self.start = None
        self.preview_surface = None
 
 
# ─────────────────────────────────────────
#  ERASER
# ─────────────────────────────────────────
class EraserTool:
    def __init__(self):
        self.last_pos = None
 
    def on_mouse_down(self, canvas, pos, color, size):
        self.last_pos = pos
        pygame.draw.circle(canvas, (255, 255, 255), pos, size * 2)
 
    def on_mouse_move(self, canvas, pos, color, size):
        if self.last_pos:
            pygame.draw.line(canvas, (255, 255, 255), self.last_pos, pos, size * 4)
        self.last_pos = pos
 
    def on_mouse_up(self, canvas, pos, color, size):
        self.last_pos = None
 
 
# ─────────────────────────────────────────
#  FLOOD FILL
# ─────────────────────────────────────────
class FillTool:
    def on_mouse_down(self, canvas, pos, color, size):
        flood_fill(canvas, pos, color)
 
    def on_mouse_move(self, canvas, pos, color, size):
        pass
 
    def on_mouse_up(self, canvas, pos, color, size):
        pass
 
 
def flood_fill(surface, start_pos, fill_color):
    x, y = start_pos
    w, h = surface.get_size()
    if x < 0 or x >= w or y < 0 or y >= h:
        return
 
    target_color = surface.get_at((x, y))[:3]
    fill_rgb = fill_color[:3] if len(fill_color) >= 3 else fill_color
 
    if target_color == tuple(fill_rgb):
        return
 
    queue = deque()
    queue.append((x, y))
    visited = set()
    visited.add((x, y))
 
    while queue:
        cx, cy = queue.popleft()
        if surface.get_at((cx, cy))[:3] != target_color:
            continue
        surface.set_at((cx, cy), fill_color)
        for nx, ny in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                if surface.get_at((nx, ny))[:3] == target_color:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
 
 
# ─────────────────────────────────────────
#  TEXT TOOL
# ─────────────────────────────────────────
class TextTool:
    def __init__(self):
        self.active = False
        self.pos = None
        self.text = ""
        self.font = None
        self.cursor_visible = True
        self.cursor_timer = 0
 
    def get_font(self):
        if self.font is None:
            self.font = pygame.font.SysFont("arial", 24)
        return self.font
 
    def on_mouse_down(self, canvas, pos, color, size):
        self.active = True
        self.pos = pos
        self.text = ""
 
    def on_mouse_move(self, canvas, pos, color, size):
        pass
 
    def on_mouse_up(self, canvas, pos, color, size):
        pass
 
    def on_key(self, event):
        """Returns True if text was committed (Enter), False if cancelled (Escape), None otherwise."""
        if not self.active:
            return None
        if event.key == pygame.K_RETURN:
            self.active = False
            return True
        elif event.key == pygame.K_ESCAPE:
            self.active = False
            self.text = ""
            return False
        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            if event.unicode and event.unicode.isprintable():
                self.text += event.unicode
        return None
 
    def commit(self, canvas, color):
        if self.pos and self.text:
            font = self.get_font()
            surf = font.render(self.text, True, color)
            canvas.blit(surf, self.pos)
 
    def draw_preview(self, screen, canvas_offset, color):
        if not self.active or self.pos is None:
            return
        font = self.get_font()
        display_text = self.text + ("|" if pygame.time.get_ticks() % 1000 < 500 else "")
        surf = font.render(display_text, True, color)
        ox, oy = canvas_offset
        screen.blit(surf, (self.pos[0] + ox, self.pos[1] + oy))
 
 
# ─────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────
def _make_rect(start, end):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    w = abs(end[0] - start[0])
    h = abs(end[1] - start[1])
    return pygame.Rect(x, y, w, h)
 
 
def _make_square(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    side = max(abs(dx), abs(dy))
    x = start[0] if dx >= 0 else start[0] - side
    y = start[1] if dy >= 0 else start[1] - side
    return pygame.Rect(x, y, side, side)