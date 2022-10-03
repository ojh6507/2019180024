from pico2d import *
def handle_events():
    global running
    global dir
    global action
    global character
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            running =False
        elif event.type ==SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir+= 1
                action = 70
                character =load_image('mario_walk.png')
            elif event.key == SDLK_LEFT:
                dir-= 1
                action = 5
                character =load_image('mario_walk.png')
        elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir-= 1
                character =load_image('idle_right.png')
                action = 5
             
            if event.key == SDLK_LEFT:
                dir+= 1
                character =load_image('idle_left.png')
                action = 5
           
running = True
open_canvas(1280,1024)

frame = 0
#bframe = 0
#block_frame = 0
dir = 0
x= 800//2
action  = 3
#character =load_image('jump.png')
character =load_image('jump.png')
characteridle =load_image('idle_right.png')

#icblock =load_image('block_1.png')
#bblock =load_image('block_2.png')
#mbos = load_image('jr_coopa.png')
#grass =load_image('grass.png')
x1= 200
frame2 = 0   
while running:
    clear_canvas()
    # jump: character.clip_draw(frame * 50,  action , 50, 75, x, 110)
    character.clip_draw(frame * 50,  10 , 50, 70, x, 90)
    characteridle.clip_draw(frame2 * 50,  3 , 50, 60, x1, 90)
 
 #   mbos.clip_draw(bframe * 50,  70 , 50, 60, 500, 90)
    
  #  grass.draw(400,35)
  #  icblock.clip_draw(block_frame * 30,  0 , 30, 35, 400, 200)
  #  bblock.clip_draw(block_frame * 30,  0 , 30, 35, 425, 200)
    #block_frame = (block_frame+1) % 4
 
    update_canvas()
    
    handle_events()

    frame = (frame + 1) % 18
    frame2 = (frame2 +1) % 79
    delay(0.1)

    x += dir * 5
    #if dir != 0:
     #   frame = (frame + dir) % 18
      #  delay(0.1)

    #else:
     #   frame = (frame + 1) % 79
      #  delay(0.03)

   # bframe = (bframe + 1) % 19
    
close_canvas()