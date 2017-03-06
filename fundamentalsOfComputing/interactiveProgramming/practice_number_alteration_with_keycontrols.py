import simplegui

# Define globals
number = 5
count = 0

def keydown(key):
    global number
    number *= 2

def keyup(key):
    global number, count
    number -= 3
    count += 1
    print number, "count is", count

# Create frame and timer
frame = simplegui.create_frame("Quiz Question", 300, 300)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Start frame and timer
frame.start()