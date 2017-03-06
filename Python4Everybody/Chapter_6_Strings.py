###Chapter 6: Strings###

    ##String Introduction
        #A string is a sequence of characters.
        #Characters of a string can be subsetted one at a time with the bracket operator.
            fruit = "banana" #store string 'banana' in variable 'fruit'
            letter = fruit[1] #stores the character at index position one in fruit variable into the variable 'letter'
            print(letter) #returns 'a' because...
        #...Python operators with zero based indexing, so subsetting the zero-eth entry returns the first character in a string.
            fruit = "banana"
            letter = fruit[0]
            print(letter) #returns 'b'
        #Negative indices count backward from the end of the string.
            fruit = "banana"
            fruit[-1] #returns the last letter, 'a'
            fruit[-2] #returns the second to last letter, 'n'
        #By the countability of string characters, the index subsetting a string must be an integer.
            fruit = "banana"
            letter = fruit[1.5]
            print(letter) #syntax error
            
     ##String Concatentation
        #String concatenation is the process of joining two strings from end to end
        #Python will not place a space between concatenated strings unless it is explicity commanded to do so with an empty string serving as a space
            a = "Hello"
            b = " There"
            print(a+b) #returns 'Hello There'
        #Strings can be concatenated using the ',' or the '+' operators:
            #The ',' concatenator keeps quotes around each concatenated strings, and bounds the outer strings in parenthesis
            #Calling print around the ',' concatenator strips the ending parenthesis, strips all quotes/commas, and puts a space before each concatenated operand
            #The '+' concatenator strips quotes around the inner concatenated strings, and does not show '+' in output.
            first = 'how are you '
            second = 'my man?'
            first + second #returns: 'how are you my man?'
            first, second #returns: ('how are you ', 'my man?')
            print(first, second) #returns: how are you  my man? (should omit ending whitespace with rtrim method in variable 'first')
            
     ##Getting the length of a string using 'len' :
        #'len' is a built in function that returns the number of characters in a string
            fruit = "banana"
            len(fruit) #returns '6'
        #Because of zero based indexing in Python, the last character in a string is indexed as one less than the length of the string:
            fruit = "banana"
            length = len(fruit)
            last = fruit[length-1] #subsets integer one less than the amount of characters in string 'fruit' in variable 'last'
            print (last) #prints the last letter, because zero based indexing means last character is subsetted
            
     ##Traversal through a string with a loop
        #A 'traversal' occurs when the characters of a string are looped through, with an operation occurring each time.
            fruit = 'banana'
            index = 0 #initialize iteration variable 'index' equal to 0
            while index < len(fruit) : #conditional code
                letter = fruit[index] #starting with the first character in 'banana', print off the character
                index = index + 1 #change iteration variable so condition eventually becomes False
        #Strings can also be traversed by use of for loops :
            fruit = 'banana'
            for char in fruit
                print (char) #print each character in 'fruit' consecutively, ending when characters are exhausted
     
     ##String Slices
        #A segment of a string is called a 'slice'. Selecting a slice is like selecting a group of consecutive characters.
            s = 'Monty Python'
            print s[0:5] #returns 'Monty'
        #The operator <string_name>[n:m] returns, inclusively, the characters of the string from the (n+1)-eth to the m-eth character.
            james = 'the_freaking_man'
            james[0:3] #returns the 1st, 2nd, and 3rd character
        #Ending a string subset call with an index exceeding the length of the string is the same as omitting the upper bound
        #Omitting the lower bound of the index (before the colon) starts the slice at the beginning of the string (equivalent to inputting '0' as start of index)
            fruit = 'banana'
            fruit[:3] #returns 'ban'
        #Omitting the upper bound of the index (after the colon) ends the slice at the last character (same as inputting one less than length of the string as end of index)
        #If the first index is greater than or equal to the second index, an empty string results.
            fruit = 'banana'
            fruit[3:3] #would show characters of string from fourth position to the third, negative range results in empty string
        #Empty strings contain no characters and have length zero, but have same general qualities as other strings
        
    ##Strings are Immutable
        #It is not possible to use the '[]' operator to change a string's character(s) because strings are 'immutable'.
            greeting = "Hello world!"
            greeting[0] = 'J' #errors out, because strings are immutable and program tried to directly change variable definition of string
        #'Immutability' means that an existing string cannot be changed, but new strings can be made as variations on the original.
            greeting = "Hello World!"
            end_word = greeting[1:len(greeting)] #Returns all but first character in variable "greeting", "ello World!" 
            new_greeting = "J" + end_word #Concatenates string "J" to start of "ello World!"
            print(new_greeting) #Returns "Jello World!", old string in variable "greeting" is unaltered
            
    ##Looping and Counting
        #The following program counts how many times 'a' occurs in a string :
            word = 'banana'
            count = 0
            for letter in word :
                if letter == "a"
                    count = count + 1 #add a number to the count every time an 'a' appears in the string
            print (count)
            
    ##The In Operator
        #The word 'in' is a Boolean operator that returns 'True' if the first string appears as a substring of the second string, "False" otherwise
            'a' in 'banana' #returns "True", 'a' appears in 'banana'
            'bann' in 'banana' #returns "False", 'bann' does not appear in 'banana'
            
    ##String Comparison
        #The comparison operator works on strings.
        #To see if two strings are equal:
            if string_a = 'banana' :
                print ('variable banana has string string_a stored in it')
        #To see if a string is alphabetically before another string:
            if word < 'banana' :
                print ('word' is alphabetically before 'banana')
            elif word > 'banana' :
                print ('word' is alphabetically after 'banana')
            else :
                print ('strings maintain equivalency')
                
     ##String Methods
        #Strings are example of Pythonic 'objects'.
        #An 'object' contains both data (in a string's case, the string's characters) and methods (functions built specific to the object in question).
        #Python has a function called 'dir' which lists the methods available for an object based on its type.
        #The 'type' function shows the type of an object and the 'dir' function shows the available methods.
            stuff = 'Hello world!'
            type(stuff) #shows the type of this variable to be a string
            dir(stuff) #shows the methods available to strings such as testing upper caseness of the letters
        #Calling a method is similar to calling a function but with different syntax.
        #'Methods' are called by appending the method name after the variable name with a period delimitor between.
            word = 'banana'
            new_word = upper(word) #function that converts word's characters to upper case
            new_word = word.upper() #method that converts word's characters to upper case, with empty parenthesis showing no arguments to be specified 
        #Method calls are called 'invocations', with the terminology of invoking a proc on an object (invoking upper on the word).
        #The string method 'upper' and 'lower' convert a string to all upper and lower case characters, respectively
            greet = 'Hello Bob'
            print (greet.lower()) #returns 'hello bob'
            print (greet.upper()) #returns 'HELLO BOB'
            print (greet.capitalize()) #returns 'Hello bob' #'capitalize' method capitalizes the first character in a string
        #The string method 'find' searches the position a substring first occurs in a grander string.
            word = 'banana'
            index = word.find('a') #finds first index point where 'a' occurs in string 'banana'
            print (index) #returns 1, by zero based indexing
            word.find('na') #returns 2, by zero based indexing
        #The 'strip' method removes white space (spaces, tabs, or newlines) from the beginning and end of a string.
            line = '        get ready cuz here we go         '
            line.strip() #returns 'get ready cuz here we go'
            line.lstrip() #returns 'get ready cuz here we go         '
            line.rstrip() #returns '        get ready cuz here we go'
        #The method 'startswith' returns Boolean value 'True' if a string starts with a substring, 'False' otherwise
            line = 'Please have a nice day'
            line.startswith('Please') #returns 'True', mother string in variable line starts with 'Please'
            line.startswith('p') #returns 'False', mother string starts with 'P', not 'p'.
            
        ##Parsing Srings
            #String parsing involves extracting a substring from a string
            #String slicing is the methodology of extracting a portion of a string to create a substring
                #Goal: parse a string by returning a substring with characters after the '@' sign, before the next space
                data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
                atpost = data.find('@') #method storing position of @ sign in string in variable 'atpos'
                print (atpos) #returns 21
                sppos = data.find('',atpos) #returns first space at the position after the @ position
                print (sppos) #returns 31
                host = data[atpos+1:sppos] #parses data string between necessary range, adding one to lower bound to exclude the '@' sign
                print (host) #returns 'uct.ac.za'
                
        ##Format Operator
            #The format operator, '%', allows the construction of strings and to replace parts of strings with data stored in those variables
            #The first operand is the format string, which contains one or more format sequences that specify how the second operand is formatted. 
            #The result of a format string is a string.
                camels = 42
                '%d' % camels #returns the string '42'
            #These operators have special meanings, where...
                # %d formats integers into strings
                # %g formats floating points into strings
                # %s formats strings into strings
            #The type of value being formatted must be interpretable as the type being coerced from (to apply %g, value must be interpreted as float).
                'In %d years I have spotted %g %s.' % (3, 0.1, 'camels') #Returns 'In 3 years I have spotted 0.1 camels.'
                '%d' % 'dollars' #error, dollar cannot be interpreted as float