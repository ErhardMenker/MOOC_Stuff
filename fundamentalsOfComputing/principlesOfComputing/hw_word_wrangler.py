# 75% 

"""
Student code for Word Wrangler game (gen_all_strings from elsewhere)
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    
    output = list()
    
    if len(list1) == 0:
        output = []
    elif len(list1) == 1:
        output = list1[:]
    elif len(list1) > 1:
        for idx in range(len(list1) - 1):
            #append this element onto the end of the list if unequal to the next...
            if list1[idx] != list1[idx + 1]:
                output.append(list1[idx])
            #append last item regardless, if duplicated in initial list none of smaller index instances would have been added
            if idx == (len(list1) - 2):
                output.append(list1[idx + 1])

    return output

def intersect(list1, list2):
    
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    
    intsct = list()
    #If an element in list1 is in list2, then it intersects so append it to output list
    for elem in list1:
        if elem in list2:
            intsct.append(elem)
    
    return intsct

# Functions to perform merge sort

def merge(list1, list2):
    
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
    
    #return an empty list if both input lists are empty
    if max(len(list1), len(list2)) == 0:
        return []
    
    mrg = list()
    
    #calculate the minimum/maximum values in each list
    min_val = min(list1 + list2)
    max_val = max(list1 + list2)
    
    #loop through each value between the max and min, inclusive... 
    #...append to mrg however many times it appears
    for elem in range(min_val, max_val + 1):
        for _ in range(list1.count(elem)):
            mrg.append(elem)
        for _ in range(list2.count(elem)):
            mrg.append(elem)
            
    return mrg
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """ 
    
    #if list is zero or one length, it is already "sorted" and should thus be returned as is
    if len(list1) <= 1:
        return list1
    
    #if list is longer than zero or one elements, divide it in half and apply the merge() function defined; return this
    #partition list1 into two halves
    mid = len(list1) / 2
    lst_half1 = list1[:mid]
    lst_half2 = list1[mid:]
    
    return merge(lst_half1, lst_half2)
            
        


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    
    #credit to: balakirevs
    
    #if string is empty, then return the empty string and be done
    if word == "":
        return [""]
    
	#divide a string into the first character and the rest
    head = word[0]
    tail = word[1:]
    #call this function on the remaining words
    rest_strings = gen_all_strings(tail)
    #initialize new strings list to empty list
    new_strings = []
    #for each string in the new_strings list...
    for string in rest_strings:
        #if the length is zero, add the letter to the list and move on
        if len(string) == 0:
            new_strings.append(head)
            continue
        length = len(string)
        #append the letter at each point in the string
        new_list = [string[:idx] + head + string[idx:] for idx in range(length + 1)]
        #append the new string to the output
        new_strings.extend(new_list)
    rest_strings.extend(new_strings)
    return rest_strings
    

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

print gen_all_strings("ab")

#print merge_sort([12, 7, 8, 9])

#print merge([7, 10, 15], [10]) 
#print merge([0, 1, 2], [0, 1, 2])
#print merge([0, 0, 1, 3, 4], [0, 1, 2, 5])

#print remove_duplicates([1, 2, 3, 3, 4, 4, 4, 4, 90, 90])

#print intersect([0, [0, 2], [0, 3], 2, 4, 9], [[0, 3], 0, 3, 5, 9])