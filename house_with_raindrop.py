import glfw 
from OpenGL.GL import * 
import random 

raindrops = []

def rain_init():
    for i in range(500):
        x = random.uniform(-1.0,1.0)
        y = random.uniform(-1.0,1.0)
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
  for drop in raindrops:
      glVertex2f(drop[0],drop[1])
  glEnd()        

def house_room():
    # glColor3f(0,1,1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.0,0.0)
    glVertex2f(0.5,0)
    glVertex2f(0.5,0.5)
    glVertex2f(0.0,0.5)
    glEnd()

def house_roof():
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.0,0.5)
    glVertex2f(0.25,0.8)
    glVertex2f(0.5,0.5)
    glEnd()

def house_door():
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.25,0)
    glVertex2f(0.35,0)
    glVertex2f(0.35,0.25)
    glVertex2f(0.25,0.25)
    glEnd()


glfw.init()

window = glfw.create_window(800,600,"House with Raindrop",None,None)
glfw.make_context_current(window)

glPointSize(2.0)
rain_init()
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    update_rain()
    house_room()
    house_roof()
    house_door()
    draw_rain()
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()