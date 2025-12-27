import glfw 
from OpenGL.GL import * 

glfw.init()

window = glfw.create_window(800,600,"Triangle Window",None,None)

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(0.5,0.6)
    glVertex2f(1,-0.5)
    glEnd()
    
    glfw.swap_buffers(window)
    glfw.poll_events()    

glfw.terminate()