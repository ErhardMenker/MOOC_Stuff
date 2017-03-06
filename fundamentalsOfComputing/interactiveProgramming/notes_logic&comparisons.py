###LOGIC AND COMPARISONS###

##A Boolean is a "type" of Python data structure, which can only evaluate to True if a statement is true or False if not.
    # '>' returns True if the left value is larger than the right value, False otherwise
    # '>=' returns True if left value is greater than or equal to the right value, False otherwise
    # '<' returns True if the left value is smaller than the right value, False otherwise
    # '<=' returns True if the left value is less than or equal to the right value, False otherwise
    # '==' returns True if the left and right values are equivalent, false otherwise
    # '!=' returns True if the left and right values are not equivalent, false otherwise

##Booleans can be derived from comparing strings to strings or numericals to numericals:
    x = 4 
    y = 5 # initialize numerical values
    x >= y # returns False by basic numerical ordinality
    x != y # returns True, these values do not equal
    word_a = "Python"
    word_b = "Java"
    word_a >= word_b #returns True, because the first letter in 'Python' is greater than in 'Java'
    
##Logical Booleans can be tested using the "or", "and", "not" qualifiers.
    #'and' only evaluates to true if all of the Booleans evaluate to True.
    #'or' only evaluates to true if at least one of the Booleans evaluates to True.
    #'not' negates the Boolean it is applied to, so a statement that was True evaluates to False and a statement that was False evaluates to True
    x = 4
    y = 5
    word_a = "Python"
    word_b = "Java"
    y >= x and word_a < word_b #evaluates to False, y is larger than x but word_b starts with smaller letter than word_a, so one of the conditions does not hold
    y >= x or word_a < word_b #evaluates to True, by virtue of the fact that at least one condition holds
    y >= x and not word_a < word_b #evaluates to True, because the first condition holds and the negation of the second condition also holds
    
    