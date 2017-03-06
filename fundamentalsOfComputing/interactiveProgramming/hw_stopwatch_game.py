# template for "Stopwatch: The Game"

import simplegui

# define global variables
t = 0
a = 0
b = 0
c = 0
x = 0 
y = 0
tock_count = 0
timer_stop = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global a, b, c, d, tock_count
    a = t % 10
    tock_count += 1
    if a == 0:
        b += 1
        b = b % 60
    if tock_count % 600 == 0:
        c += 1
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_stop 
    timer_stop = False
    timer.start()
    timer_handler()
    
def stop():
    timer.stop()
    global x, y, timer_stop
    if timer_stop == False:
        y += 1
        if a == 0:
            x += 1
    timer_stop = True
    
def reset():
    timer.stop()
    global a, b, c, t, tock_count, x, y
    t = 0
    a = 0
    b = 0
    c = 0
    tock_count = 0
    x = 0
    y = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t = t + 1
    format(t)

# define draw handler
def draw_handler(canvas):
    global a, b, c, x, y
    if b < 10:
        time_print = str(c) + ":" + "0" + str(b) + "." + str(a)
    else:
        time_print = str(c) + ":" + str(b) + "." + str(a)
    canvas.draw_text(time_print, (100, 130), 50, "Red")
    ratio = str(x) + "/" + str(y)
    canvas.draw_text(ratio, (220,30), 35, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("START", start, 200)
frame.add_button("STOP", stop, 200)
frame.add_button("RESET", reset, 200)

# start frame
frame.start()

# Please remember to review the grading rubric
