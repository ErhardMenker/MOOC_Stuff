### Linear and Binary Search

# Searching is the art of finding a key in a list of values and returning the index.

def linear_search(x, l):
	'''
	find if element x is in list l and return the index
	'''
	idx = -1
	for elem in l:
		# increment the index
		idx += 1
		# if x is equal to the iterated element, return the index
		if x == elem:
			return idx
	# if we iterated through the whole list and there were no matches, return -1 to show x not in list
	return -1
	
print linear_search(3, [1, 2, 4, 5]) # returns index of -1
print linear_search(3, [1, 2, 4, 5, 3]) # returns index of 4

# The above algorithm executes in linear time because up to every element in a list of length n is searched.

# More efficient searching algorithms can be executed on lists that are already known to be sorted.
# Binary search searches the midpoint of a sorted data structure and continues to search the midpoints.
# The run time of binary search is O(log(n)).
# Conducting linear search is more efficient than sorting and then doing binary search, since linear is O(n) and binary mergesort is O(n*log(n)).