# The index(x) method returns where number x first occurs in the given list, failing if that value does not occur.
lst = [1, 4, 42, 69, 42]
print(lst.index(42)) # returns 2, this is the index of this first occurring value

# The append(x) method appends the value of x to the end of the inputted list.
lst = [1, 4, 42, 69, 42]
lst.append(50) 
print(lst) # returns the list with 50 appended to the end

# The extend() method appends to the end of the list as individual elements the inputted list:
lst = [1, 4, 42, 69, 42]
lst.append([42, 69])
print(lst) # returns: [1, 4, 42, 69, 42, [42, 69]]
lst = [1, 4, 42, 69, 42]
lst.extend([42, 69]) # returns: [1, 4, 42, 69, 42, 42, 69]
# Note that append() method appends multiple listed elements as a nested list

# List concatenation can also occur by joining two lists with a '+' sign

# The reverse() method applied to a list reverses the order in which each element of the list appears

# The pop(i) method removes the i'th element from the list, defaulting to the last list element
lst = [1, 4, 42, 69, 42]
lst.pop(2)
print(lst) # removes the first occurring 42, returning: [1, 4, 69, 42]