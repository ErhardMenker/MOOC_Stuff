# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

# A simplegui generates a window with three main areas
# The control area has buttons allowing different inputs
# The canvas on the right shows output such as text
# The status area gives feedback about keyboard and mouse events (such as output values in a calculator)
# frame.start() creates the frame

## Program structure where simplegui is used:
# Define globals 
# Create helper functions
# State classes
# Define event handlers
# Create a frame
# Register event handlers
# Start frame and timers

import simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 36, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
