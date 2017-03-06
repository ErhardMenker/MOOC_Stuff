# Python coordinates can be given by [p[0], p[1]] for point p.
# The distance between two points p and q can be given by:
import math
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# Vectors can be thought of as the distance between each respective point.
# Given old position q and velocity vector v, the new value of the object located at point p is:
p[0] = q[0] + v[0] # new x-coordinate
p[1] = q[1] + v[1] # new y-coordinate

# Now imagine point p (two element list showing current x and y coordinates) that must stay in coordinates that are to be bounded within the canvas:
# Instances where point p collides with the wall:
p[0] <= 0 # x-value has gone past the left wall
p[0] >= width # x-value has gone past the right wall
# Instances where ball with center p and radius r collides with wall:
p[0] <= r # If the current position is less than r, part of ball is off screen
p[0] >= width - r # Left part of ball is off screen

# When a ball collides with the edge of the canvas, it must reflect and change directions.
# When a ball reflects off of a horizontal wall, the vertical element in the vector stays the same but the horizontal becomes negated:
v[0] = -v[0]
v[1] = v[1]

""" Improved Ball Movement Function (Reflects upon Collision) """

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0 / 60.0,  5.0 / 60.0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
        
    # collide and reflect off of right hand side of canvas
    if ball_pos[0] >= WIDTH - BALL_RADIUS:
        vel[0] = -vel[0]

    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()