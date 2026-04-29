import pygame
import random
import sys

CELL, COLS, ROWS = 20, 30, 28
SCREEN_W, SCREEN_H = COLS * CELL, ROWS * CELL + 50
HUD_H, FPS = 50, 10

UP, DOWN, LEFT, RIGHT = (0,-1),(0,1),(-1,0),(1,0)

BLACK=(0,0,0); WHITE=(255,255,255)
BG=(30,30,30); GRID_LINE=(45,45,45)
SNAKE_HEAD=(0,210,80); SNAKE_BODY=(0,160,60)
RED=(220,50,50); ORANGE=(255,140,0); PURPLE=(180,60,200)
YELLOW=(255,220,0)

FOOD_TYPES = [
    {"label":"Apple","value":1,"colour":RED,"weight":50,"lifetime":None},
    {"label":"Orange","value":2,"colour":ORANGE,"weight":30,"lifetime":50},
    {"label":"Grape","value":3,"colour":PURPLE,"weight":15,"lifetime":30},
]

MAX_FOOD_ON_SCREEN = 4

def weighted_choice(items):
    total=sum(i["weight"] for i in items)
    r=random.randint(1,total)
    s=0
    for i in items:
        s+=i["weight"]
        if r<=s: return i

class Food:
    def __init__(self, occupied):
        f=weighted_choice(FOOD_TYPES)
        self.value=f["value"]; self.color=f["colour"]
        self.lifetime=f["lifetime"]; self.age=0

        free=[(c,r) for c in range(COLS) for r in range(ROWS)
              if (c,r) not in occupied]
        self.pos=random.choice(free)

    def update(self):
        if self.lifetime:
            self.age+=1
            return self.age>=self.lifetime
        return False

    def draw(self, s):
        x,y=self.pos
        px=x*CELL+CELL//2
        py=y*CELL+CELL//2+HUD_H
        pygame.draw.circle(s,self.color,(px,py),CELL//2-2)
        txt=pygame.font.SysFont("arial",11,True).render(str(self.value),True,WHITE)
        s.blit(txt,txt.get_rect(center=(px,py)))

class Snake:
    def __init__(self):
        m=(COLS//2,ROWS//2)
        self.body=[(m[0]-i,m[1]) for i in range(3)]
        self.dir=RIGHT; self.grow=False

    def move(self):
        h=self.body[0]
        nh=(h[0]+self.dir[0],h[1]+self.dir[1])
        self.body.insert(0,nh) # add new head 
        if not self.grow: self.body.pop()
        else: self.grow=False

    def change(self,d):
        if (d[0]*-1,d[1]*-1)!=self.dir:
            self.dir=d

    def dead(self):
        h=self.body[0]
        return not(0<=h[0]<COLS and 0<=h[1]<ROWS) or h in self.body[1:]

class Game:
    def __init__(self):
        pygame.init()
        self.s=pygame.display.set_mode((SCREEN_W,SCREEN_H))
        self.c=pygame.time.Clock()
        self.f=pygame.font.SysFont("arial",22,True)
        self.big=pygame.font.SysFont("arial",40,True)
        self.reset()

    def reset(self):
        self.sn=Snake()
        self.food=[]
        self.score=0
        self.frame=0
        self.over=False
        self.run=True

    def loop(self):
        while self.run:
            self.c.tick(FPS)

            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    self.run=False

                if e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_UP: self.sn.change(UP)
                    elif e.key==pygame.K_DOWN: self.sn.change(DOWN)
                    elif e.key==pygame.K_LEFT: self.sn.change(LEFT)
                    elif e.key==pygame.K_RIGHT: self.sn.change(RIGHT)

                    elif self.over and e.key==pygame.K_r:
                        self.reset()

                    elif self.over and e.key==pygame.K_q:
                        self.run=False

            if not self.over:
                self.frame+=1
                self.sn.move()

                if self.sn.dead():
                    self.over=True

                for f in self.food[:]:
                    if f.pos==self.sn.body[0]:
                        self.score+=f.value
                        self.sn.grow=True
                        self.food.remove(f)

                for f in self.food[:]:
                    if f.update():
                        self.food.remove(f)

                if self.frame%25==0 and len(self.food)<MAX_FOOD_ON_SCREEN:
                    occ=set(self.sn.body)|{f.pos for f in self.food}
                    self.food.append(Food(occ))

            self.draw()

        pygame.quit()
        sys.exit()

    def draw(self):
        self.s.fill(BG)

        for c in range(COLS):
            for r in range(ROWS):
                pygame.draw.rect(self.s,GRID_LINE,(c*CELL,r*CELL+HUD_H,CELL,CELL),1)

        for f in self.food:
            f.draw(self.s)

        for i,(c,r) in enumerate(self.sn.body):
            col=SNAKE_HEAD if i==0 else SNAKE_BODY
            pygame.draw.rect(self.s,col,(c*CELL+1,r*CELL+HUD_H+1,CELL-2,CELL-2))

        # HUD
        pygame.draw.rect(self.s,(20,20,20),(0,0,SCREEN_W,HUD_H))
        self.s.blit(self.f.render(f"Score: {self.score}",True,YELLOW),(10,10))

        
        margin = 10
        y = 10
        for f in FOOD_TYPES:
            text = f"{f['label']} +{f['value']}"
            txt = self.f.render(text, True, f["colour"])
            x = SCREEN_W - txt.get_width() - margin
            self.s.blit(txt, (x, y))
            y += 18

        if self.over:
            self.s.blit(self.big.render("GAME OVER",True,RED),(130,250))
            self.s.blit(self.f.render("R - Restart",True,WHITE),(170,320))
            self.s.blit(self.f.render("Q - Exit",True,WHITE),(185,360))

        pygame.display.flip()

if __name__=="__main__":
    Game().loop() 