import random
from pico2d import *
import game_framework
import game_world
import server
from item import *
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
class stair_block:
    image = None
    def get_name(self):
        return 'stair_block'

    def edit_x(self, x):
        self.x -= x
    def __init__(self):
        if stair_block.image == None:
            stair_block.image = load_image('block_3.png')
        self.frame = 0
        self.x = 0
        self.y = 0
        self.x_size = 30
        self.y_size = 40

    def returnY(self):
        return self.y
    def draw(self):
        # self.image.clip_draw(int(self.frame) * 30, 0, 30, 40, self.x, self.y)
        self.image.clip_composite_draw(int(self.frame)*30, 0, 30, 40, 0, ' ', self.x, self.y,self.x_size,self.y_size)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def update(self):
        if self.x <= 800:
            self.frame = 0
            self.x_size = 30
            self.y_size = 30
    def handle_collision(self, other, group, p):
        if group == 'player:stair_block':
           pass

    def set_pos(self, x, y):
        self.x = x
        self.y = y - 5





class item_block:
    image = None
    def get_name(self):
        return 'item_block'

    def edit_x(self, x):
        self.x -= x

    def __init__(self):
        if item_block.image == None:
            item_block.image = load_image('block_1.png')
        self.frame = 0
        self.x = 0
        self.y = 0
        self.Y_gravity = 15
        self.temp = 0
        self.mario_size = ' '
        self.up = False
        self.Y_velocity = 0
        self.jump_height = 0
        self.type =' '
        self.x_size = 30
        self.y_size = 40
    def draw(self):
        # self.image.clip_draw(int(self.frame) * 30, 0, 30, 40, self.x, self.y)
        self.image.clip_composite_draw(int(self.frame)*30, 0, 30, 40, 0, ' ', self.x, self.y,self.x_size,self.y_size)
        draw_rectangle(*self.get_bb())
    def up_box(self):
        self.y += self.Y_velocity * game_framework.frame_time
        self.Y_velocity -= self.Y_gravity

        if self.y <= self.temp:
            self.up = False
            self.y = self.temp
            self.Y_velocity = self.jump_height
            self.available = False


    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def update(self):
        if self.x <= 800:
            if self.up and self.available:
                self.up_box()

            if self.citem:
                self.gen_item()
                self.citem = False

            if not self.available:
                self.image = load_image('unblock_1.png')
                self.frame = 0
                self.x_size = 30
                self.y_size = 30
            else:
                self.frame = (self.frame + ACTION_PER_TIME * 4 * game_framework.frame_time) % 4
                self.x_size = 30
                self.y_size = 40

    def set_pos(self,x,y, type = 'coin'):
        self.x = x
        self.y = y
        self.temp = y
        self.jump_height = y + 10
        self.Y_velocity =self.jump_height
        self.type = type
        self.available = True
        self.citem = False
    def returnY(self):
        return self.y
    def gen_item(self):
        if self.available:
            if self.type =='item':
                if server.player.mario_size == 'Small':
                    Mushroom = MUSHROOM(self.x, self.y + 17)
                    game_world.add_collision_group(server.player, Mushroom, 'player:mushroom')
                    game_world.add_collision_group(Mushroom, server.ground, 'mushroom:ground')
                    game_world.add_collision_group(Mushroom,self, 'mushroom:itemBox')
                    game_world.add_collision_group(Mushroom, server.bricks, 'mushroom:brick')

                    game_world.add_object(Mushroom, 1)
                else:
                    Flower = FLOWER(self.x, self.y + 45)
                    game_world.add_collision_group(server.player, Flower, 'player:flower')
                    game_world.add_object(Flower, 1)
            elif self.type == 'coin':
                coin = COIN(self.x,self.y + 20, 'onblock')
                game_world.add_object(coin,1)
    def handle_collision(self, other, group, p):
        if group == 'player:item_block':
            if p == 'top' and not server.player.die:
                self.citem =True
                self.up = True



class COIN:
    def get_name(self):
        return 'coin'
    def get_bb(self):
        return self.x - 10, self.y - 10,self.x + 10, self.y + 10

    def edit_x(self, x):
        self.x -= x

    def up_coin(self):
        self.y += self.Y_velocity * game_framework.frame_time
        self.Y_velocity -= self.Y_gravity
        if self.Y_velocity < 0:
            game_world.remove_object(self)

    def __init__(self ,x, y, gen = 'onground'):
        self.image = load_image('coin.png')
        self.frame = random.randint(0,3)
        self.x = x
        self.y = y
        self.jump_height = y + 5
        self.Y_velocity = self.jump_height
        self.Y_gravity = 5
        self.gen = gen
    def draw(self):
        self.image.clip_draw(int(self.frame) * 25 ,0 ,25 ,25 ,self.x, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):
        if self.x <= 800:
            if self.gen != 'onground':
                self.up_coin()
            self.frame = (self.frame + ACTION_PER_TIME * 4 * game_framework.frame_time) % 4

    def returnY(self):
        return self.y

    def handle_collision(self, other, group, pos):
        # print('ball disappear')
        if group == 'player:coin':
            game_world.remove_object(self)

class Bricks:
    def get_name(self):
        return 'brick'

    def edit_x(self, x):
        self.x -= x

    def __init__(self):
        self.image = load_image('block_2.png')
        self.frame = 0
        self.x = 0
        self.y = 0
        self.available = True
        self.up = False
        self.y_size = 40
        self.jump_height = 0
        self.Y_velocity = self.jump_height
        self.Y_gravity = 15
        self.temp = 0
    def draw(self):
        self.image.clip_composite_draw(int(self.frame) * 30, 0, 30, 40, 0, ' ', self.x, self.y, 30,
                                       self.y_size)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.up and self.available:
            self.up_box()
        if not self.available and self.op == 'destroy':
            try:
                game_world.remove_object(self)
            except:
                pass
        elif not self.available and self.op == 'solid':
            self.image = load_image('unblock_1.png')
            self.frame = 0
            self.y_size = 30


        self.frame = (self.frame + ACTION_PER_TIME * 4 * game_framework.frame_time) % 4

    def up_box(self):
        self.y += self.Y_velocity * game_framework.frame_time
        self.Y_velocity -= self.Y_gravity
        if self.y <= self.temp:
            self.up = False
            self.y = self.temp
            self.Y_velocity = self.jump_height

            self.available = False
    def set_pos(self, x, y, op = 'destroy'):
        self.x = x
        self.y = y
        self.temp = y
        self.op = op
        self.jump_height = y + 10
        self.Y_velocity = self.jump_height

    def returnY(self):
        return self.y

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
    def handle_collision(self, other, group, pos):
        # print('ball disappear')
        if group == 'player:bricks':
           if pos =='top':
             self.up = True


