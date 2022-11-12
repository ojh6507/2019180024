import random
from pico2d import *
import game_framework
import game_world

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

class item_block:
    def get_name(self):
        return 'item_block'

    def __init__(self):
        self.image = load_image('block_1.png')
        self.frame = 0
        self.x = 0
        self.y = 100
        self.moveup = False
        self.mario_size = ' '
    def draw(self):
        self.image.clip_draw(int(self.frame) * 30, 0, 30, 40, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

    def update(self):
        self.frame = (self.frame + ACTION_PER_TIME * 4 * game_framework.frame_time) % 4
    def set_pos(self,x,y):
        self.x = x
        self.y = y
    def returnY(self):
        return self.y
    def get_size(self, size):
        self.mario_size = size

    def handle_collision(self, other, group, p):
        global PLAYER
        # print('ball disappear')
        if group == 'player:item_block':
            if p == 'top':
                if self.mario_size == 'Small':
                    print('gen mushroom!!')
                else:
                    print('gen flower!!')



class COIN:
    def get_name(self):
        return 'coin'
    def get_bb(self):
        return self.x - 10, self.y - 10,self.x + 10, self.y + 10


    def __init__(self):
        self.image =load_image('coin.png')
        self.frame = random.randint(0,3)
        self.x = 400
        self.y = 90
    def draw(self):
        self.image.clip_draw(int(self.frame) * 25 ,0 ,25 ,25 ,self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + ACTION_PER_TIME * 4 * game_framework.frame_time) % 4

    def set_pos(self,x,y):
        self.x = x
        self.y = y

    def returnY(self):
        return self.y

    def handle_collision(self, other, group, pos):
        # print('ball disappear')
        if group == 'player:coin':
            game_world.remove_object(self)

class Bricks:
    def get_name(self):
        return 'brick'

    def __init__(self):
        self.image = load_image('block_2.png')
        self.frame = 0
        self.x = 0
        self.y = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 30, 0, 30, 40,self.x,self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + ACTION_PER_TIME * 4 * game_framework.frame_time) % 4

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def returnY(self):
        return self.y

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
    def handle_collision(self, other, group, pos):
        # print('ball disappear')
        if group == 'player:bricks':
           pass


