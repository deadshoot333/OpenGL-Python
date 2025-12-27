import glfw 
from OpenGL.GL import * 

#OpenGL coordinate system goes from -1.0 to 1.0,
def square_meth1():
    glBegin(GL_LINES)
    #bottom edge
    glVertex2f(0,0)
    glVertex2f(0.5,0)
    #left edge
    glVertex2f(0,0)
    glVertex2f(0,0.5)
    #top edge
    glVertex2f(0,0.5)
    glVertex2f(0.5,0.5)
    #right edge
    glVertex2f(0.5,0.5) 
    glVertex2f(0.5,0)
    glEnd()
    

def square_meth2():
    glBegin(GL_LINE_LOOP)
    #top left vertice
    glVertex2f(-0.6,0.5)
    #top right
    glVertex2f(-0.1,0.5)
    #bottom right
    glVertex2f(-0.1,0)
    #bottom left
    glVertex2f(-0.6,0)
    glEnd()
    
glfw.init()

window = glfw.create_window(800,600,"MyWindow",None,None)

glfw.make_context_current(window)

if __name__=="__main__":
    
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        #method_1
        square_meth1()
        #method_2
        square_meth2()
        glfw.swap_buffers(window)
        glfw.poll_events()
        
    glfw.terminate()