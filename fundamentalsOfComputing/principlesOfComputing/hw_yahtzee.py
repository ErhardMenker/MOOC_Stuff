""" 98% """

"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""
# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length, allowing repeats.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    
    return answer_set


def gen_all_uniques(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length, barring repeats.
    """
    #make tuple of outcomes into a list to be copied later
    outcomes = list(outcomes)
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            outcomes_copy = outcomes[:]
            for numb in partial_sequence:
                #remove the copied value from list, so not reappended
                outcomes_copy.remove(numb)
            for item in outcomes_copy:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    max_val = 0
    val = 0
    #if length of hand is one, the score is simply that element
    if len(hand) == 1:
        for elem in hand:
            max_val = elem
    #if length of hand greater than one, loop through all pairs to determine score
    elif len(hand) > 1:
        for idx in range(len(hand) - 1):
            curr_dice = hand[idx]
            next_dice = hand[idx + 1]
            #add current dice value to total
            val += curr_dice
            #if the next dice does not equal this one and val is larger than max, rename as max
            if curr_dice != next_dice and val > max_val:
                max_val = val
            #if the current and next die equal and this is last iteration, add next dice value to total
            if curr_dice == next_dice and idx == len(hand) - 2:
                val += next_dice
                if val > max_val:
                    max_val = val
            #if on last iteration but next dice does not equal this one, rename max if next dice larger than current max
            elif curr_dice != next_dice and idx == len(hand) - 2 and next_dice > max_val:
                max_val = next_dice
            #if not on last iteration when dice do not equal, reset value to zero so unequal die are not added together
            elif curr_dice != next_dice:
                val = 0
            
    return max_val


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    count = 0
    total = 0
    #dice_range is tuple of all possible outcomes
    dice_range = tuple(range(1, num_die_sides + 1))
    #iterate through each possible outcome and calculate the score of each hand
    for combo in gen_all_sequences(dice_range , num_free_dice):
        #iterate the total and counter, at the end return the division of these two
        total += score(tuple(sorted(held_dice + combo)))
        count += 1
    
    return total / float(count)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    #create copy of tuple
    temp = set([()])
    holds = set([()])
    #create set with repeats (all elements are same but different order)
    for idx in range(0, len(hand) + 1):
        combos = tuple(gen_all_uniques(hand, idx))
        for combo in combos:
            temp.add(combo)
    #create set eliminating repeats by sorting so same element entries are eliminated
    for elem in temp:
        elem = tuple(sorted(elem))
        holds.add(elem)
        
    return set(holds)


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_val = 0
    hold_list = list(gen_all_holds(hand))
    #loop through each possibility of tuples where each element is a held dice
    for hold in hold_list:
        hand_copy = list()
        #loop through each tuple value and add it to the hand
        for elem in hold:
            hand_copy.append(elem)
        num_free_dice = len(hand) - len(hand_copy)
        hand_copy = tuple(hand_copy)
        #calculate the expected value of this holding combination
        hand_val = expected_value(hand_copy, num_die_sides, num_free_dice)
        if hand_val > max_val:
            #if expected value of holding combo is highest, name that holding combo and value as the new maxima
            max_val = hand_val
            best_hold = tuple(hand_copy)
        
    return (max_val, best_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 6, 6, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)