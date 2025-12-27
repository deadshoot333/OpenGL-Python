import glfw 
from OpenGL.GL import * 

def triangle():
    glBegin(GL_LINE_LOOP)
    glVertex2f(0,0.5)
    glVertex2f(0.5,0.5)
    glVertex2f(0.25,0.8)
    glEnd()
def square():
    glBegin(GL_LINE_LOOP)
    glVertex2f(0,0.5)
    glVertex2f(0.5,0.5)
    glVertex2f(0.5,0)
    glVertex2f(0,0)
    glEnd()
def door():
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.2,0)
    glVertex2f(0.2,0.25)
    glVertex2f(0.3,0.25)
    glVertex2f(0.3,0)
    glEnd()
glfw.init()

window = glfw.create_window(800,600,"House",None,None)

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    triangle()
    square()
    door()
    glfw.swap_buffers(window)
    glfw.poll_events()
    
glfw.terminate()