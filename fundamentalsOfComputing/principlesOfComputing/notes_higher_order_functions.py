## Higher Order Functions
# Higher order functions are functions that take other functions as inputs.

def double(val):
	return 2 * val
	
def square(val):
	return val ** 2

def twice(func, val):
	return func(func(val))
	
print(twice(double, 3)) #returns 12, executes the double function twice
print(twice(square, 3)) #returns 81, because square(val) is executed twice

data = [1, 3, 6, 9, 18]
[double(item) for item in data]
print(data) #returns a list data with each element doubled

#The map(func, list_name) function takes each element in list, list_name, and performs an operation defined by func on it.
newdata2 = map(double, data) 
print(newdata2) #returns a list data with each element doubled 

#The filter(func, list_name) only returns elements in list_name that are True when the function func is executed.

def even(val):
	if val % 2:
		return False
	else:
		return True
		
newdata3 = filter(even, data)
print(newdata3) #returns 6 and 18, as they are the only input values that map to True

def area(func, low, high, stepsize):
	
	"""
	function that approximates an integral where stepsize is the calculus h whose limit approaches zero
	"""
	
	total = 0.0
	loc = low
	while low < high:
		#take the function name and operate on the current input, multiplying by the stepsize width
		total += func(loc) * stepsize
		loc += stepsize
	
	return total
	
	def g(x):
		
		"""
		raise x to the second power
		"""
		
		return x ** 2
		
	print(area(g, 0, 10, 0.0001) #returns 333.33833, a close approximation to true value 333.33333