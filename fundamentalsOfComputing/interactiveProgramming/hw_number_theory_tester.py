import simplegui

# Declare globals
n = 217
max = 23

def timer_handler():
    global n, max
    if n%2 == 0:
        n = n/2
    elif n%2 == 1:
        n = 3*n + 1
    if n > max:
        max = n
        print max
    return n

timer = simplegui.create_timer(300, timer_handler)

# Start timer
timer.start()