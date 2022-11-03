from pico2d import *
import math
import game_framework

RD, LD, RU, LU, SPACE, ATTACK, SHIFTD = range(7)
event_name = ['RD', 'LD', 'RU', 'LU', 'JUMP', 'ATTACK']
key_event_table = {
(SDL_KEYDOWN, SDLK_SPACE): SPACE,
(SDL_KEYDOWN, SDLK_LSHIFT): SHIFTD,
(SDL_KEYDOWN, SDLK_RIGHT): RD,
(SDL_KEYDOWN, SDLK_LEFT): LD,
(SDL_KEYDOWN, SDLK_z): ATTACK,
(SDL_KEYUP, SDLK_RIGHT): RU,
(SDL_KEYUP, SDLK_LEFT): LU
}

class IDLE:
    def enter(self, event):
        print('Enter IDLE')
        self.x_dir = 0
        self.Run = False

        pass

    def exit(self, event):
        print('Exit IDLE')
        pass

    def do(self):
        print('Do IDLE')


        if self.mario_size == 'Small':
            self.image = load_image('smario_idle.png')
            self.clip = 76
        elif self.mario_size == 'Normal':
            self.clip = 79
            if not self.flower:
                self.image = load_image('idle_right.png')
            else:
                self.image = load_image('flower_idle_right.png')
        self.frame = (self.frame + 1) % self.clip

    def draw(self):
        print('Draw IDLE')
        if self.face_dir == 1 and self.mario_size == 'Small':
            self.image.clip_draw(self.frame * 30,  0, 30, 35, self.x, self.y)
        elif self.face_dir == 1 and self.mario_size == 'Normal':
            self.image.clip_draw(self.frame * 50, 5, 50, 60, self.x, self.y)
        elif self.face_dir != 1 and self.mario_size == 'Small':
            self.image.clip_draw(self.frame * 30, 38, 30, 35, self.x, self.y)
        elif self.face_dir != 1 and self.mario_size == 'Normal':
            self.image.clip_draw(self.frame * 50, 5, 50, 65, self.x, self.y)

        pass

class JUMP:
    def enter(self, event):
        print('Enter Jump')
        pass
    def exit(self, event):
        print('Exit Jump')
        pass
    def do(self):
        print('Do Jump')
        pass
    def draw(self):
        print('Draw Jump')
        pass

    def draw(self):
        print('Draw Run')
        if self.x_dir == -1 and self.mario_size == 'Normal':
            self.image.clip_draw(self.frame * 50, 1 * 5, 50, 60, self.x, self.y)
        elif self.x_dir == -1 and self.mario_size == 'Small':
            self.image.clip_draw(self.frame * 30, 1 * 40, 30, 40, self.x, self.y)
        elif self.x_dir == 1 and self.mario_size == 'Normal':
            self.image.clip_draw(self.frame * 50, 1 * 70, 50, 60, self.x, self.y)
        elif self.x_dir == 1 and self.mario_size == 'Small':
            self.image.clip_draw(self.frame * 30, 1 * 0, 30, 40, self.x, self.y)


class WALK:
    def enter(self, event):
        print('Enter Run')
        if event == RD:
            self.x_dir += 1
        elif event == LD:
            self.x_dir -= 1
        elif event == RU:
            self.x_dir -= 1
        elif event == LU:
            self.x_dir += 1
    def exit(self,event):
        print('Exit Run')
        if event == SHIFTD:
            self.Run = True
        else:
            self.Run = False

        self.face_dir = self.x_dir
    def do(self):
        print('Do Run')
        if self.Run:
            self.velocity = 2
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

        else:
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



        self.frame = (self.frame + 1) % self.clip
        self.x += self.x_dir* 2 * self.velocity

        pass
    def draw(self):
        print('Draw Run')
        if self.Run:
            if self.mario_size == 'Normal':
                self.image.clip_draw(self.frame * 50, 0, 50, 60, self.x, self.y)
            elif self.x_dir == 1 and self.mario_size == 'Small':
                self.image.clip_draw(self.frame * 45, 0, 45, 40, self.x, self.y)
            elif self.x_dir == -1 and self.mario_size == 'Small':
                self.image.clip_draw(self.frame * 45, 40, 45, 40, self.x, self.y)
        else:
            if self.x_dir == -1 and self.mario_size == 'Normal':
                self.image.clip_draw(self.frame * 50, 1 * 5, 50, 60, self.x, self.y)
            elif self.x_dir == -1 and self.mario_size == 'Small':
                self.image.clip_draw(self.frame * 30, 1 * 40, 30, 40, self.x, self.y)
            elif self.x_dir == 1 and self.mario_size == 'Normal':
                self.image.clip_draw(self.frame * 50, 1 * 70, 50, 60, self.x, self.y)
            elif self.x_dir == 1 and self.mario_size == 'Small':
                self.image.clip_draw(self.frame * 30, 1 * 0, 30, 40, self.x, self.y)

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
    IDLE: {RU: WALK, LU: WALK, RD: WALK, LD: WALK, ATTACK: IDLE, SPACE: JUMP, SHIFTD: IDLE},
    WALK: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, ATTACK: WALK, SPACE: JUMP, SHIFTD: WALK},
    JUMP: {RU: JUMP, LU: JUMP, RD: JUMP, LD: JUMP, ATTACK: JUMP, SPACE: JUMP, SHIFTD: JUMP}
}
class explosion:
    def __init__(self):
        self.image = load_image('explosion.png')
        self.frame = 0
        self.x = 10
        self.y = 10
        self.w = 30
        self.h = 29
        self.anim_count = 0

    def update(self):
        self.anim_count += 1
        if self.anim_count == 4:
            self.frame = (self.frame+1)
            self.anim_count = 0
        if self.frame >= 5:
            destroy_exp()
    def set_pos(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        self.image.clip_draw(self.frame * self.w, 0, self.w, self.h, self.x, self.y)

class fire_ball:
    def __init__(self):
        self.image = load_image('fire_ball.png')
        self.x = 0
        self.y = 0
        self.w = 15
        self.h = 13
        self.height = 5
        self.Y_velocity = 5
        self.Y_gravity = 1
        self.frame = 0
        self.anim_count = 0
        self.direction = None
        self.temp_y = 10
        self.count = 0
    def set_pos(self,x,y):
        self.x = x
        self.y = y
        self.temp_y = y -5

    def set_dir(self,dir):
        self.direction = dir
    def update(self):
        self.anim_count += 1

        if self.anim_count == 3:
            self.frame = (self.frame + 1) % 4
            self.anim_count = 0
        if self.direction  == 'Right':
            self.x += 10

        elif self.direction == 'Left':
            self.x -= 10

        self.y += self.Y_velocity
        self.Y_velocity -= self.Y_gravity
        if self.y < 90:
            self.Y_velocity = 5
            self.count+= 1
        if self.count == 3:
           self.count = 0
           destroy_fire()
    def draw(self):
        self.image.clip_draw(self.frame * self.w, 0, self.w, self.h, self.x,self.y)


fire = []
exp = []
def destroy_fire():
    exp.append(explosion())
    exp[len(exp)-1].set_pos(fire[0].x, fire[0].y)

    del fire[0]
def destroy_exp():
    del exp[0]


class mario:
    def __init__(self):
        self.image = load_image('smario_idle.png')
        self.mario_size = 'Small'


        self.frame = 0
        self.action = 0
        self.clip = 76

        self.x = 100
        self.y = 100 -10
        self.flower = False

        #self.height = 65
        self.height = 35
        self.x_dir = 0
        self.face_dir = 1
        self.y_dir = 0

        #self.ch_size = 50
        self.ch_size = 30
        self. veocity = 2

        self.Run = False
        self.die = False
        self.fall = False
        self.idle = True
        self. right = False
        self.left = False
        self.growup = False

        self.jump, self.on_ground = False, False
        self.curr_direct = 'Right'

        self. mass = 10
        self.t = 0.01
        self. jump_height = 22
        self.Y_gravity = 2
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
            self.cur_state.exit(self,event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('Error: ', self.cur_state.__name__,' ', event_name[event])

            self.cur_state.enter(self, event)

        #
        # for i in fire:
        #     i.update()
        # for ex in exp:
        #     ex.update()
        # if self.x >= 0 and self.x <= 800:
        #     self.x += self.x_dir * 5
        # if self.x < 0:
        #     self.x = 0
        # elif self.x > 800:
        #     self.x = 800
        #
        # if self.jump:
        #    self.jump_mario()
        # elif self.growup:
        #     self.mario_up()
        # else:
        #     self.frame = (self.frame + 1) % self.clip
        # self.positionRect = SDL_Rect(int(self.x), int(self.y), int(self.ch_size), int(self.height))

    # def jump_mario(self):
    #     if self.idle:
    #         self.x_dir = 0
    #     elif self.right:
    #         self.x_dir = 1.5
    #     elif self.left:
    #         self.x_dir = -1.5
    #     if self.run:
    #         if self.right:
    #             self.x_dir += .5
    #         elif self.left:
    #             self.x_dir -= .5
    #     self.y += self.Y_velocity
    #     self.Y_velocity -= self.Y_gravity
    #     self.frame = (self.frame + 1) % self.clip
    #
    #     if self.curr_direct == 'Right':
    #         self.jump_right()
    #     elif self.curr_direct == 'Left':
    #         self.jump_left()
    #
    #     if self.Y_velocity < -self.jump_height:
    #         self.jump = False
    #         self.frame = 0
    #
    #         if self.idle:
    #             if self.curr_direct == 'Right':
    #                 self.idle_right_mario()
    #             elif self.curr_direct == 'Left':
    #                 self.idle_left_mario()
    #
    #         elif self.right and not self.run:
    #             self.right_mario()
    #         elif self.right and self.run:
    #             self.run_right_mario()
    #         elif self.left and not self.run:
    #             self.left_mario()
    #         elif self.left and self.run:
    #             self.run_left_mario()
    #         self.Y_velocity = self.jump_height
    # # def fall_mario(self):
    #     if self.fall:
    #         self.y -= self.y_dir *20
    #         self.image = load_image('fall_mario.png')
    #         self.height = 60
    #         self.ch_size = 35
    #         self.clip = 1
    #         self.action = 0

    def run_left_mario(self):

            self.idle = False
            self.left = True
            self.right = False


    def check_gameOver(self):
        if self.die:
            self.image =load_image('gameover_mario.png')
            self.clip = 13
            self.action = 0
            self.height = 60
            self.ch_size = 50

    def jump_right(self):
        if self.mario_size == 'Small':
            self.image = load_image('smario_jump.png')
            self.action = 0
            self.ch_size = 35
            self.height = 45
            self.clip = 30
        elif self.mario_size == 'Normal':
            if not self.flower:
                self.image = load_image('jump_right.png')
            else:
                self.image = load_image('flower_jump_right.png')

            self.action = 0
            self.ch_size = 40
            self.height = 66
            self.clip = 18

    def jump_left(self):
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
            self.action = 0
            self.ch_size = 40
            self.height = 66
            self.clip = 18
    def mario_up(self):
        self.image = load_image('mario_up.png')
        self.mario_size = 'Normal'
        self.action = 0
        self.ch_size = 40
        self.height = 80
        self.clip = 7

        self.count_grow+=1
        if self.count_grow == 4:
            self.frame = (self.frame + 1) % self.clip
            self.count_grow = 0
        if self.frame == 6:
            self.growup = False
            self.idle_right_mario()

    def draw(self):
        self.cur_state.draw(self)
    #
    #
    #     for i in fire:
    #         i.draw()
    #     for ex in exp:
    #         ex.draw()
    def add_event(self,event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
       if(event.type, event.key) in key_event_table:
           key_event = key_event_table[(event.type, event.key)]
           self.add_event(key_event)
