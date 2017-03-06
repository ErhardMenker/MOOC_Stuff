import simplegui

def draw(canvas):
    canvas.draw_circle([90, 200], 20, 10, 'white')
    canvas.draw_circle([210, 200], 20, 10, 'white')
    canvas.draw_line([55, 170], [90, 120], 5, 'red') 
    canvas.draw_line([90, 120], [130, 120], 5, 'red') 
    canvas.draw_line([50, 180], [250, 180], 40, 'red')
    
frame = simplegui.create_frame("homework", 300, 300)
frame.set_draw_handler(draw)
frame.start()