import random
from pico2d import *

class WALK:
    def enter(self, event):
        pass

    def exit(self):
        pass

    def do(self):
        self.count_anim+=1
        if self.count_anim == 3:
            self.frame = (self.frame + 1) % 17 + 1  # 방향 전환 frame: 1
            self.count_anim = 0

        self.x += self.x_dir

    def draw(self):
        self.image.clip_draw(self.frame * 25, 50 * self.action, 25, 50, self.x, 100)

class RedKoopa:
    image = None
    def __init__(self):
        if RedKoopa.image == None:
            RedKoopa.image = load_image('red_koopa.png')

        self.frame = 1
        self.x = random.randint(400, 3000)
        self.x_dir = -1
        self.action = 1
        self.count_anim = 0

        self.cur_state = WALK
        self.cur_state.enter(self, None)


    def draw(self):
        self.cur_state.draw(self)


    def update(self):
        self.cur_state.do(self)
        self.count_anim += 1

class GreenKoopa:
    image = None
    def __init__(self):
        if GreenKoopa.image == None:
            GreenKoopa.image = load_image('green_koopa.png')
        self.frame = 1
        self.action = 0
        self.x = random.randint(400, 3000)
        self.x_dir = -1
        self.action = 1
        self.count_anim = 0

        self.cur_state = WALK
        self.cur_state.enter(self, None)


    def draw(self):
        self.cur_state.draw(self)


    def update(self):
        self.cur_state.do(self)
