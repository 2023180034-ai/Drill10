from pico2d import *
import random


# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):   # 잔디는 움직이지 않아 update()가 필요없음
        pass

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Zombie:
    def __init__(self):
        self.x = 100
        self.y = 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10 
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height, self.x, self.y, frame_width // 2, frame_height // 2)

class Ball:
    def __init__(self):
        self.ballType = random.randint(0,1)  # 0 : 작은공, 1 : 큰 공
        if self.ballType == 0:
            self.image = load_image('ball21x21.png')
            self.x = random.randint(100, 700)
            self.y = 599
        else:
            self.image = load_image('ball41x41.png')
            self.x = random.randint(100, 700)
            self.y = 599
        
        
    def update(self):
        pass
    def draw(self):
        pass
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():      # 초기화
    global running
    global world

    running = True

    world =[]

    grass = Grass()
    world.append(grass)

    zombie = Zombie()
    world.append(zombie)

    balls = [Ball() for i in range(20)]
    world += balls

    team = [Boy() for i in range(11)]
    world += team

def update_world():     # 업데이트
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
