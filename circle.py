import glfw 
from OpenGL.GL import * 
import math 

def circle(xc,yc,r): #center point and radius
    glBegin(GL_POINTS)
    for angle in range(0,361):
        angle = math.radians(angle)
        x = xc + int(r * math.cos(angle))
        y = yc + int(r * math.sin(angle))
        glVertex2i(x,y)
    glEnd()
glfw.init()


window = glfw.create_window(800,600,"Circle",None,None)
glfw.make_context_current(window)
##Create window first then set co-ordinates
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-800,800,-600,600,-1,1)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    circle(0,0,500)
    #very large circles, it may look "dotted" because there are only 360 points (degrees).
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
