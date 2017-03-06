import simplegui

# Define globals
point = [10, 20]
velocity = [3, 0.7]
time = 0

# Create event handlers
def draw(canvas):
    global point
    canvas.draw_polygon([(50, 50), (180, 50), (180, 140), (50, 140)], 12, "Blue", "Blue") 
    canvas.draw_circle(point, 3, 3, "Red", "Red")
    
def tick():
    global point, velocity
    point[0] += velocity[0]
    point[1] += velocity[1] 

# Create frame and timer
frame = simplegui.create_frame("Quiz Question", 300, 300)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# Start frame and timer
timer.start()
frame.start()