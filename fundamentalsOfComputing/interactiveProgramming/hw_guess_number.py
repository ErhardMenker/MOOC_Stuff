import simplegui
import random

# Initialize global variables used in code
guess_remain = 10

# Helper function to initialize game
def new_game():
    print "New game. Range is from 0 to 1000"
    x = range1000()
    return x
    
def range1000():
    val = random.randrange(0, 1000)
    return val

comp_num = new_game()

# Define callback functions for control panel
def get_input(guess):
    global comp_num, guess_remain
    player_num = int(guess)
    print "Guess was", player_num
    guess_remain -= 1
    if guess_remain >= 1:
        if player_num > comp_num:
            print "Number of remaining guesses is", guess_remain
            print "Lower!"
        elif player_num < comp_num:
            print "Number of remaining guesses is", guess_remain
            print "Higher!"
        elif player_num == comp_num:
            print "Correct!"
            comp_num = new_game()
            guess_remain = 10
    elif guess_remain == 0:
        if player_num != comp_num:
            print "You ran out of guesses. The number was", comp_num
        elif player_num == comp_num:
            print "Correct!"
        guess_remain = 10
        comp_num = new_game() 
    
        

# Create window
f = simplegui.create_frame("Guess the number", 200, 200)
                           
                           
# Create control elements for window
#f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)
             
new_game()
f.start()