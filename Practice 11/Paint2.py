import pygame, sys, math

# constants
W, H = 900, 650
TB_W = 150 
TOOLS = [("pencil", "Pencil"), ("rect", "Rect"), ("square", "Square"), 
         ("circle", "Circle"), ("r_tri", "R-Tri"), ("e_tri", "E-Tri"), 
         ("rhombus", "Rhombus"), ("eraser", "Eraser")]
COLORS = [(0,0,0), (220,40,40), (30,120,255), (50,200,80), (255,220,0), (255,255,255)]

# Thickness
SIZES = [("Thin", 2), ("Medium", 7), ("Thick", 20)] 

def get_pts(tool, p1, p2):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    if tool == "r_tri": return [(x1, y1), (x1, y2), (x2, y2)]
    if tool == "rhombus": return [((x1+x2)/2, y1), (x2, (y1+y2)/2), ((x1+x2)/2, y2), (x1, (y1+y2)/2)]
    if tool == "e_tri":
        side = x2 - x1
        h = side * math.sqrt(3) / 2
        return [(x1 + side/2, y2 - h), (x1, y2), (x2, y2)]
    return []

pygame.init()
scr = pygame.display.set_mode((W, H))
canvas = pygame.Surface((W - TB_W, H))
canvas.fill((255, 255, 255))
fnt = pygame.font.SysFont("Arial", 14)

curr_tool, curr_col, curr_sz = "pencil", (0, 0, 0), 7
drawing, start_pos = False, None
last_pos = None # To store the previous point (smooth line)

while True:
    scr.fill((40, 40, 45))
    scr.blit(canvas, (TB_W, 0))
    mx, my = pygame.mouse.get_pos()
    cx, cy = mx - TB_W, my
    
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
        
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if mx < TB_W:
                for i, (t_id, _) in enumerate(TOOLS):
                    if 10 < mx < 140 and 30 + i*32 < my < 58 + i*32: curr_tool = t_id
                for i, col in enumerate(COLORS):
                    if 10 + i*23 < mx < 30 + i*23 and 300 < my < 320: curr_col = col
                for i, (_, val) in enumerate(SIZES):
                    if 10 < mx < 140 and 340 + i*30 < my < 365 + i*30: curr_sz = val
            else:
                drawing = True
                start_pos = (cx, cy)
                last_pos = (cx, cy) # memorizing the beginning of the line
        
        if ev.type == pygame.MOUSEBUTTONUP:
            if drawing and curr_tool not in ["pencil", "eraser"]:
                p2 = (cx, cy)
                if curr_tool == "rect": pygame.draw.rect(canvas, curr_col, (min(start_pos[0], p2[0]), min(start_pos[1], p2[1]), abs(p2[0]-start_pos[0]), abs(p2[1]-start_pos[1])), curr_sz)
                elif curr_tool == "square": 
                    s = min(abs(p2[0]-start_pos[0]), abs(p2[1]-start_pos[1]))
                    pygame.draw.rect(canvas, curr_col, (start_pos[0], start_pos[1], s, s), curr_sz)
                elif curr_tool == "circle":
                    r = int(math.hypot(p2[0]-start_pos[0], p2[1]-start_pos[1]) / 2)
                    pygame.draw.circle(canvas, curr_col, ((start_pos[0]+p2[0])//2, (start_pos[1]+p2[1])//2), r, curr_sz)
                elif curr_tool in ["r_tri", "e_tri", "rhombus"]:
                    pygame.draw.polygon(canvas, curr_col, get_pts(curr_tool, start_pos, p2), curr_sz)
            drawing = False
            last_pos = None

    # Smooth line drawing
    if drawing and curr_tool in ["pencil", "eraser"]:
        col = (255, 255, 255) if curr_tool == "eraser" else curr_col
        if last_pos:
            # connecting the old point to the new one
            pygame.draw.line(canvas, col, last_pos, (cx, cy), curr_sz * 2)
            pygame.draw.circle(canvas, col, (cx, cy), curr_sz) # Сглаживаем углы линии
        last_pos = (cx, cy)

    # Toolbar 
    for i, (t_id, name) in enumerate(TOOLS):
        bg = (80, 140, 255) if curr_tool == t_id else (60, 60, 65)
        pygame.draw.rect(scr, bg, (10, 30 + i*32, 130, 28), border_radius=5)
        scr.blit(fnt.render(name, True, (255, 255, 255)), (20, 35 + i*32))
    
    for i, col in enumerate(COLORS):
        pygame.draw.rect(scr, col, (10 + i*23, 300, 20, 20), border_radius=3)
        if col == curr_col: pygame.draw.rect(scr, (255,255,255), (10 + i*23, 300, 20, 20), 2, border_radius=3)

    scr.blit(fnt.render("Thickness:", True, (200, 200, 200)), (10, 325))
    for i, (label, val) in enumerate(SIZES):
        bg = (255, 160, 0) if curr_sz == val else (60, 60, 65)
        pygame.draw.rect(scr, bg, (10, 340 + i*30, 130, 25), border_radius=5)
        scr.blit(fnt.render(label, True, (255, 255, 255)), (20, 345 + i*30))

    pygame.display.flip() 