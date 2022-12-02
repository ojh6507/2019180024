from pico2d import*
import numpy as np
import game_world

INFO = np.zeros((13, 6))
for i in range(6):
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
            Floor_Tile.image = load_image('background/rock_ground.png')
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
            under_Tile.image = load_image('background/underground.png')
        self.x, self.y = row * 192, col * 77



class BACKGROUND:
    def get_name(self):
        return 'background'
    def __init__ (self):
        self.image = load_image('background/destroy_world.png')
        self.x = 400
    def edit_x(self,x):
        self.x-=x
    def get_pos(self):
        return self.x
    def draw (self):
        self.image.draw(self.x, 400)
    def update(self):
        pass
