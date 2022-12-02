from pico2d import *
import game_framework
import main_menu
import Final_clear_map

running = True
font = None
logo = None
ly = None
gap = None
mainBgm = None
color = (255,255,255)
choose_sound = None
bgd = None
delay_draw = 0
def enter():

    global ly, font, logo, gap, mainBgm,bgd, choose_sound, delay_draw
    ly = 430
    gap = 0.5
    font = load_font('./block/SuperMario256.ttf', 20)
    logo = load_image('./background/congratulations.png')
    choose_sound = load_wav('./music/Choose.wav')
    bgd = Final_clear_map.BACKGROUND()
    choose_sound.set_volume(30)




def exit():
    global font
    del font

def update():
    global ly,gap,bgd,delay_draw
    ly += gap
    delay_draw += 1
    ly = clamp(410,ly,430)
    bgd.update()

    if ly == 410 or ly == 430:
        gap *= -1

    delay(0.02)

def draw():
    global ly, bgd, delay_draw
    clear_canvas()

    bgd.draw()
    logo.clip_composite_draw(0,0, 2118, 158, 0, ' ', 400, ly, 700, 80)
    if delay_draw % 2 == 0:
        font.draw(280, 20, 'press A to Main Menu', color)



    update_canvas()
def handle_events():
    global color
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == ((SDL_KEYDOWN, SDLK_a) or (SDL_KEYDOWN, SDLK_KP_A)):
            choose_sound.play()
            delay(0.3)
            game_framework.change_state(main_menu)



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
