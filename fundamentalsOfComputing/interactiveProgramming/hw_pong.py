""" SUBMITTED COPY"""

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
score1 = 0
score2 = 0
adj_pad_1 = 0
adj_pad_2 = 0
paddle1_pos = .5 * HEIGHT - .5 * PAD_HEIGHT
paddle2_pos = .5 * HEIGHT - .5 * PAD_HEIGHT
ball_pos = [0.5*WIDTH, 0.5*HEIGHT]
ball_vel = [.01*random.randrange(-99, 100), .01*random.randrange(-99, 100)]

def spawn_ball():
    global BALL_RADIUS, WIDTH, HEIGHT, ball_pos, ball_vel, paddle1_pos, paddle2_pos, PAD_HEIGHT, score1, score2
    
    if ball_pos[0] <= BALL_RADIUS and ball_pos[1] > paddle1_pos and ball_pos[1] < paddle1_pos + PAD_HEIGHT:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] <= BALL_RADIUS: 
        ball_pos = [0.5*WIDTH, 0.5*HEIGHT]
        ball_vel = [1, .01*random.randrange(-99, 100)]
        score2 += 1
    
    if ball_pos[0] >= WIDTH - BALL_RADIUS and ball_pos[1] > paddle2_pos and ball_pos[1] < paddle2_pos + PAD_HEIGHT:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_pos = [0.5*WIDTH, 0.5*HEIGHT]
        ball_vel = [-1, .01*random.randrange(-99, 100)]
        score1 += 1
    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_vel[0] >= 0:
        ball_vel[0] += .0025
    elif ball_vel[0] < 0:
        ball_vel[0] -= .0025
    if ball_vel[1] >= 0:
        ball_vel[1] += .0025
    elif ball_vel[1] < 0:
        ball_vel[1] -= .0025
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, PAD_HEIGHT, PAD_WIDTH
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 3, "White", "White")
    
    # draw paddles
    canvas.draw_polyline([(.5*PAD_WIDTH, paddle1_pos), (.5*PAD_WIDTH, paddle1_pos + PAD_HEIGHT)], PAD_WIDTH, "White")
    canvas.draw_polyline([(WIDTH - .5*PAD_WIDTH, paddle2_pos), (WIDTH - .5*PAD_WIDTH, paddle2_pos + PAD_HEIGHT)], PAD_WIDTH, "White")    
    
    # draw scores
    canvas.draw_text(str(score1),[150, 100], 70, "White") 
    canvas.draw_text(str(score2),[400, 100], 70, "White") 
        
def keydown(key):
    global adj_pad_1, adj_pad_2, paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos, HEIGHT, PAD_HEIGHT
    
    if key == simplegui.KEY_MAP["s"] and paddle1_pos >= 0:
        adj_pad_1 = 5
    elif key == simplegui.KEY_MAP["w"] and paddle1_pos <= HEIGHT - PAD_HEIGHT:
        adj_pad_1 = -5
    else:
        adj_pad_1 = 0
    
    if key == simplegui.KEY_MAP["down"] and paddle2_pos >= 0:
        adj_pad_2 = 5
    elif key == simplegui.KEY_MAP["up"] and paddle2_pos <= HEIGHT - PAD_HEIGHT:
        adj_pad_2 = -5
    else:
        adj_pad_2 = 0
        
def keyup(key):
    global paddle1_vel, paddle2_vel, adj_pad_1, adj_pad_2
    adj_pad_1 = 0
    adj_pad_2 = 0 
    
def reset():
    global score1, score2, ball_pos, ball_vel
    score1 = 0
    score2 = 0
    ball_pos = [0.5*WIDTH, 0.5*HEIGHT]
    ball_vel = [.01*random.randrange(-99, 100), .01*random.randrange(-99, 100)]
    
def tick():
    global ball_vel
    spawn_ball()
    
def tock():
    global adj_pad_1, adj_pad_2, paddle1_pos, paddle2_pos
    if paddle1_pos > HEIGHT - PAD_HEIGHT:
        adj_pad_1 = 0
        paddle1_pos = HEIGHT - PAD_HEIGHT
    
    if paddle1_pos < 0:
        adj_pad_1 = 0
        paddle1_pos = 0
    
    if paddle2_pos > HEIGHT - PAD_HEIGHT: 
        adj_pad_2 = 0
        paddle2_pos = HEIGHT - PAD_HEIGHT
    
    if paddle2_pos < 0:
        adj_pad_2 = 0
        paddle2_pos = 0
    
    paddle1_pos += adj_pad_1
    paddle2_pos += adj_pad_2
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("RESET", reset, 200)
timer1 = simplegui.create_timer(10, tick)
timer2 = simplegui.create_timer(10, tock)


# start frame
new_game()
frame.start()
timer1.start()
timer2.start()
