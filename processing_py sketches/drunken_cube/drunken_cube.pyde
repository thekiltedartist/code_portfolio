import random
colors = [(191, 4, 73), (89, 2, 34), (3, 62, 140)]
start_x = 540
start_y = 360
def replicator():
    fill(random.randint(0,255),random.randint(0,255), random.randint(0,255))
    rect(start_x, start_y, 20, 20)
    
def randomizor():
    global start_x
    global start_y
    i = 0
    while i < 100:
        replicator()
        start_x += random.randint(-1, 1)
        start_y += random.randint(-1, 1)
        i +=1

def setup():
    size(1080,720)
    
    

def draw():
    background(0)
    randomizor()
    
    
    
    
        


    
        
