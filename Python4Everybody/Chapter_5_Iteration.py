###Chapter 5: Iteration###

    ##Updating Variables
        #Updating variables is common, such as setting x = x + 1. But this code will error out if x is not defined, or 'initialized'.
        #Updating a variable by adding 1 is called an 'increment' , subtracting 1 is a 'decrement'.
        
    ##The While Statement
        #While loops execute a body of code until a condition no longer holds, following the logic:
            #1) Evaluate the condition, yielding 'True' or 'False'
            #2) If the condition is false, exit the loop and exit the following statement after the while loop.
            #3) If the condition is 'true', execute the body of code and return to step 1.
        #The value in the loop that changes each time is the 'iteration variable'.
        #The iteration variable must both exist in the body code and eventually be false according to the condition, or the loop is an "infinite loop"
            n = 5 #initialize iteration variable n.
            while n > 0 :
                print (n)
                n = n - 1 #subtract 1 from n and set equal to n, go back to test condition
            print ("blastoff!") #executes once the condition on the iteration variable evaluates to false
        #A loop is an 'infinite loop' if the logical condition always evaluates to 'True'.
            n = 10
            while True : #condition will always hold as 'True' by definition, so execution never ends
                print (n)
                n = n - 1
            print ('done') #never printed because loop is never exited
        #A while loop is essentially a repeatedly executed if statement, where the body of code is executed as long as the condition holds
        #'Break' can be inputted into a loop and once this condition is recognized, the loop is exited.
            while True :
                line = input('>')
                if line = 'done' :
                    break
                print ('line') #executed for any input() other than 'done'. If 'done' is inputted, program recognizes 'break' and exits loop.
            print ('done') #to be printed when loop exiting occurs
        #The 'continue' command in a while loop immediately calls for leaving the body of the while loop and reevaluates the condition.
            while True:
                line = input('>')
                if line[0] == '#' : #if the first character in the input is '#'...
                    continue #...leave iteration and reevaluate condition
                if line == 'done'#if the user input is 'done'... 
                    break #...exit loop
             print ('Done!') #occurs after loop is broken
        
     ##Definite loops using 'for'
        #While loops are 'indefinite loops' because they continue to loop until a condition is false, so iteration amount may not be immediately known.
        #Looping through a defined list of things is a 'definite loop'. This occurs in a 'for loop'.
        #for and while loops are similar because there is a statement followed by a loop body.
        #for loops perform an iteration on an item in a list one at a time, until the list is exhausted and the loop is exited.
            friends = ['joseph' , 'sally' , 'liz']
            for friend in friends #select each string from this list, one at a time
                print ('hello',friend) #prints hello friend, for each name in the list
            print('im done!')
        #The iteration variable for for loops is the variable being assigned the individual names in the list.
        #The 'in' in the control statement is used to assign the iteration variable sequentially to the elements of the list being looped through.
        #'Break' and 'continue' can be used in for loops.
        
     ##Counting and Summing Loops 
        #Loops can be used to determine how many items are in a list (counting loop) and summing the items in a list (summing loop).
        #Counting Loop:
            count = 0
            for itervar in [3, 41, 12, 9, 74] :
                count = count + 1 #each iteration adds 1 to the list count, starting from a count of 0
            print ('Count:'), count
        #Iteration variables in a for loop that count elements in a list are 'counters'.
        #Summing Loop:
            total = 0
            for itervar in [3, 41, 12, 9, 74] :
                total = total + itervar #iteration variable directly used to be summed to by previous integers 
            print ('Total:), total
        #Iterator variables in a for loop that sum elements in lists are 'accumulators'. 
            
      ##Minimum and Maximum Loops
        #Loops can extract maxima and minima by selecting each element and setting it equal to the optimum if it exceeds all previous elements to that point
            largest = None
            print 'Before:', largest
            for itervar in [3, 41, 12, 9, 74, 15] :
                if largest is None or itervar > largest :
                    largest = itervar #set largest equal to the current iterated variable if 'None' is selected or it exceeds the previously found largest
                print 'Loop:', itervar, largest
            print 'Largest:', largest