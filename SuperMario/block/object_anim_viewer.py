from pico2d import *

class item_block:
    def __init__(self):
        self.image = load_image('block_1.png')
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 40, 330, 90)
    def update(self):
        self.frame = (self.frame+1)%4

class COIN:
    def __init__(self):
        self.image =load_image('coin.png')
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 25 ,0 ,25 ,25 ,400,90)
    def update(self):
        self.frame = (self.frame + 1) % 4

class Bricks:
    def __init__(self):
        self.image = load_image('block_2.png')
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 40, 370, 90)

    def update(self):
        self.frame = (self.frame + 1) % 4

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            running =False

running = True
open_canvas()

frame = 0

coin =load_image('coin.png')
bblock =load_image('block_2.png')
# icblock =load_image('block_1.png')


icblock = item_block()
coin = COIN()
block = Bricks()

while running:
    clear_canvas()

    coin.draw()
    icblock.draw()
    block.draw()

    coin.update()
    icblock.update()
    block.update()
    update_canvas()
    handle_events()
    frame = (frame+1) % 4
    delay(0.1)
close_canvas()