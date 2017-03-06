"""Someone else's code that is fully operational for how to do this game"""

import simplegui
import random

cur_range = 100
secret_number = " "
remaining_guess = " "

# Helper function
def new_game():
    """ Returns a new secret number for each new game,
    defines range and outputs remaining guesses."""
    
    global cur_range, secret_number, remaining_guess
    if cur_range == 100:
        secret_number = random.randrange(0, 100)
        remaining_guess = 7
        print "Range is from 0 to 100."
        print "Guess a number."
        print "You have",remaining_guess, "guesses remaining."
        remaining_guess = remaining_guess - 1        
        
    elif cur_range == 1000:
        secret_number = random.randrange(0, 1000)
        remaining_guess = 10
        print "Range is from 0 to 1000."
        print "Guess a number."
        print "You have",remaining_guess, "guesses remaining."
        remaining_guess = remaining_guess - 1
        
    else:
        new_game()
        

# Event handlers
def range100():
    """ Sets range to [0, 100)."""
    global cur_range   
    cur_range = 100
    print
    new_game()


def range1000():
    """ Sets range to [0, 1000)."""
    global cur_range    
    cur_range = 1000
    print
    new_game()


def input_guess(guess):
    """ Inputs a new guess and returns a conditional response.
    Shows remaining guesses, win/lose, and starts a new game."""
    
    global secret_number, remaining_guess
    guess = float(guess)
    print
    print "Guess was", guess
    
    if guess > secret_number:
        print "Lower"
        print "You have",remaining_guess, "guesses remaining."
        remaining_guess = remaining_guess - 1

        if remaining_guess == -1:
            print "You lose!"
            print
            print "Play again?"
            new_game()
        
    elif guess < secret_number:
        print "Higher"
        print "You have",remaining_guess, "guesses remaining."
        remaining_guess = remaining_guess - 1
        
        if remaining_guess == -1:
            print "You lose!"
            print
            print "Play again?"
            new_game()
        
    else:
        print "Correct! \nYou win!"
        print 
        print "Play again?"
        new_game()

    
# Frame
frame = simplegui.create_frame("Guess the Number", 300, 300)


# Register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 150)
frame.add_button("Range is [0, 1000)", range1000, 150)
frame.add_input("Guess", input_guess, 150)

# Call new_game 
new_game()

