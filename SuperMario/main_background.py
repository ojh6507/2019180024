from pico2d import*
import numpy as np
import game_world

class BACKGROUND:
    def get_name(self):
        return 'background'
    def __init__ (self):
        self.image = load_image('background/title_background.png')
        self.x = 3750
    def edit_x(self,x):
        self.x = x
    def get_pos(self):
        return self.x
    def draw (self):
        self.image.draw(self.x, 500)
    def update(self):
        pass
