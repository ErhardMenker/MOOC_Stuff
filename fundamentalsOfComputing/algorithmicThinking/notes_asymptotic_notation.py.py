### Asymptotic Notation

# "Big O" notation is an example of asymptotic notation, meaning that the running time of an algorithm is expressed related to a mathematical function.
# Given an algorithm f, which is a function of input n or f(n), algorithm f(n) = O(g(n)) iff at every value of n sufficiently large, function g(n) multiplied by...
# ... some non-negative constant c is greater than or equal to f(n) (the algorithm is less computational than this function).
# If algorithm f(n) is greater than or equal to non-negative constant times the function's g(n) run time at a sufficiently large n, then f(n) = OMEGA(g(n)) (the algorithm is... 
# ...more comptational than this function).
# If at every point beyond a fixed n, there exists two constants c1 an c2 such that c1 * g(n) is greater than algorithm f(n) but c2 * g(n) is less than f(n),...
# ...then f(n) = THETA(g(n))) (the algorithm's run time is sandwiched between this function's computational time).
# If f(n) is OMEGA(g(n)) and O(g(n)), then f(n) is THETA(g(n)) and vice versa.
