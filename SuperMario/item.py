from pico2d import *
import game_framework
import game_world
PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0/ 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM/ 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

JUMP_SPEED_KMPH = 10.0
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

class MUSHROOM:
    image = None
    def get_name(self):
        return 'mushroom'

    def edit_x(self, x):
        self.x -= x
    def __init__(self, x,y):
        if MUSHROOM.image == None:
            MUSHROOM.image = load_image('./item/mushroom.png')
        self.x, self.y = x, y + 25
        self.Y_gravity = 0.25
        self.dir = -1
        self.y_velocity = 0
        self.pre_velcoity = 0

    def draw(self):
        self.image.clip_composite_draw(0, 0, 50, 50, 0, ' ', self.x, self.y-13, 25, 25)
        # self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())
    def update(self):
        self.pre_velcoity = self.y_velocity
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.y_velocity * JUMP_SPEED_PPS * game_framework.frame_time
        self.y_velocity -= self.Y_gravity

    def get_bb(self):
        return self.x-12, self.y-25, self.x+12, self.y

    def handle_collision(self, other, group, pos):
        if group == 'player:mushroom':
            game_world.remove_object(self)
        elif group == 'mushroom:ground' or group == 'mushroom:itemBox' or group =='mushroom:brick':
            if pos == 'bottom':
                self.y -= self.pre_velcoity * JUMP_SPEED_PPS * game_framework.frame_time
                self.pre_velcoity = 0
                self.y_velocity = 0

            if pos == 'right':
                self.y -= self.pre_velcoity * self.Y_gravity * 20 * game_framework.frame_time
                self.pre_velcoity = 0
                self.y_velocity = 0
                self.dir = -1
                self.x -= 10

            if pos == 'left':
                self.y -= self.pre_velcoity * self.Y_gravity * 20 * game_framework.frame_time
                self.pre_velcoity = 0
                self.y_velocity = 0
                self.dir = 1
                self.x += 10



class FLOWER:
    image = None

    def get_name(self):
        return 'flower'

    def edit_x(self, x):
        self.x -= x

    def __init__(self, x, y):
        if FLOWER.image == None:
            FLOWER.image = load_image('./item/flower.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.clip_composite_draw(0, 0, 50, 57, 0, ' ', self.x, self.y - 13, 25, 25 + 7)
        # self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
      pass
    def get_bb(self):
        return self.x - 12, self.y - 24, self.x + 12, self.y

    def handle_collision(self, other, group, pos):
        if group == 'player:flower':
            game_world.remove_object(self)

class STAR:
    image = None
    def get_name(self):
        return 'star'
    def __init__(self, x,y):
        if STAR.image == None:
            STAR.image = load_image('./item/star.png')
        self.x, self.y =x, y
        self.dir = -1

    def draw(self):
        self.image.clip_composite_draw(0, 0, 16, 16, 0, ' ', self.x, self.y-13, 16, 16)
        # self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())
    def update(self):
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
    def get_bb(self):
        return self.x-12, self.y-24, self.x+12, self.y

    def handle_collision(self, other, group, pos):
        if group == 'player:star':
            game_world.remove_object(self)

