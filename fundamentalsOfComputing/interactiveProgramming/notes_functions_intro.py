# PYTHON FUNCTIONS

# computes the area of a triangle
def triangle_area(base, height):     # header - defines output as function of inputs (ends in colon)
    area = (1.0 / 2) * base * height # body - stipulates how output is function of inputs(all of body is indented)
    return area                      # body - call to return outputs value. any code that exists after the call to return in a Python function is ignored

# no code is executed until the function is called with actual inputs:

a1 = triangle_area(3, 8) #variable a1 equals the output based on function and inputs
print a1
a2 = triangle_area(14, 2)
print a2

# a function is a 'blackbox', because inputs map to outputs with machine level code operating in background

# converts fahrenheit to celsius
def fahrenheit2celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius

# test!!!
c1 = fahrenheit2celsius(32)
c2 = fahrenheit2celsius(212)
print c1, c2

# functions can be nested!:

# converts fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit) #extracts celsius input and...
    kelvin = celsius + 273.15 #...adds 273.5 to celsius equivalent to find kelvin
    return kelvin

# test!!!
k1 = fahrenheit2kelvin(32)
k2 = fahrenheit2kelvin(212)
print k1, k2

# prints hello, world!
def hello():
    print "Hello, world!"

# functions can be void if they do not include 'return' command to return a value:
    
# test!!!
hello()      # call to hello prints "Hello, world!"
h = hello()  # call to hello prints "Hello, world!" a second time
print h      # prints None since there was no return value equal to h, h is void
