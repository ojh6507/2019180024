from pico2d import*
import numpy as np
import game_world
INFO =np.zeros((34,254))
for i in range(254):
    INFO[2,i] = 1

INFO[6,10] = 2

print(INFO)

TILESIZE = 30
TILESIZE2 = 30
def set_world():
    for col in range(len(INFO)):
        for row in range(len(INFO[col])):
            if INFO[col][row] == 0:
                empty = Empty_Tile(col, row)
                game_world.add_object(empty,2)
            elif INFO[col][row] == 1:
                print(1)
                ground = Floor_Tile(col, row, TILESIZE)
                game_world.add_object(ground,3)
            elif INFO[col][row] == 2:
                print(1)
                ground = Floor_Tile(col, row, TILESIZE2)
                game_world.add_object(ground, 3)


class Floor_Tile:
    image = None
    def get_name(self):
        return 'background'

    def __init__(self,col, row, size =1):
        if Floor_Tile.image == None:
            # Floor_Tile.image =load_image('test_tile.png')
            Floor_Tile.image = load_image('upper_t1.png')
        self.tilesize = size
        self.x, self.y = row * self.tilesize, col * self.tilesize
        self.rect_x, self.rect_y = self.x, self.y


    def get_rect(self):
        #self.x - self.size = left
        #self.x + self.size = right
        pass
        # return self.y + self.size//2, self.y - self.size//2, self.x - self.size//2, self.x + self.size//2
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y)
        pass

class Empty_Tile:
    image = None
    def get_name(self):
        return 'background'

    def __init__(self,col, row):
        if Empty_Tile.image == None:
            Empty_Tile.image =load_image('test_tile.png')

        self.x, self.y = row * 50, col * 50
        self.rect_x, self.rect_y = self.x, self.y


    def get_rect(self):
        #self.x - self.size = left
        #self.x + self.size = right
        pass
        # return self.y + self.size//2, self.y - self.size//2, self.x - self.size//2, self.x + self.size//2
    def update(self):
        pass
    def draw(self):
        pass

class Item_Tile:
    def get_name(self):
        return 'background'

    def __init__(self,col, row, size):
        self.tilesize = size
        self.grid_x, self.grid_y = row * self.tilesize, col * self.tilesize
        self.rect_x, self.rect_y = self.grid_x, self.grid_y


    def get_rect(self):
        #self.x - self.size = left
        #self.x + self.size = right
        pass
        # return self.y + self.size//2, self.y - self.size//2, self.x - self.size//2, self.x + self.size//2
    def update(self):
        pass
    def draw(self):
        pass

class BACKGROUND:
    def get_name(self):
        return 'background'
    def __init__ (self):
        self.image = load_image('background_2.png')
        self.x = 3750
    def draw (self):
        self.image.draw(self.x, 500)

    def update(self):
        pass



