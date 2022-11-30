import random
import game_framework
from pico2d import *

import game_world

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

JUMP_SPEED_KMPH = 10.0
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)


class WALK:
    def enter(self, event):
        pass

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + ACTION_PER_TIME * self.clip * game_framework.frame_time) % self.clip  # 방향 전환 frame: 1
        if self.frame <= 1:
            self.frame = 2

        self.count_anim = 0

        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        # self.image.clip_draw(int(self.frame) * 25, 50 * self.action, 25, 50, self.x, self.y)
        self.image.clip_composite_draw(int(self.frame) * 25, 50 * self.action, 25, 50, 0, self.reflect, self.x, self.y, 25, 50)

class RedKoopa:
    image = None

    def get_name(self):
        return 'monster'
    def edit_x(self, x):
        self.x -= x

    def __init__(self):
        if RedKoopa.image == None:
            RedKoopa.image = load_image('monster/red_koopa.png')

        self.frame = random.randint(0,15)
        self.x = random.randint(400, 3000)
        self.y = 70

        self.x_dir = -1
        self.action = 1
        self.clip = 17
        self.reflect = ' '
        self.cur_state = WALK
        self.cur_state.enter(self, None)

        self.Y_gravity = 0.25
        self.pre_velocity = 0
        self.y_velocity = 0
        self.jump_height = 0

    def set_pos(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def update(self):

        self.pre_velocity = self.y_velocity
        self.y += self.y_velocity * JUMP_SPEED_PPS * game_framework.frame_time
        self.y_velocity -= self.Y_gravity

        if self.x < 850:
            self.cur_state.do(self)

        if self.x < -1000 or self.y < -1:
            try:
                game_world.remove_object(self)
            except:
                pass

    def get_bb(self):
        return self.x - 15, self.y - 23, self.x + 15, self.y + 23


    def handle_collision(self, other, group, pos):
        if group == 'fire:red':
            try:
                game_world.remove_object(self)
                game_world.remove_object(other)
            except:
                pass
        if group == 'red:empty':
            if pos == 'right':
                self.y += 5
                self.x -= 2

                self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                self.y_velocity = 0
                self.pre_velocity = 0

                self.x_dir = -1
                self.reflect = ' '
                self.Onground = True

            if pos == 'left':
                self.y += 5
                self.x += 2
                self.x_dir = 1
                self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                self.y_velocity = 0
                self.pre_velocity = 0


                self.reflect = 'h'
                self.Onground = True

        if group == 'player:red':
            if pos == 'bottom':
                try:
                    game_world.remove_object(self)
                except:
                    pass

            elif pos == 'left':
                    self.y += 5
                    self.x -= 2
                    self.x_dir = -1
                    self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                    self.y_velocity = 0
                    self.pre_velocity = 0
                    self.reflect = ' '

            elif pos == 'right':
                    self.y += 5
                    self.x += 2
                    self.x_dir = 1
                    self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                    self.y_velocity = 0
                    self.pre_velocity = 0
                    self.reflect = 'h'

        if group == 'red:ground':
            if pos == 'bottom':
                self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                self.y_velocity = 0
                self.pre_velocity = 0

            if pos == 'right':
                self.y += 5
                self.x -= 2
                self.x_dir = -1
                self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                self.y_velocity = 0
                self.pre_velocity = 0
                self.reflect = ' '

            if pos == 'left':
                self.y += 5
                self.x += 2
                self.x_dir = 1
                self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                self.y_velocity = 0
                self.pre_velocity = 0
                self.reflect = 'h'




class GreenKoopa:
    image = None

    def get_name(self):
        return 'monster'

    def edit_x(self, x):
        self.x -= x

    def __init__(self):
        if GreenKoopa.image == None:
            GreenKoopa.image = load_image('monster/green_koopa.png')
        self.frame = random.randint(0, 15)
        self.x = random.randint(400, 3000)
        self.y = 70

        self.x_dir = -1
        self.action = 1
        self.clip = 17
        self.reflect = ' '
        self.cur_state = WALK
        self.cur_state.enter(self, None)

        self.Y_gravity = 0.25
        self.pre_velocity = 0
        self.y_velocity = 0
        self.jump_height = 0



    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        self.pre_velocity = self.y_velocity
        self.y += self.y_velocity * JUMP_SPEED_PPS * game_framework.frame_time
        self.y_velocity -= self.Y_gravity

        if self.x < 850:
            self.cur_state.do(self)
        if self.x < -1000 or self.y < -1:
            try:
                game_world.remove_object(self)
            except:
                pass

    def get_bb(self):
        return self.x - 10, self.y - 23, self.x + 10, self.y + 23

    def set_pos(self,x,y):
        self.x = x
        self.y = y

    def handle_collision(self, other, group, pos):
        if group == 'fire:green':
            try:
                game_world.remove_object(self)
                game_world.remove_object(other)
            except:
                pass

        if group == 'player:green':
            if pos == 'bottom':
                try:
                    game_world.remove_object(self)
                except:
                    pass

            elif pos == 'left':
                self.y += 5
                self.x -= 2
                self.x_dir = -1
                self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                self.y_velocity = 0
                self.pre_velocity = 0
                self.reflect = ' '

            elif pos == 'right':
                self.y += 5
                self.x += 2
                self.x_dir = 1
                self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                self.y_velocity = 0
                self.pre_velocity = 0
                self.reflect = 'h'

        if group == 'green:ground':
                if pos == 'bottom':
                    self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                    self.y_velocity = 0
                    self.pre_velocity = 0

                if pos == 'right':
                    self.y += 5
                    self.x -= 2
                    self.x_dir = -1
                    self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                    self.y_velocity = 0
                    self.pre_velocity = 0
                    self.reflect = ' '

                if pos == 'left':
                    self.y += 5
                    self.x += 2
                    self.x_dir = 1
                    self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                    self.y_velocity = 0
                    self.pre_velocity = 0
                    self.reflect = 'h'


