import random
from pico2d import *
from character import character
from block import block
from monster import monster
import game_framework
WIDTH, HEIGHT = 800,600

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


world = None
player = None
fire = None
brick_block = None
coin = []
item = []
brick = []
goomba = None
green = None
red = None


def draw_world():
    world.draw()
    player.draw()

def enter():
    global world, player,fire,brick_block,coin,item,brick,goomba,green,red
    world = background()
    player = character.mario()
    fire = character.fire
    brick_block = block.Bricks()
    coin = [block.COIN() for n in range(0, 20)]
    item = [block.item_block() for n in range(0, 10)]
    brick = [block.Bricks() for n in range(0, 15)]
    goomba = monster.GOOMBA()
    green = monster.GreenKoopa()
    red = monster.RedKoopa()
    setPos_coin()

def exit():
    global world, player, fire, brick_block, coin, item, brick, goomba, green, red
    del world
    del player
    for one_fire in fire:
        del one_fire
    for one_coin in coin:
        del one_coin
    for one_item in item:
        del one_item
    for one_brick in brick:
        del one_brick

    del goomba
    del green
    del red
def update():
    startTick = SDL_GetTicks()

    world.update()
    player.update()
    for c in coin:
        c.update()
    for it in item:
        it.update()
    for br in brick:
        br.update()
    red.update()
    green.update()
    goomba.update()

    delay_time = 1000 / 60 - (SDL_GetTicks() - startTick)
    if delay_time > 0:
        delay(0.02)


def draw():
    clear_canvas()
    draw_world()
    for c in coin:
        c.draw()
    for it in item:
        it.draw()
    for br in brick:
        br.draw()
    red.draw()
    green.draw()
    goomba.draw()
    update_canvas()

def handle_events():
    player.handle_event()

def pause():
    pass
def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__': # 단독 실행이면
    test_self()
