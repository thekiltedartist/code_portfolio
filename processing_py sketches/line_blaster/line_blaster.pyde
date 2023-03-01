import random
start_y = 720
def line_blaster():
    global start_y
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rando_w = random.randint(-20, 20)
    rando_h = random.randint(-720, 20)
    random_x = random.randint(0, 1080)
    fill(r, g, b)
    rect(random_x, start_y, rando_w, rando_h)
    noStroke()

def setup():
    size(1080,720)
    background(0)
    
def draw():
    line_blaster()
    


    
        
