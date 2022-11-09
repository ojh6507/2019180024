import random
import game_framework
import game_world
import round1
from pico2d import *
from player import character
from player import *
from block import block
from monster import Goomba
from monster import Koopa
WIDTH, HEIGHT = 800,600

def setPos_coin():
    global coin
    for c in coin:
        c.set_pos(random.randint(400, 10000),random.randint(75, 200))
    for it in item:
        it.set_pos(random.randint(400, 10000),random.randint(200, 300))
    for br in brick:
        br.set_pos(random.randint(400, 10000), random.randint(200, 300))


world = None
player = None
fire = None
exp = None
brick_block = None
coin = None
item = None
brick = None
goomba = None
green = None
red = None
music = None

def check_collide(a, b):

    top_a, bottom_a, left_a, right_a = a.get_rect()
    top_b, bottom_b, left_b, right_b = b.get_rect()

    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    if left_a > right_b: return False
    if right_a < left_b: return False

    return True


def set():
    global world, player
    if world.x < (-2950):
        if player.x - 400 < 0:
            for game_object in game_world.all_objects():
                if game_object.get_name() != 'player':
                    game_object.x -= (player.x - 400)


    elif player.x - 400 > 0:
        for game_object in game_world.all_objects():
            if game_object.get_name() != 'player':
                game_object.x -= (player.x - 400)
        player.x = 400





    elif player.x - 400 < 0 :
        if world.x - (player.x - 400) < 3750:
            for game_object in game_world.all_objects():
                if game_object.get_name() != 'player':
                    game_object.x -= (player.x - 400)

            player.x = 400




def enter():
    global world, player,fire,brick_block,\
        coin,item,brick,goomba,green,red,exp,music
    world = round1.BACKGROUND()
    round1.set_world()
    player = character.mario()

    brick_block = block.Bricks()
    coin = [block.COIN() for n in range(0, 20)]
    item = [block.item_block() for n in range(0, 10)]
    brick = [block.Bricks() for n in range(0, 15)]

    goomba = Goomba.GOOMBA()
    green = Koopa.GreenKoopa()
    red = Koopa.RedKoopa()
    setPos_coin()

    game_world.add_object(world, 0)
    game_world.add_object(player, 1)
    game_world.add_object(goomba, 1)
    game_world.add_object(green, 1)
    game_world.add_object(green, 1)
    game_world.add_objects(coin, 1)
    game_world.add_objects(item, 1)
    game_world.add_objects(brick, 1)

    #music = load_music('stage1.mp3')
    #music.set_volume(10)
    #music.play()


def exit():
    game_world.clear()
def update():
    set()
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player.handle_event(event)

def pause():
    pass
def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas(800,600)
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__': # 단독 실행이면
    test_self()
