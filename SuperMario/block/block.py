import random
from pico2d import *
import game_framework
import game_world
import server

from item import *
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

OPEN_TIME_PER_ACTION = 1
OPEN_PER_TIME = 1.0 / OPEN_TIME_PER_ACTION

JUMP_SPEED_KMPH = 10.0
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

class Boss_Door:
    image = None
    sound = None
    def __init__(self):
        if Boss_Door.image == None:
            Boss_Door.image = [load_image("./block/BossDoor/" + "bd_" + "%d" %i + ".png") for i in range(1, 15)]
        if Boss_Door.sound == None:
            Boss_Door.sound = load_wav('./music/door_open.wav')
            Boss_Door.sound.set_volume(30)

        self.frame = 0
        self.reflect = ' '
        self.x_size = 117
        self.y_size = 98
        self.x = 400
        self.y = 82
        self.bb_x = self.x_size //2
        self.bb_y = self.y_size // 2
        self.activate = True
        self.working = False
        self.trans_scene = False
        self.play_sound = True
    def update(self):
        if self.working:
            if self.play_sound:
                self.sound.play()
                self.play_sound = False
            self.frame = (self.frame + len(Boss_Door.image) * OPEN_PER_TIME * game_framework.frame_time) % len(Boss_Door.image)

        if int(self.frame) == len(Boss_Door.image) - 1:
            self.frame = len(Boss_Door.image) - 1
            self.trans_scene = True
            self.working = False

    def draw(self):
        self.image[int(self.frame)].clip_composite_draw(0, 0, 107, 68, 0, self.reflect, self.x, self.y,
                                                                    self.x_size, self.y_size)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.bb_x, self.y - self.bb_y, self.x + self.bb_x, self.y + self.bb_y
    def handle_collision(self, other, group, p):
        pass



class Door:
    image = None
    def get_name(self):
        return 'pipe'

    def edit_x(self, x):
        self.x -= x

    def __init__(self):
        if Door.image == None:
            Pipe.image = load_image('./block/pipe.png')
        self.activate = False
        self.x = 750
        self.y = 75
        self.x_size = 46
        self.y_size = 62
        self.bb_x = self.x_size//2
        self.bb_y = self.y_size//2
        self.num = 0

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def get_bb(self):
        return self.x - self.bb_x, self.y - self.bb_y, self.x + self.bb_x, self.y + self.bb_y

    def draw(self):
        self.image.clip_composite_draw(0, 0, 32, 48, 0, ' ', self.x, self.y, self.x_size, self.y_size)


    def update(self):
        if self.activate:
            self.image = load_image('./block/avail_door.png')
        else:
            self.image = load_image('./block/closed_door.png')

        self.bb_x = self.x_size // 2
        self.bb_y = self.y_size // 2

    def handle_collision(self, other, group, p):
        pass


class Pipe:
    image = None
    font = None
    def get_name(self):
        return 'pipe'
    def edit_x(self, x):
        self.x -= x
    def __init__(self):
        if Pipe.image == None:
            Pipe.image = load_image('./block/pipe.png')
        if Pipe.font == None:
            Pipe.font = load_font('./block/SuperMario256.ttf', 14)
        self.activate = False
        self.type = 'goal'
        self.x = 7100
        self.y = 80
        self.tempy = self.y
        self.x_size = 55
        self.y_size = 90

        self.bb_x = 30
        self.bb_y = 45
        self.num = 0

    def setPos(self,x,y, num = 0, type = 'goal'):
        self.x = x
        self.y = y
        self.tempy = y
        self.type = type
        self.num = num


    def get_bb(self):
        return self.x - self.bb_x , self.y - self.bb_y, self.x + self.bb_x, self.y + self.bb_y

    def draw(self):
        if self.type == 'stage':
            self.font.draw(self.x - self.bb_x , self.y + self.bb_y + 20, 'Stage %d' %self.num, (255, 255, 255))

        self.image.clip_composite_draw(0, 0, 35, 40, 0, ' ', self.x, self.y, self.x_size,self.y_size)

        pass
    def update(self):
        if self.activate:
            self.image = load_image('./block/pipe.png')
            self.x_size = 55
            self.y_size = 90
            self.y = self.tempy
        else:
            self.image = load_image('./block/broken_pipe.png')
            self.x_size = 45
            self.y_size = 50
            self.y = self.tempy - 15
        self.bb_x = self.x_size // 2
        self.bb_y = self.y_size // 2
        pass

    def handle_collision(self, other, group, p):
        pass



class item_block:
    image = None
    effect = None
    def get_name(self):
        return 'item_block'

    def edit_x(self, x):
        self.x -= x

    def __init__(self):
        if item_block.image == None:
            item_block.image = load_image('./block/block_1.png')
        if item_block.effect ==None:
            item_block.effect = load_wav('./music/Bump.wav')
            item_block.effect.set_volume(40)

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
        self.x_size = 33
        self.y_size = 40
    def draw(self):
        # self.image.clip_draw(int(self.frame) * 30, 0, 30, 40, self.x, self.y)
        self.image.clip_composite_draw(int(self.frame)*30, 0, 30, 40, 0, ' ', self.x, self.y,self.x_size,self.y_size)
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
                self.image = load_image('./block/unblock_1.png')
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
        self.jump_height = y + 3
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
                    game_world.add_collision_group(Mushroom, server.itemBox, 'mushroom:itemBox')
                    game_world.add_collision_group(Mushroom, server.bricks, 'mushroom:brick')

                    game_world.add_object(Mushroom, 1)
                else:
                    Flower = FLOWER(self.x, self.y + 45)
                    game_world.add_collision_group(server.player, Flower, 'player:flower')
                    game_world.add_object(Flower, 1)
            elif self.type == 'coin':
                coin = COIN()
                coin.set_pos(self.x, self.y, 'block')
                game_world.add_object(coin,1)
                server.coin_count += 1
                coin.sound.play()

    def handle_collision(self, other, group, p):
        if group == 'player:item_block':
            if p == 'top' and not server.player.die:
                self.citem =True
                self.up = True
                item_block.effect.play()



class COIN:
    sound = None
    image = None
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
    def set_pos(self,x,y, gen = 'onground'):
        self.x = x
        self.y = y
        self.jump_height = y + 5
        self.Y_velocity = self.jump_height
        self.gen = gen
    def __init__(self):
        if COIN.image == None:
            COIN.image = load_image('./block/coin.png')
        if COIN.sound == None:
            COIN.sound = load_wav('./music/Coin.wav')
            COIN.sound.set_volume(50)

        self.frame = random.randint(0,3)
        self.x = 0
        self.y = 0
        self.jump_height = 5
        self.Y_velocity = self.jump_height
        self.Y_gravity = 5
        self.gen = 'block'
    def draw(self):
        self.image.clip_draw(int(self.frame) * 25 ,0 ,25 ,25 ,self.x, self.y)


    def update(self):
        if self.x <= 800:
            if self.gen != 'onground':
                self.up_coin()
            self.frame = (self.frame + ACTION_PER_TIME * 4 * game_framework.frame_time) % 4

    def returnY(self):
        return self.y

    def handle_collision(self, other, group, pos):
        # print('ball disappear')
        if group == 'player:coin' and not server.player.die:
            COIN.sound.play()
            game_world.remove_object(self)

class Bricks:

    Brick_effect = None
    effect = None
    image = None
    def get_name(self):
        return 'brick'

    def edit_x(self, x):
        self.x -= x

    def __init__(self):
        if Bricks.image == None:
            Bricks.image = load_image('./block/block_2.png')
        if Bricks.Brick_effect == None:
            Bricks.Brick_effect = load_wav('./music/BrickBlock.wav')
            Bricks.Brick_effect.set_volume(50)
        if Bricks.effect == None:
            Bricks.effect = load_wav('./music/Bump.wav')
            Bricks.effect.set_volume(40)
        self.frame = 0
        self.x = 0
        self.y = 0
        self.available = True
        self.up = False
        self.y_size = 40
        self.x_size = 33

        self.jump_height = 0
        self.Y_velocity = self.jump_height
        self.Y_gravity = 15
        self.temp = 0
        self.clip = 4
        self.width = 30
        self.height = 40


    def draw(self):
        self.image.clip_composite_draw(int(self.frame) * self.width, 0,self.width, self.height, 0, ' ', self.x, self.y, self.x_size,
                                       self.y_size)

    def update(self):
        if self.up and self.available:
            self.up_box()
        if not self.available and self.op == 'destroy':
            self.image = load_image('./block/block_2_crack.png')
            self.clip = 4
            self.height = 40
            self.width = 40
            self.x_size = 80
            self.y_size = 80
            self.available = False
            self.y -= 10 * JUMP_SPEED_PPS * game_framework.frame_time

        elif not self.available and self.op == 'solid':
            self.image = load_image('./block/unblock_1.png')
            self.frame = 0
            self.y_size = 30


        self.frame = (self.frame + ACTION_PER_TIME * 4 * game_framework.frame_time) % self.clip
        if self.y < 0:
            try:
                game_world.remove_object(self)
            except:
                pass


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
        self.jump_height = y + 2
        self.Y_velocity = self.jump_height

    def returnY(self):
        return self.y

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
    def handle_collision(self, other, group, pos):
        # print('ball disappear')
        if group == 'player:bricks' and self.available and not server.player.die:
           if pos =='top':
             self.up = True
             self.frame = 0
             if self.op == 'destroy':
                 self.Brick_effect.play()
             else:
                 self.effect.play()



