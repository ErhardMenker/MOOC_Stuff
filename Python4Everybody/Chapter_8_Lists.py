###Chapter 8: Lists###

    ##A List is a Sequence
        #A string is a sequence of characters, but a list is a sequence of elements or items.
        #Like strings, lists can have variable names assigned to them.
        #A list is created by using square brackets '[]', and multiple elements are separated by a comma.
            x = [10, 20, 30, 40] #List x contains 4 scalar elements.
        #The elements of a list can be of any type, such as a string, integer, float, Boolean, another list, etc.
            ['spam', 2.0, 5, [10, 20]] #List contains 4 elements: a string, float, integer, and a list, respectively
        #A list that exists in another list is nested.
        #A list containing no elements is an empty list, created with empty brackets: '[]'
            cheeses = ['Cheddar', 'Edam', 'Gouda']
            numbers = [17, 123]
            empty = []
            print (cheeses, numbers, empty) #returns: '['Cheddar', 'Edam', 'Gouda'], [17, 123], []'
            
    ##Lists are Mutable
        #Just as the square bracket operator accesses the characters of a string, it is used to access the element of a list.
        #Zero based indexing is still used.
            cheeses = ['Cheddar', 'Edam', 'Gouda']
            cheeses[1] #returns 'Edam'
            cheeses[-2] #returns 'Edam'
            cheeses[3] #returns an error message, there is no 4th element to reference.
        #Lists are mutable (unlike strings) because the order of list items can be changed and list items can be reassigned.
            numbers = [17, 123]
            numbers[1] = 5 #reassign 2nd listed number to 5.
            print (numbers) #returns [17, 5]
        #Each valid index maps to one and only one of the elements in a list.
        #Referencing list elements that do not exist returns an "IndexError"
        #Calling negative list indices counts backwards from the end of the list.
        #The in operator tests whether a value is an element in a list
             cheeses = ['Cheddar', 'Edam', 'Gouda']
             'Edam' in cheeses #Returns 'True'
             'Swiss' in cheeses #Returns 'False'
            
    ##Traversing a List
        #A for loop through a list iterates through each element of the list, as a for loop through a string loops through each character.
            cheeses = ['Cheddar', 'Edam', 'Gouda']
            for cheese in cheeses :
                print(cheese) #prints out 'Cheddar' , 'Edam' , 'Gouda' , respectively
        #Updating list elements is easily done by referencing the indices of a list...
        #...this is easily done by using the 'range' and 'len' functions in conjunction. This returns a list of numbers from 0 to one less the list's length...
        #...by zero based indexing, looping through these indices will reference every element in the list.
             numbers = [17, 123]
             for i in range(len(numbers)) : #returns a list containing 0 through 1 
                numbers[i] = 2*numbers[i] #doubles each element
                print (numbers) #returns [34, 246]
        #A for loop through an empty list never executes the body because there are no iterations
        #When tabulating the amount of elements of a list, nested lists count only as one element
        
    ##List Operations
        #The '+' operator concatenates lists.
            a = [1, 3, 5]
            b = [7, 9, 11]
            c = a + b
            print (c) #returns [1, 3, 5, 7, 9, 11]
        #The '*' operator repeats the list by the amount of times the inputted argument is
            a = [1]
            a*4 #returns [1, 1, 1, 1]
            b = [7, 9, 11]
            b*2 #returns [7, 9, 11, 7, 9, 11]
            
    ##List Slices
        #The slice operator also works on lists, with integer inputs.
        #By zero based index, list_name[a:b] returns the elements of list_name starting from index a and up to but not including index b.
            a = ['foo', 'bar', 'norf', 'zong', 'jeremy', 'peterson']
            a[3:5] #returns: ['zong','jeremy']
        #Omitting the left index starts the slice from the beginning and omitting the second ends the slice at the end of sliced list.
            a[2:] #returns: ['norf', 'zong', 'jeremy', 'peterson']
            a[:3] #returns: ['foo', 'bar', 'norf']
        #It follows that omitting both slice arguments simply returns all elements of the sliced list
        #Inputting list arguments outside of their respective range does not error out, but acts as if no argument was inputted there.
            a[:1000] #returns entire list 'a'
        #Slice operators on the left side can act as a method to reassign list elements.
            t = ['a', 'b', 'c', 'd', 'e', 'f']
            t[1:3] = ['x', 'y'] #reassigns first and second element to respective values
            print(t) #returns ['a', 'x', 'y', 'd', 'e', 'f']
            
    ##List Methods
        #Python provides methods that operate on lists.
        #The append() method adds the inputted value as the last element of the list
            t = ['a', 'b', 'c']
            t.append('d') #tack on 'd' as the last element of list tabulating
            print(t) #returns: ['a', 'b', 'c', 'd']
        #The extend() method acts like append(), but adds a list to the last element of another list
            t1 = ['a', 'b', 'c']
            t2 = ['d', 'e']
            t1.extend(t2)
            print(t1) #returns: ['a', 'b', 'c', 'd', 'e'] (t2 is unmodified)
        #The sort() method arranges the elements of the list from lowest to highest
            t = ['d', 'c', 'e', 'b', 'a']
            t.sort()
            print(t) #returns: ['a', 'b', 'c', 'd', 'e']
        #Most list methods are void, meaning they modify the list and return none, so a variable should not be set equal to the method because it will equal 'None'.
        #In this sense, lists and strings are opposites. List methods operate on the list so the initial list is gone, unlike immutable strings.
        
    ##Deleting Elements
        #The pop() method deletes the element corresponding to the inputted argument's index and stores that in the variable name.
            t = ['a', 'b', 'c']
            x = t.pop(1) #remove the 1st element of t, storing it in x
            print(t) #returns: ['a', 'c']
            print(x) #returns: 'b'
        #If you don't need the removed value, the del operator works just fine.
            t = ['a', 'b', 'c']
            del t[1]
            print(t) #returns: ['a', 'c']
        #The remove() method removes the first instance of the inputted element from the list
            t = ['a', 'b', 'c']
            t.remove('b') 
            print(t) #returns: ['a', 'c']
        #Deleting multiple consecutive elements can be done with a slice operator
            t = ['a', 'b', 'c', 'd', 'e', 'f']
            del t[1:5] #deletes the 1st through the 4th indexed elements
            print(t) #returns: ['a', 'f']
    
    ##Lists and Functions
        #There are a number of built-in functions that perform standard procedures on lists:
            nums = [90, 100, 110]
            print (len(nums)) #returns: 3 (the number of elements in list)
            print (max(nums)) #returns: 110 (the largest element in the list)
            print (min(nums)) #returns: 90 (the smallest element in the list)
            print (sum(nums)) #returns: 300 (the total of the list elements)
        #A program can be created using lists to calculate the average of numbers:
            while True :
                numlist = []
                num = input('Enter number: ')
                if num = 'done' :
                    break
                try :
                    value = float(num)
                    numlist.append(value)
                except :
                    continue
            average = sum(numlist)/len(numlist)
            
    ##Lists and Strings
        #Strings can be partitioned into lists by letters by use of the list() function:
            s = 'spam'
            t = list(s)
            print(t) #returns: ['s', 'p', 'a', 'm']
        #Strings can be partitioned into lists by words by use of the split() method:
            s = 'pining for the fjords'
            t = s.split()
            print(t) #returns: ['pining', 'for', 'the', 'fjords']
            print (t[2]) #returns: 'the'
        #The default split() argument is to use a space delimiter, but others can be inputted:
            s = 'spam-spam-spam'
            delimiter = '-'
            s.split(delimiter) #returns: ['spam', 'spam', 'spam']
        #Split views multiple consecutive spaces as equivalent to one space.
        #The join() method takes a list argument and concatenates adjacent elements using the delimiter:
            t = ['pining', 'for', 'the', 'fjords']
            delimiter = ' ' #delimiter is everywhere a space exists
            delimiter.join(t) #returns: 'pining for the fjords'
        
    ##Parsing Lines
        #Parsing lines means looking through a block of text and finding sub-text that satisfies certain criteria
        #The split method is useful in separating text into a list and subsetting elements of interest
            fhand = open('mbox-short.txt')
            for line in fhand :
                line = line.rstrip() #remove white space on right side
                if not line.startswith('From ') :
                    continue #go to next iteration, don't care about this line
                words = line.split() #line must start with 'From ', create list using space delimiters
                print words[2] #print word of interest
                
    ##Objects and Values
        #Assigning multiple variables equal to the same string implies they are identical because that string is immutable.
            a = 'banana'
            b = 'banana'
            a is b #returns 'True'
        #However, by mutability of lists, this same identical property does not hold true for lists:
            a = [1, 2, 3]
            b = [1, 2, 3]
            a is b #returns 'False' because a and b are currently equivalent but not identical
        #Identical objects means that the value of the objects are equal, and changing one variable changes the other because equality always must hold.
        #Equivalent objects mean that the objects currently have the same value
        #Identical implies equivalent, but the converse does not always hold
        #An object has a value, and equal values for multiple objects implies equivalence.
        
    ##Aliasing
        #A variable referring to an object is the object's reference
            a = [1, 2, 3]
            b = a #a and b now refer to the same object
            b is a #returns: 'True'
        #In above, a and b refer to the same object. An object having multiple references means it is "aliased."
        #Changes made with one alias affect the other's value.
            b[0] = 17
            print(a) #returns [17, 2, 3]
        #Aliased strings are less problematic because strings are immutable, so their values won't change and cause associated confusion caused by aliasing.
        
    ##List Arguments
        #A function that modifies a list parameter is viewable:
            def delete_head(t) :
                del t[0]
            letters = ['a', 'b', 'c']
            delete_head(letters) #function operates on list letters, serving as placeholder for abstract list t.
            print(letters) #returns ['b', 'c']
        #Some operations modify lists, others create new lists entirely
            t1 = [1, 2]
            t2 = t1.append(3) 
            print (t1) #returns: [1, 2, 3] (t1 has been modified)
            print (t2) #returns: None (no list has actually been created_
            t3 = t1 + [3]
            print (t3) #returns: [1, 2, 3] (because new list has been created)
            t2 is t3 #returns false, because different list operations
        #It is possible to write a function that simply creates a new list and refers to that list subsequently:
            def tail(t) :
                return t[1:] 
            
        
        
            
            
                