import random

"""
Function to convert a string name input into relevant number
"""

def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print ("erroneous human name input")
    return number

"""
Function to convert a number into the same string output as name_to_number function
"""

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print ("erroneous computer number input")
    return name
    
"""
Application function that invokes other two functions, comparing computer choice to human input
"""
    
def rpsls(player_choice):
    print ("Player chooses " + player_choice)
    player_number = name_to_number(player_choice)
    #computer randomly simulates integer between 0 and 4, inclusive 
    comp_number = random.randrange(0,5)
    comp_name = number_to_name(comp_number)
    print ("Computer chooses " + comp_name)
    if comp_number == player_number:
        print ("Player and computer tie!")
    elif (player_number - comp_number)%5 == 1 or (player_number - comp_number)%5 == 2:
        print ("Player wins!")
    elif (player_number - comp_number)%5 == 3 or (player_number - comp_number)%5 == 4:
        print ("Computer wins!")
    print ""

#calls to the application function:
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")





