import random

from pico2d import *

class item_block:
    def __init__(self):
        self.image = load_image('block_1.png')
        self.frame = 0
        self.x = 0
        self.y = 200
        self.count_anim = 0
    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 40, self.x, self.y)
    def update(self):
        self.count_anim += 1
        if self.count_anim == 4:
            self.frame = (self.frame+1)%4
            self.count_anim = 0
    def set_pos(self,x,y):
        self.x = x
        self.y = y


class COIN:
    def __init__(self):
        self.image =load_image('coin.png')
        self.frame = random.randint(0,3)
        self.count_anim = 0
        self.x = 400
        self.y = 90
    def draw(self):
        self.image.clip_draw(self.frame * 25 ,0 ,25 ,25 ,self.x, self.y)

    def update(self):
        self.count_anim += 1
        if self.count_anim == 3:
            self.frame = (self.frame + 1) % 4
            self.count_anim = 0
    def set_pos(self,x,y):
        self.x = x
        self.y = y
class Bricks:
    def __init__(self):
        self.image = load_image('block_2.png')
        self.frame = 0
        self.count_anim = 0
        self.x = 0
        self.y = 0

    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 40,self.x,self.y)

    def update(self):
        self.count_anim +=1
        if self.count_anim == 4:
            self.frame = (self.frame + 1) % 4
            self.count_anim = 0

    def set_pos(self, x, y):
        self.x = x
        self.y = y


