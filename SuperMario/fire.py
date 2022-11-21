from pico2d import *
import game_world
import game_framework
import server

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 60.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



class Ball:
    image = None

    def get_name(self):
        return 'fire_ball'

    def __init__(self, x=800, y=300, dir = 1):
        if Ball.image == None:
            Ball.image = load_image('fire_ball.png')
        self.x, self.y, self.dir = x, y, dir

        self.height = 5
        self.Y_velocity = 5
        self.Y_gravity = 1
        self.frame = 0
        self.count = 0
        self.ground = False
        self.temp_y = y - 5
    def destroy(self):
        game_world.remove_object(self)
    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.Y_velocity
        self.Y_velocity -= self.Y_gravity

        if self.ground: #타일과 충돌로 변경 예쩡
            self.Y_velocity = 5
            self.count += 1
            self.ground = False

        if self.count >= 8:
           self.destroy()

    def draw(self):
        self.image.clip_draw(self.frame * 15, 0, 15, 13, self.x, self.y)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x-10, self.y-10,self.x+10, self.y+10
    def handle_collision(self, other, group, pos):
        if group == 'fire:goomba':
           pass
        if group == 'fire:red':
            pass
        if group == 'fire:ground':
            if pos == 'bottom':
                self.ground =True
            if pos == 'right' or pos == 'left':
                self.destroy()







