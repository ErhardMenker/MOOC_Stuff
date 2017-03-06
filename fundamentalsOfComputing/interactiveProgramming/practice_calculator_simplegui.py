# starting point for calculator

import simplegui

# intialize globals
store = 0
operand = 0

# event handlers for calculator with a store and operand

# output() is mother function called in all operations
def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    """ swap contents of store and operand"""
    global store, operand #clarifies store and operand are global values, not local to function swap()
    store, operand = operand, store
    output()
    
def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()
    
def enter(inp):
    global operand
    operand = int(inp)
    output()

# create frame
f = simplegui.create_frame("Calculator",300,300)

# register event handlers (second input are function calls)
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("Add", add, 100)
f.add_button("Sub", sub, 100)
f.add_button("Mult", mult, 100)
f.add_button("Div", div, 100)
f.add_input("Enter operand", enter, 100)

# get frame rolling
f.start()