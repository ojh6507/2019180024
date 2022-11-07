from pico2d import *
class FIRE:
    image = None

    def get_name(self):
        return 'fire_ball'

    def __init__(self,x = 800,y = 300, velocity = 1):
        if FIRE.image == None:
            FIRE.image = load_image('fire_ball.png')

            self.x, self.y = x,y
            self.w = 15
            self.h = 13
            self.height = 5
            self.Y_velocity = 5
            self.Y_gravity = 1
            self.frame, self.anim_count, self.count = 0
            self.direction = None
            self.temp_y = 10

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.temp_y = y - 5

    def set_dir(self, dir):
        self.direction = dir

    def update(self):
        self.anim_count += 1
        if self.anim_count == 3:
            self.frame = (self.frame + 1) % 4
            self.anim_count = 0
        if self.direction == 'Right':
            self.x += 10

        elif self.direction == 'Left':
            self.x -= 10

        self.y += self.Y_velocity
        self.Y_velocity -= self.Y_gravity
        if self.y < 90:
            self.Y_velocity = 5
            self.count += 1
        if self.count == 3:
            self.count = 0

    def draw(self):
        self.image.clip_draw(self.frame * self.w, 0, self.w, self.h, self.x, self.y)




