import glfw 
from OpenGL.GL import * 
import math

def circle(xc,yc,r):
    
    glBegin(GL_POINTS)
    for angle in range(0,361):
        angle = math.radians(angle)
        x = xc + int(r * math.cos(angle)) 
        y = yc + int(r * math.sin(angle)) 
        glVertex2i(x,y)
    glEnd()
glfw.init()

window = glfw.create_window(800,600,"Bouncing Circle",None,None)
glfw.make_context_current(window)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-800,800,-600,600,-1,1)

x_pos = 0.0
y_pos = 0.0
x_velocity = 0.2
r = 100

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    if x_pos + r >= 600 or x_pos - r <= -800:
        x_velocity *=-1
    circle(int(x_pos),int(y_pos),r)
    x_pos += x_velocity
    glfw.swap_buffers(window)
    glfw.poll_events()
    
glfw.terminate()