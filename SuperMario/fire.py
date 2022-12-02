from pico2d import *
import game_world
import game_framework
import server

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 60.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

JUMP_SPEED_KMPH = 10.0
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)


class Ball:
    image = None
    bump_sound = None
    gen_Fire = None
    def get_name(self):
        return 'fire_ball'

    def edit_x(self, x):
        self.x -= x

    def __init__(self, x=800, y=300, dir = 1):
        if Ball.image == None:
            Ball.image = load_image('./player/fire_ball.png')
        if Ball.bump_sound == None:
            Ball.bump_sound = load_wav('./music/Bump.wav')
            Ball.bump_sound.set_volume(30)
        if Ball.gen_Fire == None:
            Ball.gen_Fire = load_wav('./music/genFire.wav')
            Ball.gen_Fire.set_volume(30)
        Ball.gen_Fire.play()
        self.x, self.y, self.dir = x, y, dir

        self.Y_velocity = 2
        self.Y_gravity = 0.25
        self.frame = 0
        self.count = 0
        self.ground = False
    def destroy(self):
        try:
            game_world.remove_object(self)
        except:
            pass
    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.Y_velocity * JUMP_SPEED_PPS * game_framework.frame_time
        self.Y_velocity -= self.Y_gravity

        if self.ground:
            self.Y_velocity = 2
            self.count += 1
            self.ground = False
        if self.y < 0:
            self.destroy()

    def draw(self):
        self.image.clip_draw(self.frame * 15, 0, 15, 13, self.x, self.y)

    def get_bb(self):
        return self.x-10, self.y-10,self.x+10, self.y+10
    def handle_collision(self, other, group, pos):
        if group == 'fire:goomba':
           pass
        if group == 'fire:red':
            pass
        if group == 'fire:ground':
            if pos == 'bottom':
                self.ground = True
            else:
                Ball.bump_sound.play()
                self.destroy()

        if group == 'fire:itembox':
            if pos == 'top':
                self.ground = True
            elif pos == 'right' or pos == 'left':
                Ball.bump_sound.play()
                self.destroy()
        if group == 'fire:bricks':
            if pos == 'top':
                self.ground = True
            elif pos == 'right' or pos == 'left':
                Ball.bump_sound.play()
                self.destroy()
        if group == 'fire:pipe':
            if pos == 'top':
                self.ground = True
            else:
                Ball.bump_sound.play()
                self.destroy()








