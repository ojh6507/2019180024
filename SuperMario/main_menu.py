import game_framework
from pico2d import *
import game_framework
import stage_state
import main_background
running = True
font = None
bgimg = None
logo = None
bx = None
ly = None
gap = None
voice = None
def enter():

    global bx, ly, bgimg, font, logo, gap, voice
    bx = 3770
    ly = 430
    gap = 0.5
    font = load_font('./block/SuperMario256.ttf', 30)
    logo = load_image('./background/nsmb_logo.png')
    bgimg = main_background.BACKGROUND()
    voice = load_wav('./music/Lets_Go.wav')
    voice.set_volume(20)


def exit():
    global bgimg, font, voice
    del bgimg
    del font
    del voice

def update():
    global bx,ly,gap
    bx -= 1
    ly += gap
    ly = clamp(410,ly,430)
    bx = clamp(0, bx, 3770)
    if bx == 0:
        bx = 3770

    if ly == 410 or ly == 430:
        gap *= -1


    bgimg.edit_x(bx)
    delay(0.02)

pass
def draw():
    global  ly
    clear_canvas()
    bgimg.draw()
    font.draw(280, 100, 'Press SPACE', (255, 255, 255))
    logo.clip_composite_draw(0,0, 2560, 1467, 0, ' ', 400, ly, 500, 300)

    update_canvas()
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            voice.play()
            delay(1)
            game_framework.change_state(stage_state)



