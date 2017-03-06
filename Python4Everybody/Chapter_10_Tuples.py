###Chapter 10: Tuples###

    ##Tuple Introduction
        #A tuple is a sequence of values (much like a list is).
        #Like a list, tuple element values can be any type and are indexed by integers.
        #Unlike lists, tuples are immutable.
        #By the immutability property of tuples, many operations such as 'append()' and 'sort()' are not allowed.
            dir(tuple()) #shows only properties allowed for immutable objects.
            dir(list()) #shows operations allowed for general (immutable) objects, and mutable objects (such as append() and sort()).
        #Therefore, any operation that can be done on tuples can be done on lists, but the converse does not hold.
        #Tuples are comparable (elements can be tested for ordinality) and hashable (has a hash function).
        #A tuple is a comma-separated list of values:
            t = 'a', 'b', 'c', 'd', 'e'
        #Pythonically, tuples should be enclosed in parentheses to allow quick tuple identification.
            t = ('a', 'b', 'c', 'd', 'e')
        #A single element tuple must include the final comma, lest it be interpreted as a string:
            t1 = ('a',)
            type(t1) #returns: <class 'tuple'>
        #An empty tuple can be created by declaring 'tuple()'
            t = tuple()
            print (t) #returns an empty tuple
        #If the tuple() input is a sequence (string, list, or tuple), the result is a tuple with the elements of a sequence.
            t1 = tuple('lupins')
            print(t1) #returns: ('l', 'u', 'p', 'i', 'n', 's')
            t2 = tuple(['erhard', 3.1415192654, 69, ['jeremy', 'foo bar']])
            print(t2) #returns: ('erhard', 3.141592654, 69, ['jeremy', 'foo bar'])
        #A tuple should not be used as a variable name because it is the name of a constructor.
        #Many list operators work on tuples including bracket indexes (with zero based indexing) and slice operators:
            t = ('a', 'b', 'c', 'd', 'e') #initialize MWE tuple values
            print(t[0]) #returns: 'a'
            print(t[1:3]) #returns: ('b', 'c')
        #By the immutability property of tuples, attempts to reassign tuple elements within a tuple will result in error:
            t[0] = 'f' #returns: TypeError (because an operation was attempted which is not supported by the tuple object)
        #Tuple elements cannot be modified, but they can be altered in an operation producing a new tuple:
            t = ('a', 'b', 'c', 'd', 'e') #initialize MWE tuple values
            t = ('A') + t[1:] #concatenate 'A' to the beginning of tuple t, but with the first element dropped.
            print(t) #returns: ('A', 'b', 'c', 'd', 'e')
            d = {'a':10, 'b':22, 'c':1}
            t = sorted(d.items()) #guarentees that the key-value pairs will be sorted, while simply calling d.items() does not
            print(t) #returns: [('a',10), ('b', 22), ('c', 1)]
    ##Comparing Tuples
        #The comparison operator works with sequences, which includes tuples.
        #Python compares the first element from each sequence and only compares the next element if equality holds.
        #Once the first corresponding element from the tuples do not equal, the inequality is decided and no further comparison occurs.
            (0, 1, 20000000) < (0, 3, 4) #returns: True (The 0th elements are equal, so go on to 1st element where 1 is less than 3)
        #The 'sort function' works in similar fashion: it looks for ordinality in the first element, but progresses sequentially by element order until the tie is broken.
        #This sequential ranking feature of pattern leads to the pattern called DSU, which stands for...
            #'Decorate' a sequence by building a list of tuples with one or more sort keys preceding the elements from the sequence.
            #'Sort' the list of tuples using the Python build-in 'sort function'.
            #'Undecorate' by extracting the sorted elements of the sequence. 
                #Build an algorithm that sorts a list called 'word' from longest to shortest:
                def sort_by_length(words): #create a function called 'sort_by_length'.
                    t = list() #initialize an empty list.
                    for word in words: #For every word in the list...
                        t.append((len(word), word)) #...append to the end of list t a tuple element which contains a word's length and the word's characters, respectively.
                    t.sort(reverse=True) #Once words/word lengths are all appended to t, sort list t in descending order.
                    res = list() #initialize another empty list.
                    for length, word in t: #for each word length and word in sorted list...
                        res.append(word) #...append the word onto the new list, discarding the length of the word which was used to sort.
                    return res
    
    ##Tuple Assignment
        #A 'data structure' is a collection of related values, often organized in lists, dictionaries, tuples, etc. 
        #'Compound data structures' occur when there are multiple mappings creating multiple data structures, such as a list of tuples or dictionaries that contain tuples as keys and lists of values. 
        #Python allows a tuple on the LHS of an assignment statement (a "tuple assignment"), allowing the assignment of more than one variable at a time when the LHS/RHS are sequences.
            m = ['have', 'fun']
            x, y = m #sets x equal to m[0], and y equal to m[1]
            print(x) #returns: 'have'
            print(y) #returns: 'fun'
        #The amount of variables on the LHS and RHS must be equivalent for Python not to error out, if there are more than one LHS variables (aka: LHS uses variables in tuples form)...
        #...errors resulted from inequality in symbol-value pairs in tuple assignments are called 'shape errors', which result when the type, size, and composition of the symbol-value pairs don't harmoniously correspond.
        #This means the amount of elements in the tuples must be equivalent on both sides.
        #In above example, it would error out to input: x, y, z = m , because there are only two elements in m to assign variables to.
            m = ['have', 'fun']
            (x, y) = m
            print(x) #returns: 'have'
            print(y) #returns: 'fun'
            x, y = y, x #now x maps to 'fun' and y to 'have'
        #Both sides of these statements are tuples, but the LHS is a tuple of variables while the RHS is a tuple of expressions.
        #More sophisticated use of tuples can be implemented to parse data:
            addr = 'monty@python.org'
            uname, domain = addr.split('@') #RHS splits email using '@' as a delimiter. uname is the string before the '@', domain is that which is after.
            
    ##Dictionaries and Tuples
        #Dictionaries have a method called items that return a list of tuples, where each tuple is a key-value pair.
            d = {'a':10, 'b':1, 'c':22} #initiate a dictionary mapping with keys equal to a single letter mapping to corresponding number values.
            t = d.items() #produces a list of tuples
            print (t) #returns corresponding key value pairs in a 'random' order.
            t.sort() #sorts list of tuples
            print(t) #returns the new list in ascending alphabetical order by key value (so the 'a' key-value pair first, followed by 'b' and 'c', respectively)
            
    ##Multiple Assignment with Dictionaries
        #The items() method used on a dictionary input returns a list of tuples, where each tuple is a key-value pair in the dictionary.
        #Combining the items() method, tuple assignment, and for yields a nice code pattern for traversing the keys and values of a dictionary in a single loop:
            for key, val in d.items():
                print val, key #goes through each key-value pair in a list of tuples, and prints the corresponding output for each iteration.
        #The loop above has two iteration variables, where each of the iteration variables loops through the respective class of the key-value pair.
        #It is possible to combine these methods and loop through the value in a sorted (alphabetical) fashion:
            d = {'a':10, 'b':1, 'c':22} #initiaze dictionary with 3 key-value pairs
            l = list() #initialize empty list
            for key, val in d.items(): #convert dictionary into a list of key-value tuples.
                l.append((val,key)) #append each value and key as an element in list 'l'.
            l #prints out list of tuples with value (number) first, followed by the key (letter)
            l.sort(reverse=True)
            print(l) #returns the list of tuples sorted by the value first, then the key.
        #Note that in the above example, sorting did not error out because it was performed directly on a list. That list just happened to contain tuples which individually are not sortable (by immutability).
        #Lists of tuples can be looped through to print the ten most common words in a text:
            import string #allows additional string methods to be used
            fhand = open('romeo-full.txt') #create file handle called 'fhand' to refer to 'romeo_full' text file
            counts = dict() #initialize empty dictionary
            for line in fhand: #for every line in the file...
                line = line.translate(None, string.punctuation) #remove punctuation so words with punctuation are equivalent as the same words without
                line = line.lower() #lower case all words, so capital and lower case words are treated equivalently
                words = line.split() #split each line into a list of words, using space as a delimiter.
                for word in words: #for every word in the file...
                    if word not in counts: #if the word has not been added to the dictionary...
                        counts[word] = 1 #...create a key of that word in the dictionary and initialize its value to one.
                    else: #if word is already a key in the dictionary...
                        counts[word] += 1 #...add an instance of that word to the value in the dictionary.
            lst = list() #initialize an empty list
            for key, val in counts.items(): #for every key value pair in the list of tuples...
                lst.append((val, key)) #...tack on the value-key pair (in that order) to the end of list called 'lst'.
            lst.sort(reverse=True) #sort that list from largest to smallest number (corresponding to amount of times the corresponding key was observed)...
                                   #...if there is an equivalence in occurrence, then the sort occurs alphabetically by the key value. 
            for key, val in lst[:10]:
                print key, val #print off the 10 most common words in the file, with its corresponding count. 
                
    ##Using Tuples as Keys in Dictionaries
        #Since tuples are hashable but lists are not, if we want to create a composite key to use in a dictionary we must use a tuple as the key.
        #A composite key is written to map multiple keys to one value.
            #An example of a composite key is to map a last and first name pair to a telephone number:
            directory[last,first] = number #the expression in brackets is a tuple.
            for last, first in directory: #for every last and first name (respectively) in the directory...
                print (first, last, directory[last,first]) #...print out the iterated first and last name and its respective mapped output (that person's phone number)
                
    ##Generalizing Sequence Properties
        #In many contexts, the different sequence types (strings, lists and tuples) can be used interchangeably. When should each type be preferred?
        #Strings are not be used when their limits (the immutability property and elements needing to be characters) pose problems for the needed project.
        #Lists benefit from being mutable, but tuples are advantageous because they are more efficient in terms of memory used. 
        #When temporary variables are made, tuples are typically preferred to lists.
        #Lists are more common than tuples (since they are mutable), but in some contexts tuples are preferable:
            #It may be syntactically simpler to create a tuple than a list (like in a return statement)
            #Tuples are useful in using a sequence as a dictionary key (by the immutable property)
            #Passing a sequence as an argument to a function makes tuples more preferable, reducing the potential for unexpected behavior due to aliasing.
        #Because tuples are immutable, they don't provide methods like sort() and reverse() which modify existing mutable lists...
        #...however, Python provides built-in functions sorted and reversed which returns a new list with the same elements in a different order.
            
        
                    
        