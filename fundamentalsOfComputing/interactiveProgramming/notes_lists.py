## List Intro
# Lists give the capability of referring to multiple objects separately stored within one variable.
# Lists store zero or more elements together, separated by commas.

## Different List Types
# Element types in lists can include an arbitrary mixture of Booleans, strings, integers, floats, and even embedded lists, etc...
# ...but programming convention holds that lists should just include one 'type'
# An empty list stores zero elements can be created by empty brackets: []
# Non-empty lists can be created by storing all of the elements in outer brackets, [], and separating individual elements by commas.

# Fun With Lists

# Create:
mt_list = []
print(mt_list) # returns empty brackets

l = [1, 3, 4, -7, 62, 43]
print(l) # returns the above list

l2 = ['milk', 'eggs', 'bread', "butter"]

l3 = [[3, 4], ['a', 'b', 'c'], []]
print(len(l3)) # returns 3, there are 3 elements in the list (does not matter how many elements are in nested lists)

# Subsetting Lists
# Printing out the list by subsetting a position in square brackets returns that value, conditioned on that index existing (else there is an error) using zero-based indexing (as always)
l = [1, 3, 4, -7, 62, 43]
print(l[3])# returns: -7
# Inputting a negative number indexes backwards from the end of the list, where -1 corresponds to the last list element.
print(l[-2]) # returns: 62
# Subsetting a range of a list returns the first specified element up to but not including the second element specifying the range.
print(l[:3]) # returns: [1, 3, 4]

# Updating Lists
# Lists are mutable, meaning that values can be reassigned by assigning an element of the list (using list subsetting) to something else.
cheeses = ['gouda', 'cheddar', "swiss"]
cheeses[1:3] = ['pepperjack', "provolone"]
print(cheeses) # returns: ['gouda', 'pepperjack', 'provolone']

