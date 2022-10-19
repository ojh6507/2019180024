import random
from pico2d import *
from character import character
from block import block
from monster import monster

WIDTH, HEIGHT = 800,600
open_canvas(800,600)
player = character.mario()
fire = character.fire
brick_block = block.Bricks()
coin = [block.COIN() for n in range(0, 20)]

item = [block.item_block() for n in range(0, 10)]
brick = [block.Bricks() for n in range(0, 15)]

goomba = monster.GOOMBA()
green = monster.GreenKoopa()
red = monster.RedKoopa()

def setPos_coin():
    global coin
    for c in coin:
        c.set_pos(random.randint(400, 10000),random.randint(75, 200))
    for it in item:
        it.set_pos(random.randint(400, 10000),random.randint(200, 300))
    for br in brick:
        br.set_pos(random.randint(400, 10000), random.randint(200, 300))

class background:
    def __init__ (self):
        self.image = load_image('background_2.png')
        self.background_x = 3750
        self.dir = 0
    def draw (self):
        self.image.draw(self.background_x, 500)
    def update(self):
        global  player
        if self.background_x < (-2950):
            if player.x - 400 < 0:
                self.background_x -= (player.x - 400)
                goomba.x -= player.x - 400
                green.x -= player.x - 400
                red.x -= player.x - 400
                for c in coin:
                    c.x -= player.x - 400
                for it in item:
                    it.x -= player.x - 400
                for br in brick:
                    br.x -= player.x - 400
                for f in fire:
                    f.x -= player.x - 400

                player.x = 400


            pass
        elif player.x - 400 > 0:
            self.background_x -= (player.x - 400)
            goomba.x -= player.x - 400
            green.x -= player.x - 400
            red.x -= player.x - 400
            for c in coin:
                c.x -=player.x - 400
            for it in item:
                it.x -= player.x - 400
            for br in brick:
                br.x -= player.x - 400
            #for f in fire:
             #   f.x -=player.x - 400

            player.x = 400


        elif player.x - 400 < 0:
            if self.background_x - (player.x - 400) < 3750:
                self.background_x -= (player.x - 400)
                goomba.x -= player.x - 400
                green.x -= player.x - 400
                red.x -= player.x - 400
                for c in coin:
                    c.x -= player.x - 400
                for it in item:
                    it.x -= player.x - 400
                for br in brick:
                    br.x -= player.x - 400
                #for f in fire:
                 #   f.x -= player.x - 400

                player.x = 400


world = background()

def draw_world():
    world.draw()
    world.update()

setPos_coin()

while(character.running):

    startTick = SDL_GetTicks()
    clear_canvas()
    draw_world()
    for c in coin:
        c.draw()
        c.update()
    for it in item:
        it.draw()
        it.update()
    for br in brick:
        br.draw()
        br.update()

    player.draw()
    player.handle_event()
    player.update()

    red.draw()
    red.update()
    green.draw()
    green.update()
    goomba.draw()
    goomba.update()

    update_canvas()
    delay_time = 1000/60 - (SDL_GetTicks() - startTick)
    if delay_time > 0:
        delay(0.02)

close_canvas()