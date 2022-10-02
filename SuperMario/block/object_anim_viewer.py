from pico2d import *
def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            running =False

running = True
open_canvas()

frame = 0

coin =load_image('coin.png')
bblock =load_image('block_2.png')
icblock =load_image('block_1.png')

while running:
    clear_canvas()
    coin.clip_draw(frame * 25 ,0 ,25 ,25 ,400,90)
    bblock.clip_draw(frame * 30 ,0 ,30 ,40 ,370,90)
    icblock.clip_draw(frame * 30 ,0 ,30 ,40 ,330,90)
    update_canvas()
    handle_events()
    frame = (frame+1) % 4
    delay(0.1)
close_canvas()