import game_framework
import main_state
import title_state
from pico2d import *

name = "PauseState"
image = None
time = None



def enter():
    global image,time
    time = 0
    image = load_image('pause.png')

def exit():
    global image
    del(image)

def pause():
    pass
def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            #game_framework.change_state(title_state)
        elif(event.type,event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()



def draw():
    clear_canvas()
    main_state.draw()
    if time < 1:
        image.clip_draw(250, 250, 400, 400, 400, 400)
    update_canvas()
    
def update():
    global time
    time = (time+0.05)%2
    pass