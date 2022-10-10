from pico2d import *     
running = True
open_canvas(1280,1024)
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
        self.action = 0
    def draw(self):
        self.image.clip_draw(self.frame * 28, 0, 28, 30, 1200, 200)
    
    def update(self):
        self.frame = (self.frame + 1) % 9+1 #방향 전환 프레임: 1
        delay(0.05)

class RedKoopa:
    def __init__(self):
        self.image = load_image('red_koopa.png')
        self.frame  = 1
        self.action = 0
    def draw(self):
        self.image.clip_draw(self.frame * 25, 50 * self.action, 25, 50, 950, 200)
    
    def update(self):
        self.frame = (self.frame + 1) % 17+1 #방향 전환 frame: 1
        delay(0.02)

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



gframe = 0
rframe = 0
grframe = 1

rrframe = 0
raction = 0


rrkoopa = load_image('red_koopa_wake.png')
redkoopa =RedKoopa()
greenkoopa = GreenKoopa()
goomba = GOOMBA()
boss = jr_boss()
while running:
    clear_canvas()
    # jump: character.clip_draw(frame * 50,  action , 50, 75, x, 110)

    # rrkoopa.clip_draw(rrframe * 45, 0, 45, 44, 900, 200)

    boss.draw()
    goomba.draw()
    redkoopa.draw()
    greenkoopa.draw()

    boss.update() 
    goomba.update()
    redkoopa.update()
    greenkoopa.update()

    update_canvas()
    handle_events()

   

    # rrframe =(rframe + 1) % 5
    # grframe =(grframe + 1) % 18
    
    if rframe == 0:
        if raction == 0:
            raction = 1
        else:
            raction = 0

close_canvas()