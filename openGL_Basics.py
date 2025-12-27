import glfw 
from OpenGL.GL import * 

glfw.init()

window = glfw.create_window(800,600,"OpenGL Window",None,None)

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    
    ##RENDERING CODES
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(0.1,0.2) 
    # glVertex2f(0.6,0.7)
    glEnd()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
   