speed = 1
def setup():
    size (400, 400)
    background(3, 117, 202)
    
    f = 0
    while (f < 10):
        fish(random(400), random(400), random(255), random(255), random(255))
        f = f+1
    
def fish(xCoordinate, yCoordinate, r,g,b):
    fill(r,g,b)
    ellipse(xCoordinate, yCoordinate, 60, 30)
    triangle(xCoordinate+60, yCoordinate-10, xCoordinate+30, yCoordinate, xCoordinate+40, yCoordinate+30)
    
def draw():
    background(3, 117, 202)
    global xCoordinate, speed
    xCoordinate = random(50)
    xCoordinate += speed
    
