# Examples of mouse input

import simplegui
import math

# intialize globals
WIDTH = 450
HEIGHT = 300
ball_pos = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt( (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    global ball_pos, ball_color
    # if distance from mouse click to center of ball is larger than the radius (mouse click outside ball)...
    if distance(pos, ball_pos) < BALL_RADIUS:
    # ...change the color to green
    	ball_color = "Green"
    else:
    # ...otherwise, change the position and color the ball red
    	ball_pos = list(pos) # map tuple coordinates as list coordinates
        ball_color = "Red"

def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Black", ball_color)

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
# create mouse click handler and map to click function
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
    