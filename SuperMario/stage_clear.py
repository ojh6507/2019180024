
import game_framework
from pico2d import *
import game_framework
import stage_state
import main_menu

running = True
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('./background/clear.png')

def exit():
    global image
    del image

def update():
   pass
def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            game_framework.change_state(stage_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_b):
            game_framework.change_state(main_menu)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_KP_A):
            game_framework.change_state(stage_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_KP_B):
            game_framework.change_state(main_menu)

