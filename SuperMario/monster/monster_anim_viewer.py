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
rframe = 0
rrframe = 0
raction = 0

mbos = load_image('jr_coopa.png')
goomba = load_image('Goomba.png')
rkoopa = load_image('red_koopa.png')
rrkoopa = load_image('red_koopa_wake.png')


while running:
    clear_canvas()
    # jump: character.clip_draw(frame * 50,  action , 50, 75, x, 110)
    mbos.clip_draw(bframe * 50,  60 , 50, 70, 500, 90)
    goomba.clip_draw(0,  gframe * 50 , 42, 50, 600, 90)
    rkoopa.clip_draw(rframe * 25, 50 * raction, 25, 50, 900, 90)
    rrkoopa.clip_draw(rrframe * 50, 0, 50, 48, 900, 200)

    update_canvas()
    handle_events()

    bframe = (bframe + 1) % 19
    gframe = (gframe - 1) % 8
    rframe =(rframe + 1) % 18
    rrframe =(rframe + 1) % 5
    
    if rframe == 0:
        if raction == 0:
            raction = 1
        else:
            raction = 0
   
    delay(0.1)
close_canvas()