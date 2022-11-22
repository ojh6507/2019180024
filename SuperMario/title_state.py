import game_framework
from pico2d import *
import game_framework
import play_state

running = True
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('tuk_credit.png')

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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(play_state)
