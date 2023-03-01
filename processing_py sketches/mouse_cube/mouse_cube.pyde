import random
        
def mouse_cube():
    fill(random.randint(0,255),random.randint(0,255), random.randint(0,255))
    rect(mouseX, mouseY, 20, 20)

def setup():
    size(1080,720)
    
    

def draw():
    background(0)
    mouse_cube()
    
    
    
    
        


    
        
