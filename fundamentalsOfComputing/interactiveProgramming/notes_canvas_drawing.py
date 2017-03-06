# Computer monitors show 2D grid of pixels which are stored in a frame buffer.
# Computers update the monitor based on the frame buffer at a rate of 60-72 times a second (refresh rate)
# Many applications will register a special function called a "draw handler."
# The draw handler takes in the updated content within the frame buffer.
# In CodeSkulptor, the draw handler is registered using a simpleGUI command and is called at 60 times per second.
# Draw handler updates the canvas using a series of draw commands.

## Canvas coordinates
# Canvas coordinates are provided in Cartesian Coordinates where the origin, [0, 0], is in the upper left of the canvas.
# The x-coordinate in the coordinate pair shows how far to go to the right, while the y-coordinate shows how far down to go.

# First example of drawing on the canvas:

import simplegui

# define draw handler
def draw(canvas):
    # 1st arg is text, 2nd is location, 3rd is font size, 4th is color
    canvas.draw_text("Hello!",[100, 100], 24, "White")
    # location of position starts at the lower left hand corner 
    canvas.draw_circle([100, 100], 2, 2, "Red")

# create frame
frame = simplegui.create_frame("Text drawing", 300, 200)

# register draw handler that registers the 'draw function' which can create images    
frame.set_draw_handler(draw)

# start frame
frame.start()

# Second example of more advanced canvas drawing:

# example of drawing operations in simplegui
# standard HMTL color such as "Red" and "Green"
# note later drawing operations overwrite earlier drawing operations

import simplegui


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_circle([100, 100], 50, 2, "Red", "Pink")
    canvas.draw_circle([300, 300], 50, 2, "Red", "Pink")
    canvas.draw_line([100, 100],[300, 300], 2, "Black")
    canvas.draw_circle([100, 300], 50, 2, "Green", "Lime")
    canvas.draw_circle([300, 100], 50, 2, "Green", "Lime")
    canvas.draw_line([100, 300],[300, 100], 2, "Black")
    canvas.draw_polygon([[150, 150], [250, 150], [250, 250], [150, 250]], 2, 
          "Blue", "Aqua")
    canvas.draw_text("An example of drawing", [60, 385], 24, "Black")

    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 400, 400)
frame.set_draw_handler(draw)
frame.set_canvas_background("Yellow")


# Start the frame animation
frame.start()
