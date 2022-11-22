import random
import math
import BehaviorTree
from pico2d import *
import game_framework
import game_world
TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0/ 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM/ 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

def wander(self):
    self.speed = RUN_SPEED_PPS
    if self.timer <= 0:
        self.timer = 1.0
        self.dir = random.random() *2 *math.pi
        return BehaviorTree.SUCCESS
    else:
        return BehaviorTree.RUNNING






























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
        # self.image.clip_draw(int(self.frame) * 28, 30 * self.action, 28, 30,self.x, self.y)
        self.image.clip_composite_draw(int(self.frame) * 28, 30 * self.action , 28, 30, 0, self.reflect, self.x, self.y, 28, 30)

        pass

class GOOMBA:
    image = None
    def get_name(self):
        return 'monster'
    def edit_x(self, x):
        self.x -= x

    def __init__(self):
        if GOOMBA.image == None:
            GOOMBA.image = load_image('Goomba.png')
        self.frame = 1
        self.action = 1
        self.x = random.randint(0, 1000)
        self.x_dir = 0
        self.y = 55
        self.reflect = ' '
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

    def handle_collision(self, other, group, pos):
        if group == 'fire:goomba':
            try:
                game_world.remove_object(self)
                game_world.remove_object(other)
            except:
                pass
