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
import stage_clear
import gameOver


def setPos():

    server.itemBox[0].set_pos(900,200)
    server.itemBox[1].set_pos(900, 350)
    server.itemBox[2].set_pos(700, 200,'item')
    server.itemBox[3].set_pos(2800, 200,'item')
    server.itemBox[4].set_pos(3230, 300,'coin')
    server.itemBox[5].set_pos(10, 10)
    server.itemBox[6].set_pos(10, 10)
    server.itemBox[7].set_pos(10, 10)
    server.itemBox[8].set_pos(5800, 200,'item')
    server.itemBox[9].set_pos(6450, 200)

    server.bricks[0].set_pos(930, 200)
    server.bricks[1].set_pos(870, 200)
    server.bricks[2].set_pos(2200, 300)
    server.bricks[3].set_pos(2230, 300)
    server.bricks[4].set_pos(2260, 300)
    server.bricks[5].set_pos(2290, 300)
    server.bricks[6].set_pos(2320, 300)
    server.bricks[7].set_pos(2350, 300)

    server.bricks[8].set_pos(3200,200,'solid')
    server.bricks[9].set_pos(3230,200)
    server.bricks[10].set_pos(3260, 200,'solid')
    server.bricks[11].set_pos(4160, 230)
    server.bricks[12].set_pos(4190, 230)
    server.bricks[13].set_pos(4220, 230)

    server.bricks[14].set_pos(5090, 200)
    server.bricks[15].set_pos(5120, 200,'solid')
    server.bricks[16].set_pos(5150, 200,'solid')
    server.bricks[17].set_pos(5770, 200,'solid')
    server.bricks[18].set_pos(5830, 200)
    server.bricks[19].set_pos(5860, 200)

    server.bricks[20].set_pos(6090, 250,'solid')
    server.bricks[21].set_pos(6120, 250)
    server.bricks[22].set_pos(6150, 250)
    server.bricks[23].set_pos(6180, 250)
    server.bricks[24].set_pos(6420, 200)
    server.bricks[25].set_pos(6480, 200)
    server.bricks[26].set_pos(6510, 200)


    server.goomba[0].set_pos(1000, 200)
    server.goomba[1].set_pos(1500, 200)
    server.goomba[2].set_pos(2200, 430)
    server.goomba[3].set_pos(2260, 430)
    server.goomba[4].set_pos(5800, 260)

    server.red[0].set_pos(1750, 80)
    server.red[1].set_pos(3500, 80)
    server.red[2].set_pos(5000, 80)
    server.red[3].set_pos(3960, 400)


    server.coin[0].set_pos(1500, 200)
    server.coin[1].set_pos(1530, 200)
    server.coin[2].set_pos(1560, 200)

    server.coin[3].set_pos(1900, 200)
    server.coin[4].set_pos(1930, 200)
    server.coin[5].set_pos(1960, 200)

    server.coin[6].set_pos(2460, 150)
    server.coin[7].set_pos(2490, 150)
    server.coin[8].set_pos(2520, 150)

    server.coin[9].set_pos(4750, 200)
    server.coin[10].set_pos(4780, 200)
    server.coin[11].set_pos(4810, 200)

    server.coin[12].set_pos(5380, 200)
    server.coin[13].set_pos(5410, 200)
    server.coin[14].set_pos(5440, 200)

    server.coin[15].set_pos(6100, 60)
    server.coin[16].set_pos(6130, 60)
    server.coin[17].set_pos(6160, 60)
    server.coin[18].set_pos(6190, 60)
    server.coin[19].set_pos(6220, 60)

    server.green[0].set_pos(2500, 150)
    server.green[1].set_pos(3000, 110)
    server.green[2].set_pos(4000, 400)
    server.green[3].set_pos(6300, 110)

def collide(a,b):
    str = ' '

    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False


    if abs(a.x - b.x) < 12 and a.y < b.y:
        str = 'top'
    elif abs(a.y - b.y) < 72 and a.x < b.x:
        str = 'right'
    elif abs(a.y - b.y) < 70 and a.x > b.x:
        str = 'left'
    if a.y > tb or ba >= tb:
        str = 'bottom'

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

            if round1.INFO[col][row] == -1:
                server.empty.append(round1.Empty_Tile(col, row))

            elif round1.INFO[col][row] == 1:
                server.ground.append(round1.Floor_Tile(col, row))

            elif round1.INFO[col][row] == 2:
                server.ground.append(round1.under_Tile(col, row))

def enter():
    server.world = round1.BACKGROUND()
    set_world()
    server.player = character.mario()
    pipe = block.Pipe()
    pipe.activate = True

    server.coin = [block.COIN() for n in range(0, 20)]
    server.itemBox = [block.item_block() for n in range(10)]
    server.bricks = [block.Bricks() for n in range(40)]
    server.goomba = [Goomba.GOOMBA() for i in range(5)]
    server.green = [Koopa.GreenKoopa() for i in range(4)]
    server.red = [Koopa.RedKoopa() for i in range(4)]

    setPos()

    game_world.add_object(server.world, 0)
    game_world.add_object(server.player, 1)
    game_world.add_objects(server.goomba, 1)
    game_world.add_objects(server.green, 1)
    game_world.add_object(pipe, 3)

    game_world.add_objects(server.red, 1)
    game_world.add_objects(server.coin, 2)
    game_world.add_objects(server.itemBox, 2)
    game_world.add_objects(server.bricks, 1)
    game_world.add_objects(server.ground, 3)
    game_world.add_objects(server.empty, 3)

    game_world.add_collision_group(server.player, server.coin, 'player:coin')
    game_world.add_collision_group(server.player, server.itemBox, 'player:item_block')
    game_world.add_collision_group(server.player, server.bricks, 'player:bricks')
    game_world.add_collision_group(server.player, server.ground, 'player:ground')
    game_world.add_collision_group(server.player, server.goomba, 'player:goomba')
    game_world.add_collision_group(server.player, server.red, 'player:red')
    game_world.add_collision_group(server.player, server.green, 'player:green')
    game_world.add_collision_group(server.goomba, server.ground, 'goomba:ground')
    game_world.add_collision_group(server.goomba, server.itemBox, 'goomba:itemBox')
    game_world.add_collision_group(server.goomba, server.bricks, 'goomba:bricks')
    game_world.add_collision_group(server.green, server.ground, 'green:ground')
    game_world.add_collision_group(server.red, server.ground, 'red:ground')
    game_world.add_collision_group(server.red, server.empty, 'red:empty')
    game_world.add_collision_group(server.player, pipe, 'player:pipe')

    game_world.add_collision_group(None, server.ground, 'fire:ground')
    game_world.add_collision_group(server.goomba, None,'fire:goomba')
    game_world.add_collision_group(server.red, None, 'fire:red')
    game_world.add_collision_group(server.green, None, 'fire:green')
    game_world.add_collision_group(server.itemBox, None, 'fire:itembox')
    game_world.add_collision_group(server.bricks, None, 'fire:bricks')
    game_world.add_collision_group(pipe, None, 'fire:pipe')

    # game_world.add_collision_group(server.player, server.stair, 'player:stair')


def exit():
    game_world.clear()

    server.world = None
    server.coin.clear()
    server.itemBox.clear()
    server.goomba.clear()
    server.red.clear()
    server.green.clear()
    server.ground.clear()
    server.bricks.clear()
    server.empty.clear()
    server.pipes.clear()

    server.ground.clear()
    server.empty.clear()
    server.goomba.clear()

def update():
    set()
    if server.player.y < 0:
        server.min_health = -1
        game_framework.change_state(gameOver)
        print('gameover')
    if server.player.y > 700:
        server.min_health = 0
        server.stage_info = 2
        game_framework.change_state(stage_clear)
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if abs(a.x - b.x) <= 110:
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
