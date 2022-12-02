from pico2d import*
import numpy as np
import game_world
import server

INFO = np.zeros((13, 40))
for i in range(40):
    INFO[0, i] = 1

class Empty_Tile:
    image = None
    def __init__(self, col, row):
        self.x, self.y = row * 192, col * 77
    def get_name(self):
        return 'background'
    def edit_x(self,x):
        self.x-=x
    def get_bb(self):
        return self.x - 98, self.y - 40, self.x + 98, self.y + 200
    def __init__(self,col, row):
        self.x, self.y = row * 192, col * 77
    def update(self):
        pass
    def draw(self):
        pass

    def handle_collision(self, other, group, pos):
        pass


class Floor_Tile(Empty_Tile):
    def __init__(self,col, row):
        self.x, self.y = row * 192, col * 77

    def get_bb(self):
        return self.x - 400, self.y - 40, self.x + 400, self.y + 45
    def update(self):
        pass
    def draw(self):
        pass
    def handle_collision(self,other,group,pos):
        pass


class BACKGROUND:
    def get_name(self):
        return 'background'
    def __init__ (self):
        self.image = load_image('./background/tower_background.png')
        self.bgm = load_music('./music/stage3.mp3')
        self.bgm.set_volume(40)
        self.bgm.repeat_play()
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.x = self.w/2
        self.y = self.h/2
        self.window_bottom = 0
    def draw (self):
        self.image.draw(self.x,self.y)
    def update(self):
        pass
