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
graction = 0

goomba = load_image('Goomba.png')
rkoopa = load_image('red_koopa.png')
rrkoopa = load_image('red_koopa_wake.png')
grkoopa = load_image('green_koopa.png')

boss = jr_boss()
while running:
    clear_canvas()
    # jump: character.clip_draw(frame * 50,  action , 50, 75, x, 110)
    goomba.clip_draw(gframe * 28, 0, 28, 30, 1200, 200)
    rkoopa.clip_draw(rframe * 25, 50 * raction, 25, 50, 950, 200)
    rrkoopa.clip_draw(rrframe * 45, 0, 45, 44, 900, 200)

    grkoopa.clip_draw(grframe * 25, 50 * graction, 25, 50, 990, 200)
    boss.draw()
    boss.update()
    update_canvas()
    handle_events()

    gframe = (gframe + 1) % 9+1

    rframe =(rframe + 1) % 18
    rrframe =(rframe + 1) % 5
    
    grframe =(grframe + 1) % 18
    
    if rframe == 0:
        if raction == 0:
            raction = 1
        else:
            raction = 0
   
    if grframe == 0:
        if graction == 0:
            graction = 1
        else:
            graction = 0
   
    delay(0.1)
close_canvas()