import glfw
from OpenGL.GL import *
import time

def draw_triangle(x):
    glBegin(GL_TRIANGLES)
    # Use a nice color so we can see it clearly
    # glColor3f(0.2, 0.6, 1.0) 
    glVertex2f(x, 0.5)
    glVertex2f(x - 0.5, -0.5)
    glVertex2f(x + 0.5, -0.5)
    glEnd()

if not glfw.init():
    raise Exception("GLFW cannot be initialized")

window = glfw.create_window(800, 600, "Bouncing Triangle Animation", None, None)

if not window:
    glfw.terminate()
    raise Exception("Window cannot be created")

glfw.make_context_current(window)

# 1. Configuration
x_position = 0.0
x_velocity = 0.02  # This determines the speed and direction
triangle_width = 0.5 # Half-width of your triangle

while not glfw.window_should_close(window):
    # Clear the screen (Black background)
    glClear(GL_COLOR_BUFFER_BIT)
    
    # 2. Update the position
    x_position += x_velocity
    
    # 3. Bounce Logic
    # Check if the RIGHT edge hits the right wall OR the LEFT edge hits the left wall
    if x_position + triangle_width >= 1.0 or x_position - triangle_width <= -1.0:
        x_velocity *= -1.0  # Reverse the direction
    
    # 4. Drawing
    draw_triangle(x_position)
    
    glfw.swap_buffers(window)
    glfw.poll_events()
    
    # Control frame rate (approx 60 FPS)
    time.sleep(1/60)

glfw.terminate()