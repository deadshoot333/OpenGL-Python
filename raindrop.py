import glfw 
from OpenGL.GL import * 
import random 

raindrops = []

for i in range(500):
    x = random.uniform(-1.0,1.0)
    y = random.uniform(1.0,2.0)
    speed = random.uniform(0.0001,0.0003)
    raindrops.append([x,y,speed])

def update_rain():
    for drop in raindrops:
        drop[1] -= drop[2]
        if drop[1] < -1.0:
            drop[0] = random.uniform(-1.0,1.0)
            drop[1] = random.uniform(-1.0,1.0)
def draw_rain():
    glBegin(GL_POINTS)
    for drops in raindrops:
        glVertex2f(drops[0],drops[1])
    glEnd()
    
glfw.init()

window = glfw.create_window(800,600,"My Window",None, None)
glfw.make_context_current(window)

glPointSize(2.0)
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    update_rain()
    draw_rain()
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
    