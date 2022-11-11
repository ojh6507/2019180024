from pico2d import *
import game_framework
import game_world
PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0/ 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM/ 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

class MUSHROOM:
    image = None
    def get_name(self):
        return 'mushroom'
    def __init__(self, x,y):
        if MUSHROOM.image == None:
            MUSHROOM.image = load_image('mushroom.png')
        self.x, self.y =x, y
        self.dir = -1

    def draw(self):
        self.image.clip_composite_draw(0, 0, 50, 50, 0, ' ', self.x, self.y-13, 25, 25)
        # self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())
    def update(self):
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
    def get_bb(self):
        return self.x-12, self.y-24, self.x+12, self.y

    def handle_collision(self, other, group):
        if group == 'player:mushroom':
            game_world.remove_object(self)

