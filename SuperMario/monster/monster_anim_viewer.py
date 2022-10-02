from pico2d import *     
running = True
open_canvas(1280,1024)
def handle_events():

    events = get_events()
    global running
    for event in events:
        if event.type== SDL_QUIT:
            running = False

bframe = 0
gframe = 8
mbos = load_image('jr_coopa.png')
goomba = load_image('Goomba.png')

while running:
    clear_canvas()
    # jump: character.clip_draw(frame * 50,  action , 50, 75, x, 110)
    mbos.clip_draw(bframe * 50,  60 , 50, 70, 500, 90)
    goomba.clip_draw(0,  gframe * 50 , 42, 50, 600, 90)

    update_canvas()
    handle_events()

    bframe = (bframe + 1) % 19
    gframe = (gframe - 1) % 8
    delay(0.1)
close_canvas()