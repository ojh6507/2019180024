import random
import game_framework
import game_world
import round1
from pico2d import *
from player import character
from block import block
from monster import Goomba
from monster import Koopa
import server
import title_state
WIDTH, HEIGHT = 800,600

def setPos():

    server.itemBox[0].set_pos(900,150)
    server.itemBox[1].set_pos(900, 300)
    server.itemBox[2].set_pos(700, 150,'item')

    server.itemBox[3].set_pos(2800, 200,'item')
    server.itemBox[4].set_pos(3230, 300,'coin')
    server.itemBox[5].set_pos(10, 10)
    server.itemBox[6].set_pos(10, 10)
    server.itemBox[7].set_pos(10, 10)
    server.itemBox[8].set_pos(5800, 200,'item')
    server.itemBox[9].set_pos(6450, 150)

    server.bricks[0].set_pos(930,150)
    server.bricks[1].set_pos(870, 150)

    server.bricks[2].set_pos(2200, 300)
    server.bricks[3].set_pos(2230, 300)
    server.bricks[4].set_pos(2260, 300)
    server.bricks[5].set_pos(2290, 300)
    server.bricks[6].set_pos(2320, 300)
    server.bricks[7].set_pos(2350, 300)

    server.bricks[8].set_pos(3200,200)
    server.bricks[9].set_pos(3230,200)
    server.bricks[10].set_pos(3260, 200)

    server.bricks[11].set_pos(4160, 230)
    server.bricks[12].set_pos(4190, 230)
    server.bricks[13].set_pos(4220, 230)

    server.bricks[14].set_pos(5090, 200)
    server.bricks[15].set_pos(5120, 200)
    server.bricks[16].set_pos(5150, 200)

    server.bricks[17].set_pos(5770, 200)
    server.bricks[18].set_pos(5830, 200)
    server.bricks[19].set_pos(5860, 200)

    server.bricks[20].set_pos(6090, 200)
    server.bricks[21].set_pos(6120, 200)
    server.bricks[22].set_pos(6150, 200)
    server.bricks[23].set_pos(6180, 200)

    server.bricks[24].set_pos(6420, 150)
    server.bricks[25].set_pos(6450, 150)
    server.bricks[26].set_pos(6480, 150)


    server.stair[0].set_pos(6730, 60)
    server.stair[1].set_pos(6760, 60)
    server.stair[2].set_pos(6790, 60)
    server.stair[3].set_pos(6820, 60)
    server.stair[4].set_pos(6850, 60)
    server.stair[5].set_pos(6880, 60)
    server.stair[6].set_pos(6910, 60)
    server.stair[7].set_pos(6940, 60)

    server.stair[8].set_pos(6760, 90)
    server.stair[9].set_pos(6790, 90)
    server.stair[10].set_pos(6820, 90)
    server.stair[11].set_pos(6850, 90)
    server.stair[12].set_pos(6880, 90)
    server.stair[13].set_pos(6910, 90)
    server.stair[14].set_pos(6940, 90)

    server.stair[15].set_pos(6790, 120)
    server.stair[16].set_pos(6820, 120)
    server.stair[17].set_pos(6850, 120)
    server.stair[18].set_pos(6880, 120)
    server.stair[19].set_pos(6910, 120)
    server.stair[20].set_pos(6940, 120)

    server.stair[21].set_pos(6820, 150)
    server.stair[22].set_pos(6850, 150)
    server.stair[23].set_pos(6880, 150)
    server.stair[24].set_pos(6910, 150)
    server.stair[25].set_pos(6940, 150)

    server.stair[26].set_pos(6850, 180)
    server.stair[27].set_pos(6880, 180)
    server.stair[28].set_pos(6910, 180)
    server.stair[29].set_pos(6940, 180)

    server.stair[30].set_pos(6880, 210)
    server.stair[31].set_pos(6910, 210)
    server.stair[32].set_pos(6940, 210)

    server.stair[33].set_pos(6910, 240)
    server.stair[34].set_pos(6940, 240)


music = None

def collide(a,b):
    str = ' '

    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    # 충돌 없는 것부터 처리

    if ra - lb >= 1  and la < lb:
        str = 'right'

    if rb - la >= 1 and rb < ra:
        str = 'left'

    if ((ra - lb >= 1 and lb - la <= 20) or (rb - la <= 20 and ra - rb <= 20) or (ra <= rb and lb <= la)) and (tb - ba < 50 and ta > tb):
        str = 'bottom'

    if ((ra - lb >= 1 and lb - la <= 15) or (rb - la <= 15 and ra - rb <= 15) or (ra <= rb and lb <= la)) and (ta - bb < 20 and bb > ba):
        str = 'top'
    return True, str


def set():
    player_x, player_y = server.player.get_pos()
    world_x = server.world.get_pos()

    if world_x < (-2950) and player_x - 400 < 0:
        for game_object in game_world.all_objects():
            if game_object.get_name() != 'player':
                game_object.edit_x(player_x - 400)


    elif world_x > (-2950) and player_x - 400 > 0:
        for game_object in game_world.all_objects():
            if game_object.get_name() != 'player':
                game_object.edit_x(player_x - 400)
        server.player.edit_x(400)


    elif player_x - 400 < 0 and world_x - (player_x - 400) < 3750:
        for game_object in game_world.all_objects():
            if game_object.get_name() != 'player':
                game_object.edit_x(player_x - 400)
        server.player.edit_x(400)


def set_world():
    for col in range(len(round1.INFO)):
        for row in range(len(round1.INFO[col])):

            if round1.INFO[col][row] == 0:
                server.empty.append(round1.Empty_Tile(col, row))
                # game_world.add_object(empty,2)

            elif round1.INFO[col][row] == 1:
                server.ground.append(round1.Floor_Tile(col, row))

                # game_world.add_object(ground,3)

            elif round1.INFO[col][row] == 2:
                server.ground.append(round1.under_Tile(col, row))

                # game_world.add_object(underground,3)

cur_len = None
gposx = []
gposy = []
def enter():
    global music, gposx,gposy
    gposx += [1000,1500,2200,2260] # for debug
    gposy += [100, 100, 380, 380] # for debug

    server.world = round1.BACKGROUND()
    set_world()
    server.player = character.mario()
    # server.coin = [block.COIN() for n in range(0, 20)]
    server.itemBox = [block.item_block() for n in range(10)]
    server.bricks = [block.Bricks() for n in range(40)]
    server.stair = [block.stair_block() for n in range(35)]

    server.goomba = [Goomba.GOOMBA(gposx[i], gposy[i]) for i in range(4)]
    server.green = [Koopa.GreenKoopa() for i in range(3)]
    server.red = [Koopa.RedKoopa() for i in range(3)]
    setPos()

    game_world.add_object(server.world, 0)
    game_world.add_object(server.player, 1)
    game_world.add_objects(server.goomba, 1)
    game_world.add_objects(server.green, 1)

    game_world.add_objects(server.red, 1)
    # game_world.add_objects(server.coin, 1)
    game_world.add_objects(server.itemBox, 2)
    game_world.add_objects(server.bricks, 1)
    game_world.add_objects(server.stair, 1)
    game_world.add_objects(server.ground,3)
    game_world.add_objects(server.empty,3)

    # game_world.add_collision_group(server.player, server.coin, 'player:coin')
    game_world.add_collision_group(server.player, server.itemBox, 'player:item_block')
    game_world.add_collision_group(server.player, server.bricks, 'player:bricks')
    game_world.add_collision_group(server.player, server.ground, 'player:ground')
    game_world.add_collision_group(server.player, server.goomba, 'player:goomba')
    game_world.add_collision_group(server.player, server.red, 'player:red')
    game_world.add_collision_group(server.player, server.green, 'player:green')
    game_world.add_collision_group(server.goomba, server.ground, 'goomba:ground')
    game_world.add_collision_group(server.goomba, server.itemBox, 'goomba:itemBox')
    game_world.add_collision_group(server.goomba, server.bricks, 'goomba:bricks')
    game_world.add_collision_group(server.player, server.stair, 'player:stair')
    game_world.add_collision_group(server.green, server.ground, 'green:ground')
    game_world.add_collision_group(server.red, server.ground, 'red:ground')

    #music = load_music('stage1.mp3')
    #music.set_volume(10)
    #music.play()


def exit():
    game_world.clear()
    server.ground.clear()
    server.empty.clear()
    server.goomba.clear()

def update():
    set()
    if server.player.y < 0:
        game_framework.change_state(title_state)
    if server.player.y > 600:
        game_framework.change_state(title_state)

    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if abs(a.x - b.x) <= 100:
            if collide(a, b):
                v, p = collide(a,b)
                if v:
                    a.handle_collision(b, group, p)
                    b.handle_collision(a, group, p)

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
            server.player.handle_event(event)

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
