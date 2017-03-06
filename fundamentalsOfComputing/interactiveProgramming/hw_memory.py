""" Version works except for counting issue in case of stupid players """

# implementation of card game - Memory

import simplegui
import random

# global creation
turns = 0
turns_utility = 0
turns_message = "Turns = " + str(turns)
cards_1 = range(8)
cards_2 = range(8)
deck = None
card = None
card_location = None
store_card = None
store_card_location = None
eternal_list = list()

# helper function to initialize globals
def new_game():
    global turns, turns_utility, cards_1, cards_2, deck, eternal_list, card, card_location, store_card, store_card_location
    turns = 0
    turns_utility = 0
    random.shuffle(cards_1)
    random.shuffle(cards_2)
    deck = cards_1 + cards_2
    
    eternal_list = []
    card = None
    card_location = None
    store_card = None
    store_card_location = None

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global turns, turns_utility, deck, card, card_location, store_card, store_card_location, eternal_list
    
    turns_utility += 1
    turns = turns_utility // 2

    if turns_utility % 2 == 0:
        store_card = card
        store_card_location = card_location
    elif turns_utility % 2 == 1:
        store_card = None
        store_card_location = None
    for index in range(len(deck)):
        if pos[0] < 50 * (index + 1) and pos[0] > 50 * index:
            card = deck[index]
            card_location = index
      
    if (card == store_card) and card_location <> store_card_location:
        eternal_list.append([card, card_location])
        eternal_list.append([store_card, store_card_location])
   
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card, card_location, store_card, store_card_location
    label.set_text("Turns = " + str(turns))
    for card_val in range(15):
        card_val += 1
        horiz = 50*card_val
        canvas.draw_line((horiz, 0), (horiz, 100), 1, 'red')
    if card != None:
        canvas.draw_text(str(card), (50 * card_location + 15, 60), 50, "red")
    if store_card != None:
        canvas.draw_text(str(store_card), (50 * store_card_location + 15, 60), 50, "red")
    if eternal_list <> []:
        for value_index_pair in eternal_list:
            canvas.draw_text(str(value_index_pair[0]), (50 * value_index_pair[1] + 15, 60), 50, "red")
        
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.set_canvas_background("green")
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
