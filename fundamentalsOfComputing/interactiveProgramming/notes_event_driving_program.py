#The programming model in linear form means that there is simply sequential..
#...execution whose result only vary by data inputs
#Event driven programming sets up the program, and then waits for a specific input (event) to occur and reacts accordingly
#Whenever an event occurs, the program responds accordingly by referencing the appropriate handler functions... 
#...(maybe a button is hit, so the button handler function part of the program is called)

##Possible Events:
#Input (button, text box)
#Keyboard (key down, key up)
#Mouse (click, drag)
#Timer

#The wait state occurs when the program is done, and the user interface waits for events to occur for the program to react to them
#The "event queue" is the process with which events occur and are reponded to accordingly by the computer.
#Subsequent events cannot be executed while the handler is handling the current event, so processing needs to be fast for applications (games) not to lag

# Example of a simple event-driven program

# CodeSkulptor GUI module
import simplegui

# Event handler
def tick():
    print "tick!"

# Register handler
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()
