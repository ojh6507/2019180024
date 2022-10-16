from pico2d import *
from character import character
from block import block
WIDTH, HEIGHT = 800,600
open_canvas(800,600)
player = character.mario()

brick_block = block.Bricks()
coin = block.COIN()
item = block.item_block()

class background:
    def __init__ (self):
        self.image = load_image('background_2.png')
        self.background_x = 3750
        self.dir = 0
    def draw (self):
        self.image.draw(self.background_x, 500)
    def update(self):
        global  player
        # 키 눌렀을 때 변화율 만큼 움직이기
        if self.background_x < (-2950):
            if player.x - 400 < 0:
                self.background_x -= (player.x - 400)
                player.x = 400
            pass
        elif  player.x - 400 > 0:
                self.background_x -= (player.x - 400)
                player.x = 400
        elif player.x - 400 < 0:
            if  self.background_x - (player.x - 400) < 3750:
                self.background_x -= (player.x - 400)
                player.x = 400

    def handle_event(self):
        global running
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False


world = background()
running = True
while(running):

    clear_canvas()
    world.draw()
    world.update()

    coin.draw()
    player.draw()
    player.handle_event()
    player.update()
    update_canvas()

close_canvas()