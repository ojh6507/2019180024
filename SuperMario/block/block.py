from pico2d import *

class item_block:
    def __init__(self):
        self.image = load_image('block_1.png')
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 40, 330, 90)
    def update(self):
        self.frame = (self.frame+1)%4

class COIN:
    def __init__(self):
        self.image =load_image('coin.png')
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 25 ,0 ,25 ,25 ,400,90)
    def update(self):
        self.frame = (self.frame + 1) % 4
        delay(0.03)

class Bricks:
    def __init__(self):
        self.image = load_image('block_2.png')
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 40, 370, 90)

    def update(self):
        self.frame = (self.frame + 1) % 4


