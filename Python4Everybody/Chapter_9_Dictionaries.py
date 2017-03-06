###Chapter 9: Dictionaries###

    ##Dictionary Introduction
        #A dictionary is a more general version of the list, because indices can be almost anything (not just numbers).
        #A dictionary is an associative array, or a mapping between a set of indices (called keys) and values.
        #The association of a key and a value is a key-value pair (or an item).
            eng2sp = dict() #create a dictionary called 'eng2sp' (translates words)
            eng2sp["one"] = "uno"
            eng2sp["two"] = "dos"
            print(eng2sp) #returns: {'one': 'uno', 'two': 'dos'}
        #The order of items in a dictionary are unpredictable, which is not problematic because keys are used instead of unalterable integer indices.
        #A key reference that is not in the dictionary results in a "KeyError".
        #The len function returns the amount of key-value pairs there are in the dictionary.
        #The in operator tells whether something appears as a key in the dictionary.
            "one" in eng2sp #returns 'True'
            "uno" in eng2sp #returns 'False'
        #To see whether something appears as a value in a dictionary, use the values() method to return a list of values and then use the in function on that list.
            vals = eng2sp.values()
            "uno" in vals #returns 'True'
        #Python dictionaries are searched with a hash table, meaning that it takes about the same amount of time to search an element no matter how many items are in the dictionary.
        #Dictionaries are Python's most powerful data collection allowing fast database-like Python operations.
        
    ##Dictionary as a Set of Counters
        #An implementation is the method used to perform a computation.
            #Calculate how many times each letter appears in a string by mapping each letter to the amount of times it ultimately occurs:
            word = 'brontosaurus'
            d = dict() #initialize empty dictionary
            for c in word : #loop through each letter of string
                if c not in d : #if letter not in dictionary...
                    d[c] = 1 #...map that letter equal to one instance
                else : #if letter is in dictionary...
                    d[c] = d[c] + 1 #...add another instance of that letter in list
            print (d) #prints out histogram of how many times each letter occurs
        #The get() method takes a key and default value and searches through a dictionary and returns an inputted default value if element is not in dictionary.
            counts = { 'chuck' : 1, 'annie' : 42, 'jan' : 100}
            print (counts.get('jan',0)) #returns '100', the value of key 'jan'
            print (counts.get('tim', 0)) #returns default '0', because key 'tim' does not exist
        #The get() method can make counting each letter more compact:
            word = "brontosaurus"
            d = dict()
            for c in word :
                d[c] = d.get(c,0) + 1 #if letter does not exist, map letter to 1. else, increment previous letter's value by one.
            print(d)
            
    ##Dictionaries and Files
        #Dictionaries can be used to count the occurrence of words in a file with some written text.
            fhand = open("mbox.txt")
            counts = dict()
            for line in fhand : #loop through each file line
                words = line.split() #split all of the words in iterated dictionary line into individual list elements
                for word in words : #loop through each word
                    if word not in count : #if word not in dictionary...
                        counts[word] = 1 #...initialize sighting of word equal to one time
                    else : #if word is in dictionary already...
                        counts[word] += 1 #...add another sighting of that word in the dictionary
            print(counts)
        
    ##Looping and Dictionaries
        #Looping through a dictionary traverses its keys.
            #Print all values in a dictionary greater than 10:
            counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
            for key in counts : #for each key in the dictionary...
                if counts[key] > 10 : #...if its corresponding value is greater than 10...
                    print (key, counts[key]) #...print the key and the corresponding value
        #Keys can be sorted by using the keys() method available for dictionary objects.
            counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
            list = counts.keys() #extracts all keys and stores them in a list
            print(list) 
            list.sort()
            for key in list : #for element in sorted list...
                print(key, counts[key])  #...print the key and its assorted value.
        #The values() method sorts the values in a dictionary, and this will actually correspond to the ordered output from the keys() method.
        #The items() method maps a pair of key-value pairs called a 'tuple'.
        #The items() method allows two iteration variables to be used in a loop, looping through each key value pair in a dictionary subsequently.
            counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
            for keys , values in counts.items() : #for each respective key-value pair....
                print(keys , values) #...print the key and value
            
    ##Advanced Parsing
        #In reality, text has punctuation and capitalization, and Python does not view words varying in these respects as equal.
            #Parse text and count occurrence of each word, accounting for capitalization/punctuation:
            import string #allows calling of certain string methods
            fhand = open('mbox.txt')
            counts = dict() #initialize empty dictionary
            for line in fhand : #loop through each line of file
                line = line.translate(None, string.punctuation) #delete all elements from the line that are in 'string.punctuation' (includes ! , . etc)
                line = line.lower() #convert all text in file line to lower case
                words = line.split() #split each word in iterated line into element of a list
                for word in words : #iterate through list of word elements
                    if word not in counts #if word is not in dictionary...
                        counts[word] = 1 #...word is mapped to one occurrence
                    else : #word is in dictionary already...
                        counts[word] += 1 #add an instance to the value of that word's mapping
                print(counts)
                
            
        