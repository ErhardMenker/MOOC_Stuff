#program to input numbers and extract smallest/largest number from list
largest = None
smallest = None #Default largest and smallest variable to type 'None'
while True : #loop only ends if a break condition is reached
    num = input("insert number here:")
    if str(num) is "done" :
        break #only exit loop if 'done' is inputted
    try :
        integer = int(num)
        if largest is None or integer > largest :
            largest = integer #store integer in largest if on first iteration or integer is largest so far
        if smallest is None or integer < smallest :
            smallest = integer #store integer in smallest if on first iteration or integer is largest so far
    except :
        print ("Invalid Input") #if input could not be typed as integer, print out "invalid input" message and reevaluate 'while condition'

print "maximum is", largest
print "minimum is", smallest