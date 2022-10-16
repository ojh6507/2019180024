from pico2d import *
class mario:
    def __init__(self):
        self.image = load_image('idle_right.png')

        self.frame = 0
        self.action = 0
        self.clip = 79

        self.x = 100
        self.y = 100

        self.height = 65
        self.x_dir = 0
        self.y_dir = 0
        self.ch_size = 50

        self.run = False
        self.die = False
        self.fall = False
        self.idle = True

        self. right = False
        self.left = False
        self.jump, self.on_ground = False, False
        self.curr_direct = 'Right'

        self. mass = 10
        self.t = 0.01
        self. jump_height = 15
        self.Y_gravity = 1
        self.Y_velocity = self.jump_height

        self.count_jump = 0
    def update(self):
        if self.x >= 0 and self.x <= 800:
            self.x += self.x_dir * 5
        if self.x < 0:
            self.x = 0
        elif self.x > 800:
            self.x = 800


        if self.jump:
            if self.idle:
                self.x_dir = 0
            elif self.right:
                self.x_dir = 3
            elif self.left:
                self.x_dir = -3

            self.y += self.Y_velocity
            self.Y_velocity -= self. Y_gravity
            self.count_jump += 1.8

            if self.count_jump >= 3:
                self.frame = (self.frame + 1) % self.clip
                self.count_jump = 0

            if self.curr_direct == 'Right':
                self.jump_right()
            elif self.curr_direct == 'Left':
                self.jump_left()

            if self.Y_velocity < -self.jump_height:
                self.jump = False
                self.frame = 0

                if self.idle:
                    if self.curr_direct == 'Right':
                        self.idle_right_mario()
                    elif self.curr_direct == 'Left':
                        self.idle_left_mario()

                elif self.right and not self.run:
                    self.right_mario()
                elif self.right and self.run:
                    self.run_right_mario()
                elif self.left and not self.run:
                    self.left_mario()
                elif self.left and self.run:
                    self.run_left_mario()
                self.Y_velocity = self.jump_height
        else:
            self.frame = (self.frame + 1) % self.clip

    def fall_mario(self):
        if self.fall:
            self.y -= self.y_dir *20
            self.image =load_image('fall_mario.png')
            self.height = 60
            self.ch_size = 35
            self.clip = 1
            self.action = 0
    def landing_mario(self):
            if self.y <=90:
                self.fall = False
                self.image =load_image('landing_mario.png')
                self.height = 45
                self.ch_size = 30
                self.clip = 6
                self.action = 0
                self.idle = True
    def idle_right_mario(self):
                self.image =load_image('idle_right.png')
                self.action = 5
                self.clip = 79
                self.ch_size = 50
    def idle_left_mario(self):
        self.image = load_image('idle_left.png')
        self.action = 5
        self.clip = 79
        self.ch_size = 50

    def right_mario(self):
        self.image = load_image('mario_walk.png')
        self.curr_direct = 'Right'

        self.right = True
        self.left = False
        self.idle = False

        self.action = 70
        self.x_dir = 2
        self.height = 60
        self.ch_size = 50
        self.clip = 25
        self.t = 0.01
    def left_mario(self):
        self.image = load_image('mario_walk.png')
        self.curr_direct = 'Left'

        self.action = 5
        self.x_dir = -2
        self.height = 60
        self.ch_size = 50

        self.idle = False
        self.right = False
        self.left = True

        self.clip = 25
        self.t = 0.01
    def run_right_mario(self):

        self.idle = False
        self.left = False
        self.right = True

        self.image = load_image('run_fast.png')
        self.x_dir = 4
        self.action = 0
        self.height = 60
        self.ch_size = 50
        self.t = 0.01
        self.clip = 18

    def run_left_mario(self):

            self.idle = False
            self.left = True
            self.right = False

            self.image = load_image('runfast_left.png')
            self.x_dir = -4
            self.action = 0
            self.height = 60
            self.ch_size = 50
            self.clip = 18




    def check_gameOver(self):
        if self.die:
            self.image =load_image('gameover_mario.png')
            self.clip = 13
            self.action = 0
            self.height = 60
            self.ch_size = 50

    def jump_right(self):

        self.image = load_image('jump_right.png')
        self.action = 0
        self.ch_size = 40
        self.height = 66
        self.clip = 18

    def jump_left(self):
        self.image =load_image('jump_left.png')
        self.action = 0
        self.ch_size = 40
        self.height = 66
        self.clip = 18
    def draw(self):
        self.image.clip_draw(self.frame * self.ch_size, 1* self.action, self.ch_size ,self.height,self.x,self.y)
     
    def handle_event(self):
       events = get_events()
       for event in events:
         if event.type == SDL_KEYDOWN:
             if event.key == SDLK_RIGHT:
                self.right_mario()

                if self.run:
                    self.run_right_mario()
             elif event.key == SDLK_LEFT:
                self.left_mario()
                if self.run:
                     self.run_left_mario()
             elif event.key == SDLK_LSHIFT:
                self.run = True
             elif event.key == SDLK_SPACE:
                self.jump = True
                self.frame = 0

         elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                self.idle_right_mario()
                self.x_dir = 0
                self.right = False
                self.idle = True

            elif event.key == SDLK_LEFT:
                self.idle_left_mario()
                self.x_dir = 0
                self.left = False
                self.idle = True
            elif event.key == SDLK_LSHIFT:
                self.run = False
                if self.left and self.curr_direct == "Left":
                    self.left_mario()
                elif self.right and self.curr_direct == "Right":
                    self.right_mario()