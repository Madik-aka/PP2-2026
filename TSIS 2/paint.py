import pygame
import sys
from datetime import datetime
from tools import (
    PencilTool, LineTool, RectTool, SquareTool, CircleTool,
    RightTriangleTool, EqTriangleTool, RhombusTool,
    EraserTool, FillTool, TextTool
)
 
# ─────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────
WINDOW_W, WINDOW_H = 1024, 768
TOOLBAR_W = 175
CANVAS_W = WINDOW_W - TOOLBAR_W
CANVAS_H = WINDOW_H 
 
BG_COLOR        = (245, 245, 245)
TOOLBAR_BG      = (30, 30, 40)
TOOLBAR_ACCENT  = (60, 60, 75)
BTN_HOVER       = (80, 80, 100)
BTN_ACTIVE      = (99, 102, 241)   # indigo
WHITE           = (255, 255, 255)
BLACK           = (0, 0, 0)
TEXT_COLOR      = (220, 220, 230)
BORDER_COLOR    = (50, 50, 65)
 
BRUSH_SIZES = [2, 5, 10]
 
PALETTE = [
    (0,   0,   0),    (255, 255, 255),  (192, 192, 192),  (128, 128, 128),
    (255,   0,   0),  (200,   0,   0),  (255, 128,   0),  (255, 200,   0),
    (255, 255,   0),  (128, 255,   0),  (0,   200,   0),  (0,   255, 128),
    (0,   255, 255),  (0,   128, 255),  (0,     0, 255),  (128,   0, 255),
    (255,   0, 255),  (255,   0, 128),  (139,  69,  19),  (255, 182, 193),
]
 
TOOLS = [
    ("Pencil",    PencilTool()),
    ("Line",      LineTool()),
    ("Rect",      RectTool()),
    ("Square",    SquareTool()),
    ("Circle",    CircleTool()),
    ("R.Triangle",RightTriangleTool()),
    ("Eq.Triangle",EqTriangleTool()),
    ("Rhombus",   RhombusTool()),
    ("Eraser",    EraserTool()),
    ("Fill",      FillTool()),
    ("Text",      TextTool()),
]
 
 
# ─────────────────────────────────────────
#  BUTTON HELPER
# ─────────────────────────────────────────
class Button:
    def __init__(self, rect, label, value=None):
        self.rect   = pygame.Rect(rect)
        self.label  = label
        self.value  = value
        self.active = False
        self.hovered= False
 
    def draw(self, surface, font):
        if self.active:
            color = BTN_ACTIVE
        elif self.hovered:
            color = BTN_HOVER
        else:
            color = TOOLBAR_ACCENT
        pygame.draw.rect(surface, color, self.rect, border_radius=6)
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, 1, border_radius=6)
        txt = font.render(self.label, True, TEXT_COLOR)
        tx  = self.rect.centerx - txt.get_width() // 2
        ty  = self.rect.centery - txt.get_height() // 2
        surface.blit(txt, (tx, ty))
 
    def check_hover(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)
 
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
 
 
# ─────────────────────────────────────────
#  MAIN APP
# ─────────────────────────────────────────
def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    pygame.display.set_caption("Paint — TSIS 2")
    clock  = pygame.time.Clock()
 
    font_sm  = pygame.font.SysFont("arial", 11)
    font_med = pygame.font.SysFont("arial", 13, bold=True)
    font_hdr = pygame.font.SysFont("arial", 14, bold=True)
 
    # Canvas
    canvas = pygame.Surface((CANVAS_W, CANVAS_H))
    canvas.fill(WHITE)
    canvas_rect = pygame.Rect(TOOLBAR_W, 0, CANVAS_W, CANVAS_H)
 
    # State
    active_tool_idx  = 0
    active_color     = BLACK
    active_size_idx  = 1          # medium by default
    drawing          = False
 
    # ── Build toolbar buttons ──────────────────
    tool_buttons  = []
    size_buttons  = []
    color_rects   = []
 
    PAD = 8
    bw  = TOOLBAR_W - PAD * 2
    bh  = 24
    x0  = PAD
    HDR = 18   # height reserved for each section header
 
    y = HDR + 4   # space for "TOOLS" header
    # Section: Tools
    for i, (name, _) in enumerate(TOOLS):
        btn = Button((x0, y, bw, bh), name, i)
        tool_buttons.append(btn)
        y += bh + 3
 
    y += HDR + 4   # space for "SIZE" header
    # Section: Brush size
    sw = (bw - 8) // 3
    size_labels = ["S (2px)", "M (5px)", "L (10px)"]
    for i, lbl in enumerate(size_labels):
        btn = Button((x0 + i * (sw + 4), y, sw, bh), lbl, i)
        size_buttons.append(btn)
    y += bh + HDR + 6   # space for "COLOR" header
 
    # Section: Color palette
    cols   = 4
    cs     = (bw - (cols - 1) * 3) // cols   # cell size
    for i, col in enumerate(PALETTE):
        row = i // cols
        c   = i  % cols
        rx  = x0 + c * (cs + 3)
        ry  = y  + row * (cs + 3)
        color_rects.append((pygame.Rect(rx, ry, cs, cs), col))
 
    # Active states
    tool_buttons[active_tool_idx].active = True
    size_buttons[active_size_idx].active = True
 
    # ── Main loop ─────────────────────────────
    while True:
        mouse_pos = pygame.mouse.get_pos()
        # offset mouse to canvas coords
        canvas_mouse = (mouse_pos[0] - TOOLBAR_W, mouse_pos[1])
 
        for btn in tool_buttons + size_buttons:
            btn.check_hover(mouse_pos)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
            # ── Keyboard ─────────────────────
            if event.type == pygame.KEYDOWN:
                # Ctrl+S → save
                if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    save_canvas(canvas)
 
                # Text tool key input
                current_tool = TOOLS[active_tool_idx][1]
                if isinstance(current_tool, TextTool):
                    result = current_tool.on_key(event)
                    if result is True:       # Enter → commit
                        current_tool.commit(canvas, active_color)
                    # result False → cancelled, None → still typing
 
            # ── Mouse Down ───────────────────
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Toolbar click?
                if mouse_pos[0] < TOOLBAR_W:
                    for i, btn in enumerate(tool_buttons):
                        if btn.is_clicked(mouse_pos):
                            for b in tool_buttons:
                                b.active = False
                            btn.active = True
                            active_tool_idx = i
                    for i, btn in enumerate(size_buttons):
                        if btn.is_clicked(mouse_pos):
                            for b in size_buttons:
                                b.active = False
                            btn.active = True
                            active_size_idx = i
                    for rect, col in color_rects:
                        if rect.collidepoint(mouse_pos):
                            active_color = col
                else:
                    # Canvas click
                    drawing = True
                    tool = TOOLS[active_tool_idx][1]
                    tool.on_mouse_down(canvas, canvas_mouse,
                                       active_color, BRUSH_SIZES[active_size_idx])
 
            # ── Mouse Move ───────────────────
            if event.type == pygame.MOUSEMOTION and drawing:
                if mouse_pos[0] >= TOOLBAR_W:
                    tool = TOOLS[active_tool_idx][1]
                    tool.on_mouse_move(canvas, canvas_mouse,
                                       active_color, BRUSH_SIZES[active_size_idx])
 
            # ── Mouse Up ─────────────────────
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if drawing:
                    tool = TOOLS[active_tool_idx][1]
                    tool.on_mouse_up(canvas, canvas_mouse,
                                     active_color, BRUSH_SIZES[active_size_idx])
                drawing = False
 
        # ── Draw ──────────────────────────────
        screen.fill(TOOLBAR_BG)
 
        # Toolbar background
        pygame.draw.rect(screen, TOOLBAR_BG, (0, 0, TOOLBAR_W, WINDOW_H))
 
        # Section headers (fixed positions based on button layout)
        def section_label(text, sy):
            lbl = font_hdr.render(text, True, (160, 160, 180))
            screen.blit(lbl, (PAD, sy))
 
        section_label("TOOLS",  4)
        section_label("SIZE",   tool_buttons[-1].rect.bottom + 4)
        section_label("COLOR",  size_buttons[0].rect.bottom + 4)
 
        # Tool buttons
        for btn in tool_buttons:
            btn.draw(screen, font_sm)
 
        # Size buttons
        for btn in size_buttons:
            btn.draw(screen, font_sm)
 
        # Color palette
        for rect, col in color_rects:
            pygame.draw.rect(screen, col, rect, border_radius=3)
            if col == active_color:
                pygame.draw.rect(screen, WHITE, rect, 2, border_radius=3)
            else:
                pygame.draw.rect(screen, BORDER_COLOR, rect, 1, border_radius=3)
 
        # Active color preview strip — just below the palette
        last_palette_y = color_rects[-1][0].bottom
        strip_y = last_palette_y + 8
        pygame.draw.rect(screen, TOOLBAR_ACCENT,
                         (PAD, strip_y, bw, 34), border_radius=6)
        lbl = font_sm.render("Active color", True, (160, 160, 180))
        screen.blit(lbl, (PAD + 4, strip_y + 2))
        pygame.draw.rect(screen, active_color,
                         (PAD + 4, strip_y + 14, bw - 8, 16), border_radius=4)
        pygame.draw.rect(screen, BORDER_COLOR,
                         (PAD + 4, strip_y + 14, bw - 8, 16), 1, border_radius=4)
 
        # Canvas
        screen.blit(canvas, (TOOLBAR_W, 0))
 
        # Canvas border
        pygame.draw.rect(screen, BORDER_COLOR, canvas_rect, 1)
 
        # Text preview (drawn on screen, not on canvas)
        current_tool = TOOLS[active_tool_idx][1]
        if isinstance(current_tool, TextTool):
            current_tool.draw_preview(screen, (TOOLBAR_W, 0), active_color)
 
        pygame.display.flip()
        clock.tick(60)
 
 
# ─────────────────────────────────────────
#  SAVE
# ─────────────────────────────────────────
def save_canvas(surface):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename  = f"canvas_{timestamp}.png"
    pygame.image.save(surface, filename)
    print(f"[Saved] {filename}")
 
 
if __name__ == "__main__":
    main() 