from pico2d import *
import math
import server
import block.block
import game_framework
from fire import Ball
import game_world
from block import block


RD, LD, RU, LU, SPACE, ATTACK, SHIFTD, SHIFTU, SPACE = range(9)
event_name = ['RD', 'LD', 'RU', 'LU', 'JUMP', 'ATTACK']
key_event_table = {
(SDL_KEYDOWN, SDLK_SPACE): SPACE,
(SDL_KEYDOWN, SDLK_LSHIFT): SHIFTD,
(SDL_KEYDOWN, SDLK_RIGHT): RD,
(SDL_KEYDOWN, SDLK_LEFT): LD,
(SDL_KEYDOWN, SDLK_z): ATTACK,
(SDL_KEYUP, SDLK_RIGHT): RU,
(SDL_KEYUP, SDLK_LEFT): LU,
(SDL_KEYUP, SDLK_LSHIFT): SHIFTU

}

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 15.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

JUMP_SPEED_KMPH = 10.0
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)


class IDLE:
    def enter(self, event):
        self.x_dir = 0
        self.frame = 0
        self.Run = False
        self.TIME_PER_ACTION = 1
        if self.mario_size == 'Small':

            self.perframe = 30
            self.action = 0
            self.height = 35

        elif self.mario_size == 'Normal':

            self.perframe = 50
            self.action = 0
            self.height = 65

    def exit(self, event):
        if event == ATTACK:
           self.Fire_Ball()

    def do(self):
        if not self.jump:
            if self.mario_size == 'Small':
                # self.image = load_image('smario_idle.png')
                self.clip = 76

            elif self.mario_size == 'Normal':
                self.clip = 79
                # if not self.flower:
                #     self.image = load_image('idle_right.png')
                # else:
                #     self.image = load_image('flower_idle_right.png')
        else:
            self.jump_func()

            if self.mario_size == 'Small':
                # self.image = load_image('smario_jump.png')
                self.clip = 30
                self.TIME_PER_ACTION = 1
            elif self.mario_size == 'Normal':
                # if not self.flower:
                #     self.image = load_image('jump_right.png')
                # else:
                #     self.image = load_image('flower_jump_rig
                self.clip = 18
                self.TIME_PER_ACTION = 0.5

        if self.face_dir == 1:
            self.reflect = ' '
        else:
            self.reflect = 'h'

        self.frame = (self.frame + self.ACTION_PER_TIME * self.clip * game_framework.frame_time) % self.clip


    def draw(self):
        if self.jump:
            if self.mario_size == 'Small':
                self.image = load_image('smario_jump.png')

                self.perframe = 35
                self.action = 0
                self.height = 45


            if self.mario_size == 'Normal':
                if not self.flower:
                    self.image = load_image('jump_right.png')
                else:
                    self.image = load_image('flower_jump_right.png')

                self.perframe = 40
                self.action = 0
                self.height = 66

        if not self.jump:
            if self.mario_size == 'Small':
                self.image = load_image('smario_idle.png')
                self.perframe = 30
                self.action = 0
                self.height = 35

            elif self.mario_size == 'Normal':
                if not self.flower:
                    self.image = load_image('idle_right.png')
                else:
                    self.image = load_image('flower_idle_right.png')

                self.perframe = 50
                self.action = 0
                self.height = 65
        if self.delay > 1:
            if self.mario_size == 'Small':
                self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0, self.reflect, self.x, self.y, self.perframe, self.height)
            elif self.mario_size == 'Normal':
                if self.jump:
                    self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0,
                                                   self.reflect, self.x, self.y, 40, 40)
                else:
                    self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0,
                                               self.reflect, self.x, self.y, 50, 50)
        else:
            if self.delay_draw % 2 == 0:
                if self.mario_size == 'Small':
                    self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0,
                                                   self.reflect, self.x, self.y, self.perframe, self.height)
                elif self.mario_size == 'Normal':
                    if self.jump:
                        self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height,
                                                       0,
                                                       self.reflect, self.x, self.y, 40, 40)
                    else:
                        self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height,
                                                       0,
                                                       self.reflect, self.x, self.y, 50, 50)



class WALK:
    def enter(self, event):
        self.frame = 0
        self.walk = True
        if event == RD:
            self.face_dir = 1
            self.x_dir = self.face_dir
        elif event == LD:
            self.face_dir = -1
            self.x_dir = self.face_dir
        elif event == RU:
            self.face_dir = -1
            self.x_dir = self.face_dir
        elif event == LU:
            self.face_dir = 1
            self.x_dir = self.face_dir
        self.TIME_PER_ACTION = 1

    def exit(self,event):
        self.walk = False
        if event == ATTACK:
            self.Fire_Ball()
        self.velocity = 1

    def do(self):
        if self.Run:
            self.TIME_PER_ACTION = 0.4
            self.velocity = 3
            if self.mario_size == 'Small':
                # self.image = load_image('smario_run.png')
                self.clip = 13

            if self.mario_size == 'Normal':
                # if not self.flower:
                #     self.image = load_image('run_fast.png')
                # else:
                #     self.image = load_image('flower_run_fast.png')
                self.clip = 18

        if not self.Run:
            self.TIME_PER_ACTION = 1
            self.velocity = 1
            if self.mario_size == 'Small':
                self.clip = 27
            if self.mario_size == 'Normal':
                self.clip = 25

        if self.jump:
            if self.mario_size == 'Small':
                self.clip = 30
                self.TIME_PER_ACTION = 1

            elif self.mario_size == 'Normal':
                self.clip = 18
                self.TIME_PER_ACTION = 0.5
            self.jump_func()


        if self.face_dir == -1:
            self.reflect = 'h'
            self.face_dir = -1

        else:
            self.reflect = ' '
            self.face_dir = 1

        self.frame = (self.frame + self.ACTION_PER_TIME * self.clip * game_framework.frame_time) % self.clip
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time *self.velocity
        self.x = clamp(25, self.x, 800)

    def draw(self):
        if self.jump:
            if self.mario_size == 'Small':
                self.image = load_image('smario_jump.png')

                self.perframe = 35
                self.action = 0
                self.height = 45

            if self.mario_size == 'Normal':
                if not self.flower:
                    self.image = load_image('jump_right.png')
                else:
                    self.image = load_image('flower_jump_right.png')

                self.perframe = 40
                self.action = 0
                self.height = 66

        else:
            if self.Run and self.mario_size == 'Normal':
                if not self.flower:
                    self.image = load_image('run_fast.png')
                else:
                    self.image = load_image('flower_run_fast.png')

                self.perframe = 50
                self.action = 0
                self.height = 60

            elif self.Run and self.mario_size == 'Small':
                self.image = load_image('smario_run.png')

                self.perframe = 45
                self.action = 0
                self.height = 40

            elif not self.Run and self.mario_size == 'Small':
                self.image = load_image('smario_walk.png')
                self.perframe = 30
                self.action = 0
                self.height = 40

            elif not self.Run and self.mario_size == 'Normal':
                if not self.flower:
                    self.image = load_image('mario_walk.png')
                else:
                    self.image = load_image('flower_mario_walk.png')
                self.perframe = 50
                self.action = 70
                self.height = 65
        if self.delay > 1:
            if self.mario_size == 'Small':
                self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0,
                                               self.reflect, self.x, self.y, self.perframe, self.height)
            elif self.mario_size == 'Normal':
                if self.jump:
                    self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0,
                                                   self.reflect, self.x, self.y, 40, 40)
                else:
                    self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0,
                                               self.reflect, self.x, self.y, 50, 50)
        else:
            if self.delay_draw % 2 == 0:
                if self.mario_size == 'Small':
                    self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0,
                                                   self.reflect, self.x, self.y, self.perframe, self.height)
                elif self.mario_size == 'Normal':
                    if self.jump:
                        self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height,
                                                       0,
                                                       self.reflect, self.x, self.y, 40, 40)
                    else:
                        self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height,
                                                       0,
                                                       self.reflect, self.x, self.y, 50, 50)



class Clear_movement:
    def enter(self,event):
        pass
    def exit(self, event):
        pass
    def do(self):
        self.Onground = False
        self.image = load_image('clear_mario.png')
        self.clip = 9
        self.height = 37
        self.perframe = 33
        self.y += JUMP_SPEED_PPS * game_framework.frame_time * 2
        self.frame = (self.frame + self.ACTION_PER_TIME * self.clip * game_framework.frame_time) % self.clip

    def draw(self):
        if self.mario_size == 'Small':
            self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0,
                                           self.reflect, self.x, self.y, 50, 40)

        elif self.mario_size == 'Normal':
            self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0,
                                       self.reflect, self.x, self.y, 50, 50)



class DIE:
    def enter(self, event):
        self.die = True
        pass

    def exit(self, event):
        pass

    def do(self):
        self.Onground = False
        self.image = load_image('gameover_mario.png')
        self.clip = 13
        self.height = 60
        self.perframe = 50
        self.jump_func()
        self.frame = (self.frame + self.ACTION_PER_TIME * self.clip * game_framework.frame_time) % self.clip


    def draw(self):
        if self.mario_size == 'Small':
            self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0,
                                           self.reflect, self.x, self.y, 40, 40)

        elif self.mario_size == 'Normal':
            self.image.clip_composite_draw(int(self.frame) * self.perframe, 0, self.perframe, self.height, 0,
                                       self.reflect, self.x, self.y, 50, 50)

next_state = {
    IDLE: {RU: WALK, LU: WALK, RD: WALK, LD: WALK, ATTACK: IDLE, SHIFTD: IDLE, SHIFTU: IDLE, SPACE: IDLE},
    WALK: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, ATTACK: WALK, SHIFTD: WALK, SHIFTU: WALK, SPACE: WALK},
    DIE: {RU: DIE, LU: DIE, RD: DIE, LD: DIE, ATTACK: DIE, SHIFTD: DIE, SHIFTU: DIE, SPACE: DIE},
    Clear_movement: {RU: Clear_movement, LU: Clear_movement, RD: Clear_movement, LD: Clear_movement, ATTACK: Clear_movement, SHIFTD: Clear_movement, SHIFTU: Clear_movement, SPACE: Clear_movement}


}

class mario:
    def get_name(self):
        return 'player'
    def __init__(self):

        self.TIME_PER_ACTION = 1
        self.ACTION_PER_TIME = 1
        self.image = load_image('smario_idle.png')
        self.mario_size = 'Small'
        self.frame = 0
        self.die = False
        self.height = 0
        self.action = 0
        self.perframe = 0
        self.reflect = ' '
        self.delay_draw = 0
        self.clip = 76
        self.x = 100
        self.y = 100

        self.x_dir = 0
        self.face_dir = 1
        self.y_dir = 0

        self.velocity = 2

        self.flower = False
        self.Run = False
        self.walk = False
        self.growup = False
        self.jump = False
        self.Onground = True

        self.mass = 10
        self.jump_height = 10

        self.Y_gravity = 0.25
        self.Y_velocity = self.jump_height
        self.count_grow = 0
        self.count_jump = 0

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.timer = 1
        self.delay = 1
        self.invincibility = False


    def jump_func(self):
        self.y += self.Y_velocity * JUMP_SPEED_PPS * game_framework.frame_time
        self.Y_velocity -= self.Y_gravity
        if self.Onground:
            self.jump = False
            self.Y_velocity = self.jump_height

    def update(self):
        self.ACTION_PER_TIME = 1.0 / self.TIME_PER_ACTION
        self.cur_state.do(self)
        self.delay += game_framework.frame_time
        self.delay_draw += 1
        if self.y < 0:
            self.event_que.clear()

        if self.event_que:
            event = self.event_que.pop()

            if event == SPACE:
                if self.Onground:
                    self.frame = 0
                    self.jump = True
                    self.Onground =False
            elif event == SHIFTD:
                self.frame = 0
                self.Run = True
            if event == SHIFTU:
                self.Run = False

            self.cur_state.exit(self,event)

            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('Error: ', self.cur_state.__name__,' ', event_name[event])
            self.cur_state.enter(self, event)
        self.x = clamp(0,self.x,800)

        if not self.jump:
            self.Onground = False
            self.y -= self.Y_gravity * JUMP_SPEED_PPS * 20 * game_framework.frame_time

        if self.invincibility:
            self.timer -= game_framework.frame_time
            if self.timer <= 0:
                self.invincibility = False
                self.timer = 1.0

        if self.die:
            self.delay = 1.1
            self.jump = True
            self.Run = False
            self.cur_state = DIE
        if server.world.x < -2950:
            self.cur_state = Clear_movement
            self.jump = True

        if not self.jump and (self.Run or self.walk):
            self.Onground = True

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def add_event(self,event):
        self.event_que.insert(0, event)
    def handle_event(self, event):
       if(event.type, event.key) in key_event_table:
           key_event = key_event_table[(event.type, event.key)]
           self.add_event(key_event)
    def Fire_Ball(self):
        if self.flower:
            ball = Ball(self.x, self.y, self.face_dir * self.velocity)
            game_world.add_collision_group(ball, server.ground, 'fire:ground')
            game_world.add_collision_group(ball, server.goomba,'fire:goomba')
            game_world.add_collision_group(ball, server.red, 'fire:red')
            game_world.add_collision_group(ball, server.green, 'fire:green')
            game_world.add_object(ball, 1)
    def check_state(self):
        self.delay = -1
        if not self.invincibility:
            if self.mario_size == 'Small':
                self.die = True
            elif self.mario_size == 'Normal':
                if self.flower == True:
                    self.flower = False
                else:
                    self.mario_size = 'Small'
                self.jump_height = 10
                self.Y_velocity = self.jump_height
                self.Onground = True
    def get_bb(self):
        if self.mario_size == 'Small':
            return self.x - 10, self.y - 17, self.x + 10, self.y + 10
        elif self.mario_size == 'Normal':
                return self.x - 10, self.y - 17, self.x + 10, self.y+8

    def get_pos(self):
        return self.x,self.y
    def edit_x(self,x):
        self.x = x

    def handle_collision(self, other, group, pos):
        if not self.die:
            if group =='player:stair':
                if pos == 'bottom':
                    self.Onground = True
                    if abs(self.x - other.x) <= 15:
                        if self.y > other.y:
                            self.y = other.y + 35
                if pos == 'right':
                    self.x_dir = 0
                    self.x -= 10

                if pos == 'left':
                    self.x_dir = 0
                    self.x += 10
            if group == 'player:coin':
                    pass
            elif group == 'player:item_block':
                if pos == 'bottom':
                    self.Onground = True
                    if abs(self.x - other.x) <= 15:
                        # if self.mario_size == 'Small':
                        self.y = other.y + 35
                        # else:
                        #     self.y = other.y + 40
                if pos == 'right':
                    self.x -= 15
                    self.x_dir = 0

                if pos == 'left':
                    self.x += 15
                    self.x_dir = 0

                if pos == 'top':
                    self.Onground = False
                    if self.Y_velocity > 0:
                        self.Y_velocity *= -1
                        self.y += self.Y_velocity * JUMP_SPEED_PPS * game_framework.frame_time

            elif group == 'player:bricks':
                if pos == 'bottom':
                    self.Onground = True
                    if abs(self.x - other.x) <= 15:
                        # if self.mario_size =='Small':
                        if self.y > other.y:
                            self.y = other.y + 35
                        # else:
                        #     if self.y > other.y:
                        #         self.y = other.y + 40

                if pos == 'right':
                    self.x_dir = 0
                    self.x -= 10

                if pos == 'left':
                    self.x_dir = 0
                    self.x += 10

                if pos == 'top':
                    self.Onground = False
                    if self.Y_velocity > 0:
                        self.Y_velocity *= -1
                        self.y += self.Y_velocity * JUMP_SPEED_PPS * game_framework.frame_time

            elif group == 'player:mushroom':
                self.mario_size = 'Normal'
                self.jump_height = 13
                self.y+= 20
                self.Y_velocity = self.jump_height
                self.Onground = True

            elif group == 'player:flower':
                self.mario_size = 'Normal'
                self.jump_height = 13
                self.Y_velocity = self.jump_height
                self.flower = True
                self.Onground = True

            elif group == 'player:ground':

                if pos == 'bottom':
                    self.Onground =True
                    # if abs(other.y + 70) < 140:
                    if self.mario_size == 'Small':
                        if self.y > other.y:
                            self.y = other.y + 58
                    else:
                        if self.y > other.y:
                            self.y = other.y + 61

                if pos == 'right':
                    self.Onground = True
                    self.x_dir = 0
                    self.x -= 10

                if pos == 'left':
                    self.Onground = True
                    self.x_dir = 0
                    self.x += 10

            elif group == 'player:red':
                if pos =='bottom':
                    self.jump = True
                    self.Onground = False

                    self.Y_velocity = self.jump_height
                    self.jump_func()
                elif pos == 'right' and not self.invincibility:
                    self.x += -1 * RUN_SPEED_PPS * game_framework.frame_time * 4 * self.velocity
                    self.check_state()
                    self.invincibility = True

                elif pos == 'left' and not self.invincibility:
                    self.x += 1 * RUN_SPEED_PPS * game_framework.frame_time * 4 * self.velocity
                    self.check_state()
                    self.invincibility = True

            elif group == 'player:green':
                if pos == 'bottom':
                    self.jump = True
                    self.Onground = False

                    self.Y_velocity = self.jump_height
                    self.jump_func()
                elif pos == 'right' and not self.invincibility:
                    self.x += -1 * RUN_SPEED_PPS * game_framework.frame_time * 4  *self.velocity
                    self.check_state()
                    self.invincibility = True

                elif pos == 'left' and not self.invincibility:
                    self.x += 1 * RUN_SPEED_PPS * game_framework.frame_time * 4* self.velocity
                    self.check_state()
                    self.invincibility = True


            elif group == 'player:goomba':
                if pos == 'bottom':
                    self.jump = True
                    self.Onground = False
                    self.Y_velocity = self.jump_height
                    self.jump_func()
                elif pos == 'right' and not self.invincibility:
                    self.x += -2 * RUN_SPEED_PPS * game_framework.frame_time * 4 * self.velocity
                    self.check_state()
                    self.invincibility = True
                elif pos == 'left' and not self.invincibility:
                    self.x += 2 * RUN_SPEED_PPS * game_framework.frame_time * 4 * self.velocity
                    self.check_state()
                    self.invincibility = True
                elif pos == 'top' and not self.invincibility:
                    self.check_state()
                    self.invincibility = True



