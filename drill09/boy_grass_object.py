from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x +=5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)



class Big_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 600
        self.speed = random.randint(3,8)
        self.B_image = load_image('ball41X41.png')
    def update(self):
        if self.y <= 80:
            pass
        else:
            self.y -= self.speed

    def draw(self):
        self.B_image.draw(self.x,self.y)


class Small_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 600
        self.speed = random.randint(3, 8)
        self.S_image = load_image('ball21X21.png')
    def update(self):
        if self.y <= 70:
            pass
        else:
            self.y -= self.speed
    def draw(self):
        self.S_image.draw(self.x,self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
# initialization code

open_canvas()
num = 10
Bball = [Big_Ball() for i in range(random.randint(5,15))]
Sball = [Small_Ball() for a in range(10)]
team = [Boy() for b in range(11)]
grass = Grass()

running = True

# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()
    for big in Bball:
        big.update()
    for small in Sball:
        small.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for big in Bball:
        big.draw()
    for small in Sball:
        small.draw()
    update_canvas()
    delay(0.05)



# finalization code

close_canvas()