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

JUMP_SPEED_KMPH = 10.0
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

def wander(self):
    self.speed = RUN_SPEED_PPS
    if self.timer <= 0:
        self.timer = 1.0
        self.dir = random.random() *2 *math.pi
        return BehaviorTree.SUCCESS
    else:
        return BehaviorTree.RUNNING

class DIE:
    def enter(self, event):
        self.image = load_image('./monster/goomba_died.png')
        pass

    def exit(self):
        self.Die = False
        pass

    def do(self):

        if self.x <= 850:
            self.frame = (self.frame + ACTION_PER_TIME * 9 * game_framework.frame_time) % 8

        if int(self.frame) == 7:
            try:
                self.Die = False
                game_world.remove_object(self)
            except:
                pass

    def draw(self):
        # self.image.clip_draw(int(self.frame) * 28, 30 * self.action, 28, 30,self.x, self.y)
        self.image.clip_composite_draw(int(self.frame) * 28, 0, 28, 13, 0, self.reflect, self.x, self.y, 28, 13)




        pass

class WALK:
    def enter(self, event):
        self.x_dir = -2
        pass
    def exit(self):
        pass

    def do(self):
        if self.x <= 850:
            self.frame = (self.frame + ACTION_PER_TIME * 9 * game_framework.frame_time) % 9
            if self.frame <= 1:
                self.frame = 2
            self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        pass

    def draw(self):
        # self.image.clip_draw(int(self.frame) * 28, 30 * self.action, 28, 30,self.x, self.y)
        self.image.clip_composite_draw(int(self.frame) * 28, 30 , 28, 30, 0, self.reflect, self.x, self.y, 28, 30)
        pass

class GOOMBA:
    image = None
    stomp_sound = None
    def get_name(self):
        return 'monster'
    def edit_x(self, x):
        self.x -= x

    def __init__(self):
        if GOOMBA.image == None:
            GOOMBA.image = load_image('./monster/Goomba.png')
        if GOOMBA.stomp_sound == None:
            GOOMBA.stomp_sound= load_wav('./music/EnemyStomp.wav')
            GOOMBA.stomp_sound.set_volume(25)

        self.frame = 1
        self.action = 1
        self.x = 0
        self.x_dir = -1
        self.y = 70
        self.reflect = ' '
        self.count_anim = 0
        self.turn = 0

        self.temp = self.x_dir
        self.cur_state = WALK
        self.cur_state.enter(self, None)
        self.Y_gravity = 0.25
        self.pre_velocity = 0
        self.y_velocity = 0
        self.jump_height = 0
        self.die = False
        self.Onground = False

    def draw(self):
        self.cur_state.draw(self)

    def set_pos(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        self.cur_state.do(self)
        self.pre_velocity = self.y_velocity
        self.y += self.y_velocity * JUMP_SPEED_PPS * game_framework.frame_time
        self.y_velocity -= self.Y_gravity

        if self.x < -1000:
            try:
                game_world.remove_object(self)
            except:
                pass
        if self.die:
            self.cur_state = DIE
            self.cur_state.enter(self, None)



    def get_bb(self):
        return self.x - 15, self.y - 16, self.x + 15, self.y + 25
        # return self.x - 10, self.y - 23, self.x + 10, self.y + 16



    def handle_collision(self, other, group, pos):
        if group == 'fire:goomba':
            self.stomp_sound.play()

            try:
                game_world.remove_object(self)
                game_world.remove_object(other)
            except:
                pass
        elif group == 'goomba:ground':
            if pos == 'bottom':

                self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                self.y_velocity = 0
                self.pre_velocity = 0

            if pos == 'right':
                self.x_dir = -1
                self.reflect = ' '
                self.y+=10

            if pos == 'left':
                self.x_dir = 1
                self.reflect = 'h'
                self.y += 10


        elif group == 'goomba:itemBox':
            if pos == 'bottom':

                self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                self.y_velocity = 0
                self.pre_velocity = 0


            if pos == 'right':
                self.x_dir = -1
                self.reflect = ' '

            if pos == 'left':
                self.x_dir = 1
                self.reflect = 'h'

        elif group == 'goomba:bricks':
            if pos == 'bottom':

                self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                self.y_velocity = 0
                self.pre_velocity = 0

            if pos == 'right':
                self.x_dir = -1
                self.reflect = ' '

            if pos == 'left':
                self.x_dir = 1
                self.reflect = 'h'

        elif group == 'player:goomba':
            if pos =='bottom' and not other.die:
                self.stomp_sound.play()
                self.die = True



