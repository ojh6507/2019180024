from pico2d import *
import math
import game_framework
from fire import Ball
import game_world

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
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class IDLE:
    def enter(self, event):
        self.x_dir = 0
        self.Run = False
        pass

    def exit(self, event):
        if event == ATTACK:
           self.Fire_Ball()
        pass

    def do(self):
        if not self.jump:
            if self.mario_size == 'Small':
                self.image = load_image('smario_idle.png')
                self.clip = 76
            elif self.mario_size == 'Normal':
                self.clip = 79
                if not self.flower:
                    self.image = load_image('idle_right.png')
                else:
                    self.image = load_image('flower_idle_right.png')
        else:
            self.y += self.Y_velocity
            self.Y_velocity -= self.Y_gravity

            if self.face_dir == 1:
                if self.mario_size == 'Small':
                    self.image = load_image('smario_jump.png')
                    self.clip = 30
                elif self.mario_size == 'Normal':
                    if not self.flower:
                        self.image = load_image('jump_right.png')
                    else:
                        self.image = load_image('flower_jump_right.png')
                    self.clip = 18

            elif self.face_dir == -1:
                if self.mario_size == 'Small':
                    self.image = load_image('smario_jump.png')
                    self.action = 45
                    self.ch_size = 35
                    self.height = 45
                    self.clip = 30

                elif self.mario_size == 'Normal':
                    if not self.flower:
                        self.image = load_image('jump_left.png')
                    else:
                        self.image = load_image('flower_jump_left.png')
                    self.clip = 18

            if self.Y_velocity < -self.jump_height:
                self.jump = False
                self.Y_velocity = self.jump_height

        self.frame = (self.frame + 1) % self.clip


    def draw(self):
        if self.jump:
            if self.face_dir == 1 and self.mario_size == 'Small':

                self.perframe = 35
                self.action = 0
                self.height = 45

            elif self.face_dir != 1 and self.mario_size == 'Small':

                self.perframe = 35
                self.action = 45
                self.height = 45

            elif self.mario_size == 'Normal':
                self.image.clip_draw(self.frame * 40, 0, 40, 66, self.x, self.y)

                self.perframe = 40
                self.action = 0
                self.height = 66

        else:
            if self.face_dir == 1 and self.mario_size == 'Small':

                self.perframe = 30
                self.action = 0
                self.height = 35

            elif self.face_dir == 1 and self.mario_size == 'Normal':

                self.perframe = 50
                self.action = 5
                self.height = 60

            elif self.face_dir == -1 and self.mario_size == 'Small':

                self.perframe = 30
                self.action = 38
                self.height = 35

            elif self.face_dir == -1 and self.mario_size == 'Normal':

                self.perframe = 50
                self.action = 5
                self.height = 65
        self.image.clip_draw(self.frame * self.perframe, self.action, self.perframe, self.height, self.x, self.y)


class WALK:
    def enter(self, event):
        if event == RD:
            self.x_dir += 1
            self.face_dir = 1
        elif event == LD:
            self.x_dir -= 1
            self.face_dir = -1
        elif event == RU:
            self.x_dir -= 1
        elif event == LU:
            self.x_dir += 1
    def exit(self,event):
        self.face_dir = self.x_dir

    def do(self):
        if not self.jump:
            if self.Run:
                self.velocity = 3
                if self.mario_size == 'Small':
                    self.image = load_image('smario_run.png')
                    self.clip = 13
                elif self.x_dir == -1 and self.mario_size == 'Normal':
                    if not self.flower:
                        self.image = load_image('runfast_left.png')
                    else:
                        self.image = load_image('flower_runfast_left.png')
                    self.clip = 18
                elif self.x_dir == 1 and self.mario_size == 'Normal':
                    if not self.flower:
                        self.image = load_image('run_fast.png')
                    else:
                        self.image = load_image('flower_run_fast.png')
                    self.clip = 18
            if not self.Run:
                self.velocity = 1
                if self.mario_size == 'Small':
                        self.image = load_image('smario_walk.png')
                        self.clip = 27
                elif self.mario_size == 'Normal':
                    self.clip = 25
                    if not self.flower:
                        self.image = load_image('mario_walk.png')
                    else:
                        self.image = load_image('flower_mario_walk.png')
        else:
            self.y += self.Y_velocity
            self.Y_velocity -= self.Y_gravity

            if self.face_dir == 1:
                if self.mario_size == 'Small':
                    self.image = load_image('smario_jump.png')
                    self.clip = 30
                elif self.mario_size == 'Normal':
                    if not self.flower:
                        self.image = load_image('jump_right.png')
                    else:
                        self.image = load_image('flower_jump_right.png')
                    self.clip = 18

            elif self.face_dir == -1:
                if self.mario_size == 'Small':
                    self.image = load_image('smario_jump.png')
                    self.action = 45
                    self.ch_size = 35
                    self.height = 45
                    self.clip = 30

                elif self.mario_size == 'Normal':
                    if not self.flower:
                        self.image = load_image('jump_left.png')
                    else:
                        self.image = load_image('flower_jump_left.png')
                    self.clip = 18

            if self.Y_velocity < -self.jump_height:
                self.jump = False
                self.Y_velocity = self.jump_height

        self.frame = (self.frame + 1) % self.clip
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time *self.velocity
        self.x = clamp(25, self.x, 800)

    def draw(self):
        if self.jump:
            if self.face_dir == 1 and self.mario_size == 'Small':
                self.image.clip_draw(self.frame * 35, 0, 35, 45, self.x, self.y)
            elif self.face_dir != 1 and self.mario_size == 'Small':
                self.image.clip_draw(self.frame * 35, 45, 35, 45, self.x, self.y)
            elif self.mario_size == 'Normal':
                self.image.clip_draw(self.frame * 40, 0, 40, 66, self.x, self.y)
        else:
            if self.Run and self.mario_size == 'Normal':

                self.perframe = 50
                self.action = 0
                self.height = 60

            elif self.Run and self.x_dir == 1 and self.mario_size == 'Small':

                self.perframe = 45
                self.action = 0
                self.height = 40

            elif self.Run and self.x_dir == -1 and self.mario_size == 'Small':

                self.perframe = 45
                self.action = 40
                self.height = 40

            if  not self.Run and self.x_dir == -1 and self.mario_size == 'Normal':

                self.perframe = 50
                self.action = 5
                self.height = 60

            elif not self.Run and self.x_dir == -1 and self.mario_size == 'Small':

                self.perframe = 30
                self.action = 40
                self.height = 40

            elif not self.Run and self.x_dir == 1 and self.mario_size == 'Normal':

                self.perframe = 50
                self.action = 70
                self.height = 60

            elif not self.Run and self.x_dir == 1 and self.mario_size == 'Small':

                self.perframe = 30
                self.action = 0
                self.height = 40

            self.image.clip_draw(self.frame * self.perframe, self.action , self.perframe, self.height, self.x, self.y)


class TRANS_SIZE:
    def enter(self, event):
        pass
    def exit(self):
        pass
    def do(self):
        pass
    def draw(self):
        pass
class TRANS_MARIO:
    def enter(self, event):
        pass
    def exit(self):
        pass
    def do(self):
        pass
    def draw(self):
        pass
class DIE:
    def enter(self, event):
        pass

    def exit(self):
        pass

    def do(self):
        pass

    def draw(self):
        pass

next_state = {
    IDLE: {RU: WALK, LU: WALK, RD: WALK, LD: WALK, ATTACK: IDLE, SHIFTD: IDLE, SHIFTU: IDLE,SPACE: IDLE},
    WALK: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, ATTACK: WALK, SHIFTD: WALK, SHIFTU: WALK, SPACE: WALK}

}
# class explosion:
#     def __init__(self):
#         self.image = load_image('explosion.png')
#         self.frame = 0
#         self.x = 10
#         self.y = 10
#         self.w = 30
#         self.h = 29
#         self.anim_count = 0
#
#     def update(self):
#         self.anim_count += 1
#         if self.anim_count == 4:
#             self.frame = (self.frame+1)
#             self.anim_count = 0
#         if self.frame >= 5:
#             destroy_exp()
#     def set_pos(self,x,y):
#         self.x = x
#         self.y = y
#     def draw(self):
#         self.image.clip_draw(self.frame * self.w, 0, self.w, self.h, self.x, self.y)

class mario:
    def get_name(self):
        return 'player'
    def __init__(self):
        self.image = load_image('smario_idle.png')
        self.mario_size = 'Small'
        self.frame = 0

        self.height = 0
        self.action = 0
        self.perframe = 0

        self.clip = 76
        self.x = 100
        self.y = 100 -10

        self.x_dir = 0
        self.face_dir = 1
        self.y_dir = 0

        self.velocity = 2

        self.flower = False
        self.Run = False
        self.growup = False
        self.jump = False

        self.mass = 10
        self.jump_height = 11
        self.Y_gravity = 0.5
        self.Y_velocity = self.jump_height
        self.count_grow = 0
        self.count_jump = 0

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)


    def update(self):
        self.cur_state.do(self)
        if self.event_que:
            event = self.event_que.pop()
            if event == SPACE:
                self.frame = 0
                self.jump = True
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

    def check_gameOver(self):
        if self.die:
            self.image =load_image('gameover_mario.png')
            self.clip = 13
            self.action = 0
            self.height = 60
            self.ch_size = 50

    def mario_up(self):
        self.image = load_image('mario_up.png')
        self.mario_size = 'Normal'
        self.action = 0
        self.ch_size = 40
        self.height = 80
        self.clip = 7

        self.count_grow += 1
        if self.count_grow == 4:
            self.frame = (self.frame + 1) % self.clip
            self.count_grow = 0
        if self.frame == 6:
            self.growup = False
            self.idle_right_mario()

    def draw(self):
        self.cur_state.draw(self)
    def add_event(self,event):
        self.event_que.insert(0, event)
    def handle_event(self, event):
       if(event.type, event.key) in key_event_table:
           key_event = key_event_table[(event.type, event.key)]
           self.add_event(key_event)
    def Fire_Ball(self):
        if self.flower:
            ball = Ball(self.x, self.y, self.face_dir * 3)
            game_world.add_object(ball, 1)
