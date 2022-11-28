import random
import game_framework
import game_world
import world_menu
from pico2d import *
from player import character
import server
import title_state
WIDTH, HEIGHT = 800, 600

music = None

def collide(a,b):
    str = ' '

    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    if ra >= lb and la <= lb:
        str = 'right'
    elif rb >= la and rb <= ra:
        str = 'left'

    if ((ra - lb >= 1 and lb - la <= 50) or (rb - la >= 1 and ra - rb <= 50) or (ra <= rb and lb <= la)) and (tb >= ba and ta > tb):
        str = 'bottom'
    elif ((ra - lb >= 1 and lb - la <= 15) or (rb - la <= 15 and ra - rb <= 15) or (ra <= rb and lb <= la)) and (ta - bb < 20 and bb > ba):
        str = 'top'


    return True, str

def set_world():
    for col in range(len(world_menu.INFO)):
        for row in range(len(world_menu.INFO[col])):

            if world_menu.INFO[col][row] == -1:
                server.empty.append(world_menu.Empty_Tile(col, row))

            elif world_menu.INFO[col][row] == 1:
                server.ground.append(world_menu.Floor_Tile(col, row))

            elif world_menu.INFO[col][row] == 2:
                server.ground.append(world_menu.under_Tile(col, row))


def enter():
    global music
    set_world()
    server.world = world_menu.BACKGROUND()
    server.player = character.mario()

    game_world.add_object(server.world, 0)
    game_world.add_object(server.player, 1)
    game_world.add_objects(server.ground, 2)
    game_world.add_collision_group(server.player, server.ground, 'player:ground')


def exit():
    game_world.clear()
    server.ground.clear()
    server.empty.clear()

def update():
    set()
    if server.player.y < 0:
        game_framework.change_state(title_state)
        print('gameover')
    if server.player.y > 700:
        game_framework.change_state(title_state)
        print('clear')
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
