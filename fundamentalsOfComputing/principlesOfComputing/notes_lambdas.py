###Anonymous Functions

# An anonymous function is a function with no name that is typically called on what would be a higher ordered functions and prefaced with "lambda"
# Anonymous functions operate on lists and execute an operation one element at a time, returning the elements in order.
# Lambdas only exist in the anonymous function in which they're called.
# Lambdas follow the form: func_name(lambda: input_name: f(input_name), list_operation)

data = [0, 1, 2, 3, 4, 5]
data3 = map(lambda x: x ** 2, data) #for each element x in data, square the element
print data3 #returns: [0, 1, 4, 9, 16, 25]

data = [1, 3, 6, 9, 18]
data4 = filter(lambda val: val % 2 == 0, data) #return an element only if it is even
print data4 #returns: [6, 18]

