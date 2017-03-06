import math

def mystery(sorted, lower, upper):
	'''
	what does this do?
	'''
	if lower > upper:
		return -1
	m = int(math.floor((lower + upper) / 2))
	
	if sorted[m] == m:
		return m
	else:
		if sorted[m] < m:
			return mystery(sorted, m + 1, upper)
		else:
			return mystery(sorted, lower, m - 1)

# application			
print mystery([-2,0,1,3,7,12,15],0,6)
print
print mystery([1, 2, 4, 6, 7000], 0, 4)