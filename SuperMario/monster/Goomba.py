import random
from pico2d import *
import game_framework
TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0/ 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM/ 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER


class WALK:
    def enter(self, event):
        self.x_dir = -2
        pass

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + ACTION_PER_TIME * 9 * game_framework.frame_time) % 9
        if self.frame <= 1:
            self.frame = 2

        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        pass

    def draw(self):
        self.image.clip_draw(int(self.frame) * 28, 30 * self.action, 28, 30,self.x, self.y)

        pass

class GOOMBA:
    image = None

    def get_name(self):
        return 'monster'

    def __init__(self):
        if GOOMBA.image == None:
            GOOMBA.image = load_image('Goomba.png')
        self.frame = 1
        self.action = 1
        self.x = random.randint(0, 1000)
        self.x_dir = 0
        self.y = 85
        self.count_anim = 0
        self.turn = 0

        self.cur_state = WALK
        self.cur_state.enter(self, None)


    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.cur_state.do(self)

    def get_bb(self):
        return self.x - 10, self.y - 11, self.x + 10, self.y + 11


