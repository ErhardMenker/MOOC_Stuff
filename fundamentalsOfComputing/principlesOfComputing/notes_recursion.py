### Recursion

# Recursion is the process by which a function calls itself.
# Every time the function is called, it must have less data (or the recurion will last infinitely).
# Example: sum n as (1 + n - 1) which is itself (1 + 1 + n - 2) and so on...
# Recursive functions can be broken down into the base case which is solvable directly, and the recursive/inductive case which is not.
# Consider the function sum_up2 which adds up to that number...
# ...the base case is 1 when n = 1, while the recursion case is n + sum_up2(n - 1) when n is greater than one.
# Recursion involves calling a function while you define it; this is alright.

def sum_up_to(n):
    
	"""
    Function to sum up all the numbers less than or equal to n
    """
	
	if n == 1:
        # base case
        return 1
    else:
        # recursive case
        return n + sum_up_to(n - 1)

print sum_up_to(1)
print sum_up_to(2)
print sum_up_to(10)
print sum_up_to(55)

print sum(range(56))

def is_palindrome(word):
    
	"""
	Test if a word is a palindrome by testing whether ending words equal until 1 or 2 letters are left
	"""
	
	if len(word) < 2:
        # base case
        return True
    else:
        # recursive case
        if word[0] != word[-1]:
            return False
        else:
            #return the is_palindrome test result for the same list but without the first and last element.
			return is_palindrome(word[1:-1])

print is_palindrome("a")
print is_palindrome("aa")
print is_palindrome("is")
print is_palindrome("madamimadam")
print is_palindrome("abcdefdcba")
