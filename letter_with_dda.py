import glfw 
from OpenGL.GL import *

def dda(x0,y0,x1,y1):
    glBegin(GL_POINTS)
    dx = x1 - x0 
    dy = y1 - y0 
    steps = max(abs(dx),abs(dy))
    xinc = dx / steps 
    yinc = dy / steps 
    x,y = x0,y0
    for i in range(steps+1):
        glVertex2i(round(x),round(y))
        x += xinc 
        y += yinc
    glEnd()
glfw.init()

window = glfw.create_window(800,600,"Letter with DDA",None,None)
glfw.make_context_current(window)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-800,800,-600,600,-1,1)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    
    dda(0,0,100,100)
    dda(100,100,200,0)
    dda(20,40,180,40)
    glfw.swap_buffers(window)
    glfw.poll_events()
    
glfw.terminate()