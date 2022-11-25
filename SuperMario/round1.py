from pico2d import*
import numpy as np
import game_world

INFO = np.zeros((13, 40))
for i in range(40):
    INFO[0, i] = 1

INFO[0,8] = 0
INFO[0,10] = 0
INFO[0,25] = 0
INFO[0,28] = 0
INFO[0,31] = 0


INFO[1,13] = 1
INFO[0,13] = 2

INFO[1,19] = 1
INFO[0,19] = 2

INFO[2,20] = 1
INFO[1,20] = 2
INFO[0,20] = 2

INFO[1,21] = 1
INFO[0,21] = 2

# def set_world():
#
#     for col in range(len(INFO)):
#         for row in range(len(INFO[col])):
#
#             if INFO[col][row] == 0:
#                 empty = Empty_Tile(col, row)
#                 game_world.add_object(empty,2)
#
#             elif INFO[col][row] == 1:
#                 ground = Floor_Tile(col, row)
#                 game_world.add_object(ground,3)
#
#             elif INFO[col][row] == 2:
#                 underground = under_Tile(col, row)
#                 game_world.add_object(underground,3)

class Empty_Tile:
    image = None
    def get_name(self):
        return 'background'
    def edit_x(self,x):
        self.x-=x
    def __init__(self,col, row):
        self.x, self.y = row * 50, col * 50
        self.rect_x, self.rect_y = self.x, self.y

    def update(self):
        pass
    def draw(self):
        pass


class Floor_Tile(Empty_Tile):
    image = None
    def __init__(self,col, row):
        if Floor_Tile.image == None:
            Floor_Tile.image = load_image('ground.png')
        self.x, self.y = row * 192, col * 77

    def get_bb(self):
        return self.x - 96, self.y - 40, self.x + 96, self.y + 40
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
    def handle_collision(self,other,group,pos):
        pass


class under_Tile(Floor_Tile):
    image = None

    def __init__(self, col, row):
        if under_Tile.image == None:
            under_Tile.image = load_image('underground.png')
        self.x, self.y = row * 192, col * 77



class BACKGROUND:
    def get_name(self):
        return 'background'
    def __init__ (self):
        self.image = load_image('background.png')
        self.x = 3750
    def edit_x(self,x):
        self.x-=x
    def get_pos(self):
        return self.x
    def draw (self):
        self.image.draw(self.x, 500)
    def update(self):
        pass
