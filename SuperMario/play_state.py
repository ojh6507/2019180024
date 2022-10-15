from pico2d import *
from character import character

WIDTH, HEIGHT = 800,600
open_canvas(800,600)
player = character.mario()
class background:
    def __init__ (self):
        self.image = load_image('background_2.png')
        self.background_x = 3750
        self.dir = 0
    def draw (self):
        self.image.draw(self.background_x, 500)
    def update(self):
        global  player
        if self.background_x - player.x_dir < 3760 and self.background_x > -2970:
            if player.x > WIDTH//2:
                self.background_x -= player.x_dir*3




        elif self.background_x - player.x_dir > 3760:
            self.background_x = 3760 + player.x_dir
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

    player.draw()
    player.handle_event()
    player.update()
    update_canvas()

close_canvas()