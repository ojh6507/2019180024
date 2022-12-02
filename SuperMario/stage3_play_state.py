import game_framework
import game_world
import round3
from pico2d import *
from player import character
from block import block
import server
import all_stage_clear
import gameOver
from monster import boss


def collide(a,b):
    str = ' '

    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    if a.y > tb:
        str = 'bottom'
    elif abs(a.y - b.y) < 70 and a.x < b.x:
        str = 'right'
    elif abs(a.y - b.y) < 70 and a.x > b.x:
        str = 'left'

    return True, str



def set_world():
    for col in range(len(round3.INFO)):
        for row in range(len(round3.INFO[col])):
            if round3.INFO[col][row] == 1:
                server.ground.append(round3.Floor_Tile(col, row))


def enter():
    global music
    set_world()
    server.world = round3.BACKGROUND()
    server.player = character.mario()
    server.player.flower = True
    server.player.mario_size = 'Normal'
    server.player.jump_height = 13
    server.bowser = boss.BOSS()
    server.door = block.Door()

    game_world.add_object(server.bowser, 1)
    game_world.add_object(server.world, 0)
    game_world.add_object(server.player, 1)
    game_world.add_objects(server.ground,1)
    game_world.add_object(server.door, 0)

    game_world.add_collision_group(server.player, server.ground, 'player:ground')
    game_world.add_collision_group(server.bowser, server.ground, 'bowser:ground')
    game_world.add_collision_group( None, server.ground, 'fire:ground')

    game_world.add_collision_group(server.player, server.bowser, 'player:bowser')
    game_world.add_collision_group(None, server.bowser, 'fire:bowser')
    game_world.add_collision_group(server.player, server.door, 'player:door')


def exit():
    game_world.clear()
    server.world = None

def update():
    server.player.y = clamp(65, server.player.y, 800)
    if server.player.die:
        game_framework.change_state(gameOver)
    if server.player.y > 700 or server.curr_stage == 4:
        server.stage_info = 3
        game_framework.change_state(all_stage_clear)
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if abs(a.x - b.x) <= 95:
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
