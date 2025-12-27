import glfw 
from OpenGL.GL import * 

def bresenham_line(x0,y0,x1,y1):
    dx = x1 - x0 
    dy = y1 - y0 
    p = 2*(dy - dx)
    x = x0 
    y = y0 
    glVertex2i(x,y)
    while x < x1:
        x += 1 
        if p >=0:
            y += 1
            p += 2 * (dy - dx)
        else:
            p += 2 * dy 
        glVertex2i(x,y)

glfw.init()

window = glfw.create_window(800,600,"Bresenham Line",None,None)

glfw.make_context_current(window)

# --- THE KEY ADDITION ---
# Tell OpenGL to map coordinates to window pixels (0-800, 0-600)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-800, 800, -600, 600, -1, 1) 
# ------------------------

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    bresenham_line(0,0,100,100)
    glEnd()
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()