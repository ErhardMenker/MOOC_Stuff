### Quadratic Sort

# A brute force sort algorithm would be solvable in a permutation amount of time; can be much better.
# A simple sorting algorithm works in O(n**2)

def quadratic_sort(l):
	'''
	sort list l in quadratic time
	'''
	# initialize the sorted list to be returned
	l_sort = list()
	# while there are still numbers in l...
	while len(l) > 0:
		# initialize min to an arbitrarily large number
		min = float("inf")
		# go through each element in l and iteratively find the minimum
		for elem in l:
			if elem < min:
				min = elem
		# remove the minimum from the list 
		l.remove(min)
		# append the minimum to the returned list
		l_sort.append(min)
	return l_sort

# example	
print quadratic_sort([3, 1, 5, 15, 69, 420, 42])
	