import glfw 
from OpenGL.GL import * 

def bresenham(x0,y0,x1,y1):
    dx = x1 - x0 
    dy = y1 - y0 
    p = 2 * (dy - dx)
    x = x0 
    y = y0 
    glVertex2i(x,y)
    while x<x1:
        x+=1
        if p >=0: 
            y += 1
            p += 2 * (dy - dx)
        else:
            p += 2 * dy 
        glVertex2i(x,y)

glfw.init()

window = glfw.create_window(800,600,"My Window",None,None)
glfw.make_context_current(window)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-800,800,-600,600,-1,1)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    bresenham(0,0,100,100)
    bresenham(200,0,300,100)
    bresenham(100,100,300,100)
    bresenham(200,0,300,100)
    bresenham(0,0,200,0)
    glEnd()
    
    glfw.swap_buffers(window)
    glfw.poll_events()
    
glfw.terminate()