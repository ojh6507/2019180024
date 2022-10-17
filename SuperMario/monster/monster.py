import random
from pico2d import *

class jr_boss:
    def __init__(self):
        self.image = load_image('jr_koopa.png')
        self.frame  = 0
    def draw(self):
        self.image.clip_draw(self.frame * 50, 60, 50, 70, 900, 200)

    def update(self):
        self.frame = (self.frame + 1) % 19

class GOOMBA:
    def __init__(self):
        self.image = load_image('Goomba.png')
        self.frame  = 1
        self.action = 1
        self.x = random.randint(0, 800)
        self.x_dir = 0
        self.y = 85
        self.count_anim = 0
        self.turn = 0
    def draw(self):
        self.image.clip_draw(self.frame * 28, 30 * self.action, 28, 30,self.x, self.y)
    
    def update(self):
        self.count_anim += 1

        if self.count_anim == 3:
            self.frame = (self.frame + 1) % 9 + 1 #방향 전환 프레임: 1
            self.count_anim = 0

        self.x += self.x_dir * 1.5
        self.Goomba_right()

    def Goomba_right(self):
        self.action = 0
        self.x_dir = 1
    def Goomba_left(self):
        self.action = 1
        self.x_dir = -1
    def Gommba_turn(self):
        self.frame = 18
class RedKoopa:
    def __init__(self):
        self.image = load_image('red_koopa.png')
        self.frame  = 1
        self.action = 0
    def draw(self):
        self.image.clip_draw(self.frame * 25, 50 * self.action, 25, 50, 950, 200)
    
    def update(self):
        self.frame = (self.frame + 1) % 17+1 #방향 전환 frame: 1
class GreenKoopa:
    def __init__(self):
        self.image = load_image('green_koopa.png')
        self.frame  = 1
        self.action = 0
    def draw(self):
        self.image.clip_draw(self.frame * 25, 50 * self.action, 25, 50, 850, 200)

    def update(self):
        self.frame = (self.frame + 1) % 17+1 #방향 전환 frame: 1
        delay(0.02)

def handle_events():

    events = get_events()
    global running
    for event in events:
        if event.type== SDL_QUIT:
            running = False
