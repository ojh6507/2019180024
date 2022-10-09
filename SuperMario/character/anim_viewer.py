from turtle import right
from pico2d import *

class mario:
    def __init__(self):
        self.image = load_image('idle_right.png')
        self.frame = 0
        self.action = 0
        self.clip = 79
        self.x = 400
        self.y = 90
        self.height = 65
        self.t =0.01
        self.x_dir = 0
        self.y_dir = 0
        self.ch_size = 50
    def update(self):
        self.x+= self.x_dir * 3
        self.y += self.y_dir *3
       
        self.frame= (self.frame + 1) % self.clip
        delay(self.t)
    def draw(self):
        self.image.clip_draw(self.frame * self.ch_size, 1* self.action, self.ch_size ,self.height,self.x,self.y)
     
    def mario_handle(self):
        events = get_events()
        global running
        for event in events:
         if event.type ==SDL_QUIT:
            running =False
            
         elif event.type == SDL_KEYDOWN:
             if event.key == SDLK_RIGHT:
                self.action = 70
                self.x_dir = 1
                self.height = 60
                self.ch_size = 50  
                self.image =load_image('mario_walk.png')
                self.clip = 25
                self.t = 0.01
             elif event.key == SDLK_LEFT:
                self.action = 5
                self.x_dir = -1
                self.height = 60
                self.ch_size = 50
                self.image =load_image('mario_walk.png')
                self.clip = 25
                self.t = 0.01
             elif event.key == SDLK_SPACE:
                self.image =load_image('jump_right.png')
                self.x_dir = 0
                self.y_dir = 1
                self.action = 0
                self.ch_size = 40
                self.height = 66
                self.clip = 18
                self.t = 0.03
         elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                self.image =load_image('idle_right.png')
                self.action = 5
                self.x_dir = 0
                self.height = 65
                self.clip = 79
                self.ch_size = 50  
            elif event.key == SDLK_LEFT:
                self.image =load_image('idle_left.png')
                self.action = 5
                self.x_dir = 0  
                self.height = 65         
                self.clip = 79
                self.ch_size = 50  
            elif event.key == SDLK_SPACE:
              pass
                

running = True
open_canvas(1280,1024)
player = mario()  
while running:
    clear_canvas()
    player.draw()
    player.mario_handle()
    player.update()
    update_canvas()
close_canvas()