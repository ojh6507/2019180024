from pico2d import *
import pygame
class mario:
    def __init__(self):
        self.image = load_image('idle_right.png')
        self.rect = self.image.get_rect()

        self.frame = 0
        self.action = 0
        self.clip = 79

        self.x = 100
        self.y = 110

        self.height = 65
        self.x_dir = 0
        self.y_dir = 0
        self.ch_size = 50
  
        self.run = False
        self.die = False
        self.fall = False
        self.idle = False
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = .35, -.12

        self.position = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)

        self.acceleration = pygame.math.Vector2(0, self.gravity)

        self. mass = 10
        self.t =0.01
  

    def update(self, dt):
        # if self.x >= 0 and self.x <= 800:
        #     self.x += self.x_dir * 4

        if self.x < 0:
            self.x = 0
        elif self.x > 800:
            self.x = 800
        self.frame = (self.frame + 1) % self.clip
        delay(0.01)
        self.horizontal_movement(dt)
        self.vertical_movement(dt)

    def horizontal_movement(self,dt):
        self.acceleration.x = 0
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False

            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.action = 70
                    self.acceleration += .3
                    self.height = 60
                    self.ch_size = 50

                    self.image = load_image('mario_walk.png')
                    self.clip = 25
                    self.t = 0.01
                    self.forward = True

                    if self.run:
                        self.image = load_image('run_fast.png')
                        self.acceleration += .6
                        self.action = 0
                        self.height = 60
                        self.ch_size = 50
                        self.t = 0.01
                        self.clip = 18

                elif event.key == SDLK_LEFT:
                    self.action = 5
                    self.acceleration -= .3

                    self.height = 60
                    self.ch_size = 50
                    self.image = load_image('mario_walk.png')
                    self.clip = 25
                    self.t = 0.01
                    self.forward = True

                    if self.run:
                        self.image = load_image('runfast_left.png')
                        self.acceleration -= .6

                        self.action = 0
                        self.height = 60
                        self.ch_size = 50
                        self.t = 0.01
                        self.clip = 18
                elif event.key == SDLK_LSHIFT:
                    self.run = True

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.image = load_image('idle_right.png')
                    self.action = 5
                    self.acceleration = 0

                    self.height = 65
                    self.clip = 79
                    self.ch_size = 50
                    self.forward = False
                elif event.key == SDLK_LEFT:
                    self.image = load_image('idle_left.png')
                    self.acceleration = 0

                    self.action = 5
                    self.height = 65
                    self.clip = 79
                    self.ch_size = 50
                elif event.key == SDLK_LSHIFT:
                    self.run = False
        self.acceleration +=self.velocity.x*self.friction
        self.velocity.x += self.acceleration.x *dt
        self.limit_velocity(4)
        self.position.x += self.velocity.x * dt +(self.acceleration.x * 5) * (dt * dt)
        self.rect.x = self.position.x
    def vertical_movement(self, dt):
        self.velocity.y += self.accerlation.y * dt
        if self.velocity.y > 7: self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt*dt)
        if self.position.y > 128:
            self.on_ground = True
            self.velocity.y = 0
            self.position.y = 128
    def limit_velocity(self, max_vel):
        min(-max_vel, max(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01: self.velocity.x = 0
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
    def idle_mario(self):
                self.image =load_image('idle_right.png')
                self.action = 5
                self.x_dir = 0
                self.height = 65
                self.clip = 79
                self.ch_size = 50
                self.idle = False
    def check_gameOver(self):
        if self.die:
            self.image =load_image('gameover_mario.png')
            self.clip = 13
            self.action = 0
            self.height = 60
            self.ch_size = 50
            self.t = 0.02
    def jump_right(self):
        self.image =load_image('jump_right.png')
        self.x_dir = 0
        self.y_dir = 1
        self.action = 0
        self.ch_size = 40
        self.height = 66
        self.clip = 18
        self.t = 0.03
        self.jump = True

    def draw(self):
        self.image.clip_draw(self.frame * self.ch_size, 1* self.action, self.ch_size ,self.height,self.position.x,self.position.y)
     
    # def handle_event(self):
       # events = get_events()
       # for event in events:
       #   if event.type ==SDL_QUIT:
       #          running =False
       #
       #   elif event.type == SDL_KEYDOWN:
       #       if event.key == SDLK_RIGHT:
       #          self.action = 70
       #          self.x_dir = 1
       #          self.height = 60
       #          self.ch_size = 50
       #          self.image =load_image('mario_walk.png')
       #          self.clip = 25
       #          self.t = 0.01
       #          self.forward = True
       #          if self.run:
       #               self.image = load_image('run_fast.png')
       #               self.x_dir = 2
       #               self.action = 0
       #               self.height = 60
       #               self.ch_size = 50
       #               self.t = 0.01
       #               self.clip = 18
       #
       #       elif event.key == SDLK_LEFT:
       #          self.action = 5
       #          self.x_dir = -1
       #          self.height = 60
       #          self.ch_size = 50
       #          self.image =load_image('mario_walk.png')
       #          self.clip = 25
       #          self.t = 0.01
       #          self.forward = True
       #
       #          if self.run:
       #               self.image = load_image('runfast_left.png')
       #               self.x_dir = -2
       #               self.action = 0
       #               self.height = 60
       #               self.ch_size = 50
       #               self.t = 0.01
       #               self.clip = 18
       #       elif event.key == SDLK_LSHIFT:
       #          self.run = True
       #       elif event.key == SDLK_SPACE:
       #          pass
       #   elif event.type ==SDL_KEYUP:
       #      if event.key == SDLK_RIGHT:
       #          self.image =load_image('idle_right.png')
       #          self.action = 5
       #          self.x_dir = 0
       #          self.height = 65
       #          self.clip = 79
       #          self.ch_size = 50
       #          self.forward = False
       #      elif event.key == SDLK_LEFT:
       #          self.image =load_image('idle_left.png')
       #          self.action = 5
       #          self.x_dir = 0
       #          self.height = 65
       #          self.clip = 79
       #          self.ch_size = 50
       #      elif event.key == SDLK_LSHIFT:
       #          self.run = False
       #      elif event.key == SDLK_SPACE:
       #          self.jump =False
