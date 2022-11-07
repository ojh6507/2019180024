import random
from pico2d import *

class WALK:
    def enter(self, event):
        self.x_dir = -2
        pass

    def exit(self):
        pass

    def do(self):
        self.count_anim += 1
        if self.count_anim == 3:
            self.frame = (self.frame + 1) % 9 + 1 #방향 전환 프레임: 1
            self.count_anim = 0

        self.x += self.x_dir * 1
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 28, 30 * self.action, 28, 30,self.x, self.y)

        pass

class GOOMBA:
    image = None

    def get_name(self):
        return 'monster'

    def __init__(self):
        if GOOMBA.image == None:
            GOOMBA.image = load_image('Goomba.png')
        self.frame  = 1
        self.action = 1
        self.x = random.randint(0, 800)
        self.x_dir = 0
        self.y = 85
        self.count_anim = 0
        self.turn = 0

        self.cur_state = WALK
        self.cur_state.enter(self, None)


    def draw(self):
        self.cur_state.draw(self)

    def update(self):
        self.cur_state.do(self)

    # def Goomba_right(self):
    #     self.action = 0
    #     self.x_dir = 1
    # def Goomba_left(self):
    #     self.action = 1
    #     self.x_dir = -1
    # def Gommba_turn(self):
    #     self.frame = 18
