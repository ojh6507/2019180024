from pico2d import*
import numpy as np
import game_world
import server

INFO = np.zeros((13, 40))
for i in range(40):
    INFO[0, i] = 1
INFO[1,3] = 1
INFO[0,3] = 2

INFO[1,5] = 1
INFO[0,5] = 2


INFO[0,8] = -1
INFO[0,10] = -1
INFO[0,25] = -1
INFO[0,28] = -1
INFO[0,31] = -1

INFO[1,12] = 1
INFO[0,12] = 2


INFO[1,13] = 1
INFO[0,13] = 2


INFO[1,16] = 1
INFO[0,16] = 2

INFO[0,17] = -1


INFO[1,19] = 1
INFO[0,19] = 2

INFO[2,20] = 1
INFO[1,20] = 2
INFO[0,20] = 2


INFO[1,35] = 1
INFO[0,35] = 2
INFO[2,36] = 1
INFO[1,36] = 2
INFO[0,36] = 2



INFO[1,21] = 1
INFO[0,21] = 2

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
        self.rect_x, self.rect_y = self.x, self.y

    def update(self):
        pass
    def draw(self):
        pass

    def handle_collision(self, other, group, pos):
        pass


class Floor_Tile(Empty_Tile):
    image = None
    def __init__(self,col, row):
        if Floor_Tile.image == None:
            Floor_Tile.image = load_image('background/sand_ground.png')
        self.x, self.y = row * 192, col * 77

    def get_bb(self):
        return self.x - 100, self.y - 40, self.x + 100, self.y + 40
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y)
    def handle_collision(self,other,group,pos):
        pass


class under_Tile(Floor_Tile):
    image = None

    def __init__(self, col, row):
        if under_Tile.image == None:
            under_Tile.image = load_image('background/sand_underground.png')
        self.x, self.y = row * 192, col * 77



class BACKGROUND:
    def get_name(self):
        return 'background'
    def __init__ (self):
        self.image = load_image('./background/background2.png')
        self.bgm = load_music('./music/stage2.mp3')
        self.bgm.set_volume(40)
        self.bgm.repeat_play()

        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.x = self.w/2
        self.y = self.h/2
        self.window_bottom = 0
    def edit_x(self,x):
        self.x -= x
    def get_pos(self):
        return self.x
    def draw (self):
        self.image.draw(self.x,self.y)
    def update(self):
        pass
