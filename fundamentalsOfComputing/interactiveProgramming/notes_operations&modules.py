# Remainder - modular arithmetic

# systematically restrict computation to a range
# long division - divide by a number, we get a quotient plus a remainder
# quotient is integer division //, the remainder is % (Docs)


# problem - reproduce a number using modular arithmetic
num = 49
tens = num // 10 #performs modular division, returning 4
ones = num % 10 #gives remainder, returning 9
print tens, ones
print 10 * tens + ones, num #multiplies the 10s place by 10 and sums the ones place to it



#Modular arithmetic of a%b shows the remainder of a when divided by b.
#If a is less than b, than the modular arithmetic value is a.

# application - 24 hour clock
# http://en.wikipedia.org/wiki/24-hour_clock

hour = 20
shift = 8
print (hour + shift) % 24 #returns the time on a 24 hour clock after time has been shifted hours into the future equal to the shift value




# application - screen wraparound
# Spaceship from week seven

width = 800 #how wide screen is 
position = 797 #where the spaceship currently is on screen
move = 5 #how far spaceship moves to right from current position
position = (position + move) % width #goes back to beginning of screen by value that spaceship's new position exceeds divisor of screen width (between 0 and 800)... 
                                     #...because you must wrap around to opposite side after exceeding screen's edge
print position

#Remainder applications also works for negative values (clock and scren wrap applications are accurate even with negative remainder divided numbers)


# Data conversion operations

# convert an integer into string - str
# convert an hour into 24-hour format "03:00", always print leading zero

hour = 3
ones = hour % 10 #returns the ones place (hour)
tens = hour // 10 #returns the 10s place (hour)
print tens, ones, ":00"
print str(tens), str(ones), ":00" #convert ints to strings in order to...
print str(tens) + str(ones) + ":00" #...concatenate them!!!

# convert a string into numbers using int and float



# Python modules - extra functions implemented outside basic Python (must be imported)

import simplegui	# access to drawing operations for interactive applications

import math	 		# access to standard math functions, e.g; trig

import random   	# functions to generate random numbers


# look in Docs for useful functions

print math.pi